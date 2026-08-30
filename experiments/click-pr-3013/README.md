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
