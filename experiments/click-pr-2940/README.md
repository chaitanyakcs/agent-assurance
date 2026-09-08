# Click PR 2940 Replay

Historical replay of the `CliRunner` EOF regression at Click's pinned
pre-change commit. The agent sees the behavioral contract but not the hidden
regression test or historical source patch.

Harbor uses the public-network Docker baseline because local network isolation
is not enforceable. This limitation must be retained in generated Evidence.

## Status

- Hidden verifier: fails at the pre-change commit; passes with the Oracle patch.
- Harbor Oracle: reward `1.0`.
- Codex `harbor/codex@0.153.4/gpt-5.5`: reward `1.0`.
- An initial Codex run completed agent execution but the hidden patch collided
  with an agent-edited test. It is recorded as an infrastructure abort and
  excluded from Capability counts; the isolated-verifier retry passed.
