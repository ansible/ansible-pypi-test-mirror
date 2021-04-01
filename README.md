# ansible-pypi-test-mirror
Scripts to manage the Ansible PyPI Test Mirror.

> Only packages used for testing Ansible are included in the mirror.

The mirror can be used with the `pip` option: `-i https://d2c8fqinjk13kw.cloudfront.net/simple/`

Perform the following steps to update the package index in S3.

1. Run `pip install -r requirements.txt` to install requirements for the scripts.
1. Run `download-packages.py -r <requirements_file>` to download packages from PyPI.
1. Run `upload-packages.sh` to upload packages to S3.
1. Run `update-index.sh` to generate a local package index.
1. Run `upload-index.sh` to upload the local package index to S3.

> Packages are only required locally if they have not yet been uploaded to S3 with `upload-packages.sh`.
> Once packages have been uploaded to S3 the local copies can be deleted.
