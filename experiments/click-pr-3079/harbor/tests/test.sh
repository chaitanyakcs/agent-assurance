#!/usr/bin/env bash
set -euo pipefail

cd /app
git checkout -- tests/test_defaults.py
git apply /tests/golden-test.patch

if pytest tests/test_defaults.py -q -k shared_param_prefers_first_default; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
    exit 1
fi
