# Click PR 2930 Held-Out Task

Historical replay package for Click PR #2930.

This task was selected as the first held-out task for the initial advisory
Decision. It reconstructs Click at pre-change commit
`011b9f9d190c71310264e6c54bae6259f5e38a9f`. The hidden regression test and
oracle source patch are not agent-visible.

The task uses Harbor's `public` network baseline because its local Docker
provider rejects network policies it cannot enforce. A real trial on this
public repository must use a Harbor environment provider that can enforce
network isolation, or record the uncontrolled network as an evidence caveat.

## Status

- Harbor Oracle passed on 2026-09-06: reward `1.0`, 0 errors.
- Codex `gpt-5.5` passed on 2026-09-06: reward `1.0`, 0 errors.
- Evidence: `experiments/click-pr-2930/evidence/codex-gpt-5.5.yaml`.
- This supports the first advisory Decision outcome for this held-out task, but
  it is not a strict confirmation because Harbor installed Codex CLI `0.153.4`
  while the Decision referenced the earlier `0.152.1` configuration digest.
