#!/usr/bin/env bash

set -eux

aws s3 sync workdir/index/ s3://ansible-pypi-test-mirror/ --delete
