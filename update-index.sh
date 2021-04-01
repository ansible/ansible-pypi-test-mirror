#!/usr/bin/env bash

set -eux

aws s3 ls s3://ansible-ci-files/pypi/packages/ | awk '{print $4}' > workdir/packages.txt

dumb-pypi \
  --package-list workdir/packages.txt \
  --output-dir workdir/index/ \
  --packages-url https://ansible-ci-files.s3.amazonaws.com/pypi/packages/ \
  --title "Ansible PyPI Test Mirror" \
  --no-generate-timestamp \
