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


def test_click_pilot_tasks_validate():
    schema = json.loads((ROOT / "schemas" / "task.schema.json").read_text())

    for path in sorted((ROOT / "experiments").glob("click-pr-*/task.yaml")):
        task = yaml.safe_load(path.read_text())
        errors = list(Draft202012Validator(schema).iter_errors(task))
        assert errors == []


def test_click_pilot_evidence_validates():
    schema = json.loads((ROOT / "schemas" / "evidence.schema.json").read_text())

    for path in (ROOT / "experiments" / "click-pr-3013" / "evidence").glob("*.yaml"):
        evidence = yaml.safe_load(path.read_text())
        errors = list(Draft202012Validator(schema).iter_errors(evidence))
        assert errors == []
