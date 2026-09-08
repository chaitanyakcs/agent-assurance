#!/bin/sh
set -eu
cd /app
git apply --unidiff-zero /tests/golden-test.patch
if pytest -q tests/test_aa_pr_3058.py; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
    exit 1
fi
