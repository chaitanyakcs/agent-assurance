# Click PR 3023 Replay

Historical replay of Click's lazy `shutil` import boundary. The verifier tracks
imports from Click modules in a fresh interpreter.

Harbor uses the public-network Docker baseline; generated Evidence must record
that network isolation was not enforced.

## Status

- Held-out direct-import verifier: fails at the pre-change commit; passes with
  the Oracle patch.
- Harbor Oracle: reward `1.0`.
- Codex `harbor/codex@0.153.4/gpt-5.5`: reward `1.0`.
