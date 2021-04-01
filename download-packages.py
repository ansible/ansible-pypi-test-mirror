#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argparse
import json
import os
import tempfile
import urllib.request

import argcomplete


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--requirement', metavar='file', action='append', dest='requirements', required=True)
    parser.add_argument('-d', '--dest', metavar='dir', default='workdir/packages/', dest='download_dir')

    argcomplete.autocomplete(parser)

    args = parser.parse_args()

    for requirement in args.requirements:
        download_requirements_file(requirement, args.download_dir)


def download_requirements_file(requirements_path: str, download_dir: str) -> None:
    with open(requirements_path) as requirements_file:
        requirements = requirements_file.read().splitlines()

    os.makedirs(download_dir, exist_ok=True)

    for requirement in requirements:
        download_requirement(requirement, download_dir)


def download_requirement(requirement: str, download_dir: str) -> None:
    package, version = requirement.split('==')

    print(f'{package}: {version}', flush=True)

    data = json.loads(urllib.request.urlopen(f'https://pypi.org/pypi/{package}/json').read())
    files = dict((item['filename'], item['url']) for item in data['releases'][version])

    for filename, url in files.items():
        path = os.path.join(download_dir, os.path.basename(filename))

        print(f'  {path} ... ', end='', flush=True)

        if os.path.exists(path):
            print('exists', flush=True)
            continue

        content = urllib.request.urlopen(url).read()

        temp_path = None

        try:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_path = temp_file.name
                temp_file.write(content)
                os.rename(temp_path, path)
                temp_path = None
        finally:
            if temp_path:
                os.remove(temp_path)

        print('downloaded', flush=True)


if __name__ == '__main__':
    main()
