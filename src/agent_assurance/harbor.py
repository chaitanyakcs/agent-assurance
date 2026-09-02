from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


def evidence_from_harbor_trial(
    trial_result_path: Path,
    *,
    task_id: str,
    evidence_id: str,
    verification_artifact: str | None = None,
    notes: str | None = None,
) -> dict[str, Any]:
    """Map one Harbor trial result to the v0 Evidence schema."""
    trial = json.loads(trial_result_path.read_text(encoding="utf-8"))
    agent_info = trial.get("agent_info") or {}
    model_info = agent_info.get("model_info") or {}
    agent_result = trial.get("agent_result") or {}
    verifier_result = trial.get("verifier_result") or {}
    rewards = verifier_result.get("rewards") or {}
    exception_info = trial.get("exception_info")

    reward = rewards.get("reward")
    if exception_info is not None:
        status = "aborted"
    else:
        status = "success" if reward == 1.0 else "failure"

    started = _parse_datetime(trial.get("started_at"))
    finished = _parse_datetime(trial.get("finished_at"))
    duration_seconds = None

    if started is not None and finished is not None:
        duration_seconds = max((finished - started).total_seconds(), 0.0)

    configuration = _configuration_name(agent_info, model_info)

    outcome: dict[str, Any] = {"status": status}

    if duration_seconds is not None:
        outcome["duration_seconds"] = round(duration_seconds, 3)

    if agent_result.get("cost_usd") is not None:
        outcome["cost"] = agent_result["cost_usd"]

    note_parts = []

    if notes:
        note_parts.append(notes)

    note_parts.extend(_harbor_note_parts(trial, agent_result))

    if exception_info is not None:
        note_parts.append(
            "Harbor exception: "
            f"{exception_info.get('exception_type', 'unknown')}."
        )

    if note_parts:
        outcome["notes"] = " ".join(note_parts)

    verification: dict[str, Any] = {
        "type": "test",
        "name": "Harbor verifier reward",
        "result": _verification_result(reward, exception_info),
        "independent": True,
        "details": f"reward={reward!r}; verifier_environment_mode="
        f"{trial.get('verifier_environment_mode')!r}",
    }

    if verification_artifact:
        verification["artifact"] = verification_artifact

    return {
        "apiVersion": "assurance.agent/v0",
        "kind": "Evidence",
        "metadata": {
            "id": evidence_id,
            "created_at": trial["finished_at"],
        },
        "task": {"id": task_id},
        "executor": {
            "type": "agent",
            "provider": model_info.get("provider", "unknown"),
            "agent": agent_info.get("name", "unknown"),
            "model": model_info.get("name", "unknown"),
            "configuration": configuration,
        },
        "outcome": outcome,
        "verification": [verification],
    }


def _configuration_name(agent_info: dict[str, Any], model_info: dict[str, Any]) -> str:
    agent = agent_info.get("name", "unknown-agent")
    version = agent_info.get("version", "unknown-version")
    model = model_info.get("name", "unknown-model")
    return f"harbor/{agent}@{version}/{model}"


def _verification_result(
    reward: float | None, exception_info: dict[str, Any] | None
) -> str:
    if exception_info is not None:
        return "not_run"

    return "pass" if reward == 1.0 else "fail"


def _harbor_note_parts(trial: dict[str, Any], agent_result: dict[str, Any]) -> list[str]:
    fields = {
        "trial_name": trial.get("trial_name"),
        "trial_uri": trial.get("trial_uri"),
        "task_checksum": trial.get("task_checksum"),
        "input_tokens": agent_result.get("n_input_tokens"),
        "cache_tokens": agent_result.get("n_cache_tokens"),
        "output_tokens": agent_result.get("n_output_tokens"),
    }

    return [f"Harbor {key}={value}." for key, value in fields.items() if value is not None]


def _parse_datetime(value: str | None) -> datetime | None:
    if value is None:
        return None

    return datetime.fromisoformat(value.replace("Z", "+00:00"))
