# Click PR 3013 Pilot

This is the first end-to-end historical replay package. It reconstructs Click
at the first parent of the historical merge commit and keeps both the golden
regression test and oracle solution outside the agent-visible workspace.

Local fail-to-pass validation on 2026-08-30:

- pre-change source plus hidden regression test: 1 failed, 6 passed;
- historical source fix plus hidden regression test: 52 passed.

The temporary validation checkout was not committed and did not modify the
upstream Click repository.

Before a real trial, run one configured coding agent and convert Harbor's
`results.json` into an Agent Assurance Evidence record.

The task uses Harbor's `public` network baseline because its local Docker
provider rejects network policies it cannot enforce. A real trial on this
public repository must use a Harbor environment provider that can enforce
network isolation, or record the uncontrolled network as an evidence caveat.

## Harbor Oracle status

The first local Harbor 0.22.0 Oracle attempt was cancelled during
`docker compose build` after the Docker environment made no progress. Harbor's
captured result had no agent result and no verifier result. This is classified
as an infrastructure abort, not task evidence.

The Oracle gate passed on retry after Docker became responsive:

- command: `uvx harbor run -p experiments/click-pr-3013/harbor -a oracle`
- result: reward `1.0`, 1 completed trial, 0 errors;
- runtime: 56 seconds;
- Harbor result: `jobs/2026-08-30__10-03-47/result.json`.

This validates the Harbor package mechanics. It is not a Capability trial for a
coding agent configuration.

## Codex trial status

One real Codex trial passed on 2026-08-30:

- command: `CODEX_FORCE_AUTH_JSON=1 uvx harbor run -p experiments/click-pr-3013/harbor -a codex -m gpt-5.5 --n-concurrent 1`
- result: reward `1.0`, 1 completed trial, 0 errors;
- runtime: 4 minutes 12 seconds;
- Harbor job result: `jobs/2026-08-30__11-21-22/result.json`;
- Harbor trial result: `jobs/2026-08-30__11-21-22/harbor__9pm7v7b/result.json`;
- deterministic verifier output: `52 passed in 0.08s`.

Two prior Codex attempts are classified as infrastructure/configuration aborts:

- `jobs/2026-08-30__11-13-36/result.json`: missing explicit model name;
- `jobs/2026-08-30__11-15-39/result.json` and
  `jobs/2026-08-30__11-19-04/result.json`: model/auth mismatch before task
  execution.

The Evidence schema can represent the successful outcome, executor identity,
duration, cost, and verifier artifact. It does not yet have structured fields
for Harbor job ids, trial ids, task checksums, token/cache counts, exception
classes, verifier environment mode, or network-enforcement caveats. The pilot
Evidence records those as `outcome.notes` or `verification.details`; no schema
change was required for this task.

A second Codex configuration passed on 2026-09-02:

- command: `CODEX_FORCE_AUTH_JSON=1 uvx harbor run -p experiments/click-pr-3013/harbor -a codex -m gpt-5.5 --ak reasoning_effort=low --n-concurrent 1`
- result: reward `1.0`, 1 completed trial, 0 errors;
- Harbor trial result: `jobs/2026-09-02__07-51-37/harbor__NMmPcUL/result.json`;
- Evidence: `experiments/click-pr-3013/evidence/codex-gpt-5.5-low-reasoning.yaml`.
