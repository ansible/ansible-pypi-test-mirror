#!/usr/bin/env bash

set -eux

aws s3 sync workdir/packages/ s3://ansible-ci-files/pypi/packages/
