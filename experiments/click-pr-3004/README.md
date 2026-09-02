# Click PR 3004 Pilot Task

Historical replay package for Click issue #2911 / PR #3004.

The task reconstructs Click at pre-change commit
`a1235aacb1be55dc66ddcfefbf64dec44b6ab54d`. The hidden test checks that Enum
choice defaults are rendered by member name in help output while preserving
existing default behavior.

The task uses Harbor's `public` network baseline because its local Docker
provider rejects network policies it cannot enforce. A real trial on this
public repository must use a Harbor environment provider that can enforce
network isolation, or record the uncontrolled network as an evidence caveat.

## Status

- Initial Oracle attempt failed because the local golden patch metadata was
  malformed; this was a package authoring issue, not task evidence.
- Harbor Oracle passed after the patch fix on 2026-09-02: reward `1.0`, 0
  errors.
- Codex `gpt-5.5` passed on 2026-09-02: reward `1.0`, 0 errors.
- Evidence: `experiments/click-pr-3004/evidence/codex-gpt-5.5.yaml`.
- Codex `gpt-5.5` with `reasoning_effort=low` passed on 2026-09-02:
  reward `1.0`, 0 errors.
- Evidence:
  `experiments/click-pr-3004/evidence/codex-gpt-5.5-low-reasoning.yaml`.
