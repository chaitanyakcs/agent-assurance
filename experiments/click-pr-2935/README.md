# Click PR 2935 Replay

Historical replay of nested-group shell completion at the pinned pre-change
commit. Hidden tests verify completion candidates at each command depth.

Harbor uses the public-network Docker baseline; generated Evidence must record
that network isolation was not enforced.

## Status

- Hidden verifier: fails at the pre-change commit; passes with the Oracle patch.
- Harbor Oracle: reward `1.0`.
- Codex `harbor/codex@0.153.4/gpt-5.5`: reward `1.0`.
