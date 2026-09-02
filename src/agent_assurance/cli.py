from __future__ import annotations

import json
from pathlib import Path

import typer
import yaml
from jsonschema import Draft202012Validator

from .harbor import evidence_from_harbor_trial

app = typer.Typer(no_args_is_help=True, help="Agent Assurance reference CLI")

SCHEMA_NAMES = {"task", "evidence", "capability", "decision"}


def _repo_root() -> Path:
    # Editable/source installs resolve schemas from the repository. A packaged
    # schema-resource mechanism will be added if/when the CLI is published.
    return Path(__file__).resolve().parents[2]


def _schema_path(kind: str) -> Path:
    if kind not in SCHEMA_NAMES:
        raise typer.BadParameter(f"kind must be one of: {', '.join(sorted(SCHEMA_NAMES))}")
    return _repo_root() / "schemas" / f"{kind}.schema.json"


@app.command()
def init(path: Path = typer.Argument(Path(".agent-assurance"))) -> None:
    """Create a minimal local Agent Assurance configuration."""
    path.mkdir(parents=True, exist_ok=True)
    config = path / "config.yaml"
    policy = path / "policy.yaml"

    if not config.exists():
        config.write_text(
            "apiVersion: assurance.agent/v0\n"
            "kind: Config\n"
            "mode: observe\n"
            "evidence:\n"
            "  prefer_deterministic: true\n",
            encoding="utf-8",
        )

    if not policy.exists():
        policy.write_text(
            "# Advisory example only; v0 does not enforce policy.\n"
            "autonomy:\n"
            "  default:\n"
            "    implement: require_human\n"
            "    open_pr: require_human\n"
            "    merge: require_human\n",
            encoding="utf-8",
        )

    typer.echo(f"Initialized {path}")


@app.command()
def validate(kind: str, document: Path) -> None:
    """Validate a YAML or JSON document against one of the v0 schemas."""
    schema = json.loads(_schema_path(kind).read_text(encoding="utf-8"))
    raw = document.read_text(encoding="utf-8")
    data = json.loads(raw) if document.suffix.lower() == ".json" else yaml.safe_load(raw)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    if errors:
        for error in errors:
            location = ".".join(str(p) for p in error.path) or "<root>"
            typer.echo(f"ERROR {location}: {error.message}", err=True)
        raise typer.Exit(code=1)

    typer.echo(f"VALID {kind}: {document}")


@app.command("harbor-evidence")
def harbor_evidence(
    trial_result: Path,
    output: Path,
    task_id: str = typer.Option(..., help="Agent Assurance Task id."),
    evidence_id: str = typer.Option(..., help="Evidence metadata id."),
    verification_artifact: str | None = typer.Option(
        None, help="Optional verifier artifact path or URI."
    ),
    notes: str | None = typer.Option(None, help="Optional outcome note prefix."),
) -> None:
    """Convert one Harbor trial result into one v0 Evidence document."""
    evidence = evidence_from_harbor_trial(
        trial_result,
        task_id=task_id,
        evidence_id=evidence_id,
        verification_artifact=verification_artifact,
        notes=notes,
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        yaml.safe_dump(evidence, sort_keys=False),
        encoding="utf-8",
    )
    typer.echo(f"Wrote Evidence: {output}")


@app.command()
def version() -> None:
    from . import __version__

    typer.echo(__version__)


if __name__ == "__main__":
    app()
