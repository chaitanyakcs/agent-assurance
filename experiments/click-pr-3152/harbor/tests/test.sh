#!/usr/bin/env bash
set -euo pipefail

cd /app
git checkout -- tests/test_options.py
git apply /tests/golden-test.patch

if pytest tests/test_options.py -q -k flag_value_on_option_with_zero_or_one_args; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
    exit 1
fi
