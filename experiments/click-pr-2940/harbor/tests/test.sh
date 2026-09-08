#!/bin/sh
set -eu
cd /app
git checkout -- tests/test_chain.py
git apply --unidiff-zero /tests/golden-test.patch
if pytest -q tests/test_chain.py -k test_pipeline; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
    exit 1
fi
