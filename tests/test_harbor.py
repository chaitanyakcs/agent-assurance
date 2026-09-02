import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from agent_assurance.harbor import evidence_from_harbor_trial


def test_harbor_success_maps_to_evidence(tmp_path):
    trial_result = tmp_path / "result.json"
    trial_result.write_text(
        json.dumps(
            {
                "trial_name": "harbor__ok",
                "trial_uri": "file:///tmp/harbor__ok",
                "task_checksum": "sha256:task",
                "agent_info": {
                    "name": "codex",
                    "version": "0.151.0",
                    "model_info": {"name": "gpt-5.5", "provider": "openai"},
                },
                "agent_result": {"cost_usd": 0.5},
                "verifier_result": {"rewards": {"reward": 1.0}},
                "verifier_environment_mode": "shared",
                "exception_info": None,
                "started_at": "2026-08-30T00:00:00Z",
                "finished_at": "2026-08-30T00:00:10Z",
            }
        )
    )

    evidence = evidence_from_harbor_trial(
        trial_result,
        task_id="task-001",
        evidence_id="evidence-001",
    )

    assert evidence["outcome"]["status"] == "success"
    assert evidence["verification"][0]["result"] == "pass"


def test_harbor_exception_maps_to_aborted_evidence(tmp_path):
    trial_result = tmp_path / "result.json"
    trial_result.write_text(
        json.dumps(
            {
                "trial_name": "harbor__auth",
                "agent_info": {
                    "name": "codex",
                    "version": "0.151.0",
                    "model_info": {"name": "gpt-5", "provider": "openai"},
                },
                "agent_result": {},
                "verifier_result": {"rewards": {"reward": 0.0}},
                "exception_info": {"exception_type": "NonZeroAgentExitCodeError"},
                "started_at": "2026-08-30T00:00:00Z",
                "finished_at": "2026-08-30T00:00:10Z",
            }
        )
    )

    evidence = evidence_from_harbor_trial(
        trial_result,
        task_id="task-001",
        evidence_id="evidence-001",
    )

    assert evidence["outcome"]["status"] == "aborted"
    assert evidence["verification"][0]["result"] == "not_run"
