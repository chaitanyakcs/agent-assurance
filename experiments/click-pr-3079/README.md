# Click PR 3079 Pilot Task

Historical replay package for Click issue #3071 / PR #3079.

The task reconstructs Click at pre-change commit
`2ed395b0b5ac4d56553ff715335f456f812cdc78`. The hidden regression checks
shared flag defaults and explicit overrides for flags targeting the same
parameter name.

The task uses Harbor's `public` network baseline because its local Docker
provider rejects network policies it cannot enforce. A real trial on this
public repository must use a Harbor environment provider that can enforce
network isolation, or record the uncontrolled network as an evidence caveat.

## Status

- Harbor Oracle passed on 2026-09-02: reward `1.0`, 0 errors.
- Codex `gpt-5.5` passed on 2026-09-02: reward `1.0`, 0 errors.
- Evidence: `experiments/click-pr-3079/evidence/codex-gpt-5.5.yaml`.
- Codex `gpt-5.5` with `reasoning_effort=low` timed out during agent
  execution on 2026-09-02: reward `0.0`, `AgentTimeoutError`.
- Evidence:
  `experiments/click-pr-3079/evidence/codex-gpt-5.5-low-reasoning.yaml`.
