#!/bin/sh
set -eu
cd /app
git apply --unidiff-zero /tests/golden-test.patch
if mypy tests/typing/typing_aa_pr_2630.py; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
    exit 1
fi
