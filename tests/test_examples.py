import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def test_minimal_examples_validate():
    for kind in ("task", "evidence", "capability", "decision"):
        schema = json.loads((ROOT / "schemas" / f"{kind}.schema.json").read_text())
        example = yaml.safe_load((ROOT / "examples" / "minimal" / f"{kind}.yaml").read_text())
        errors = list(Draft202012Validator(schema).iter_errors(example))
        assert errors == []
