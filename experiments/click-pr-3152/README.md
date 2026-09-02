# Click PR 3152 Pilot Task

Historical replay package for Click issue #3084 / PR #3152.

The task reconstructs Click at pre-change commit
`7f7bbe4569ea68e8dabee232eade069ef3310aea`. The golden regression test and
oracle source patch are hidden from the agent-visible workspace.

The task uses Harbor's `public` network baseline because its local Docker
provider rejects network policies it cannot enforce. A real trial on this
public repository must use a Harbor environment provider that can enforce
network isolation, or record the uncontrolled network as an evidence caveat.

## Status

- Harbor Oracle passed on 2026-09-02: reward `1.0`, 0 errors.
- Codex `gpt-5.5` passed on 2026-09-02: reward `1.0`, 0 errors.
- Evidence: `experiments/click-pr-3152/evidence/codex-gpt-5.5.yaml`.
