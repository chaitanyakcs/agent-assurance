#!/bin/sh
set -eu
cd /app
git apply --unidiff-zero /solution/source.patch
