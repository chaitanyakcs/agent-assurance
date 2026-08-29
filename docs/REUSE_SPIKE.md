# Reuse-First Spike

Date: 2026-08-30

## Question

Which existing projects should provide historical task mining, agent
execution, isolation, and verification mechanics for the first replay?

## Findings

### CodeProbe

Repository: [sjarmak/codeprobe](https://github.com/sjarmak/codeprobe)

Best fit for historical mining and provenance. It can mine Python repository
history, pin the pre-change state, retain the ground-truth commit separately,
generate task instructions and verification contracts, and export structured
results. Its task model records the complete configuration rather than only a
model label, which aligns with this project.

Important limits:

- CodeProbe is beta software.
- Its built-in Codex path is explicitly marked unsupported for repository-edit
  comparisons.
- Selecting tests touched by a historical PR is useful but is not sufficient
  proof that those tests fail before the fix.
- Its `task.toml` schema is not directly compatible with Harbor's current task
  schema, so conversion must be explicit and tested.

Decision: reuse mining and provenance; do not use its runner for the initial
multi-agent comparison.

### AIBench Arena

Repository:
[Elnino0009/aibench-arena](https://github.com/Elnino0009/aibench-arena)

Strongest contribution is methodological. It requires a candidate verifier to
fail at the parent commit and pass after applying the historical fix. It also
uses truncated histories, hides golden tests during execution, rejects flaky or
ungradeable tasks, separates infrastructure failures, and reports confidence
intervals rather than overclaiming from a small sample.

Important limits:

- The primary workflow is an end-to-end benchmark and leaderboard rather than
  a reusable task interchange layer.
- Setup and tests can run in Docker, but the coding-agent process currently
  runs on the host.
- Feature tasks are experimental and command oracles can be gamed.

Decision: adopt its fail-to-pass acceptance gate and contamination controls;
do not make it the core runner or data model.

### Harbor

Repository: [harbor-framework/harbor](https://github.com/harbor-framework/harbor)

Best fit for execution. Harbor supports multiple installed and external agents,
including Codex CLI and Claude Code, runs tasks in container environments,
supports hidden or separate verifier environments, and records task checksums,
resolved configuration, agent/version/model identity, timing, verifier results,
tokens, cost, errors, logs, and artifacts in each trial's `results.json`.

Important limits:

- Harbor does not reconstruct tasks from repository history.
- A Harbor task needs an explicit environment, instruction, verifier, and
  optional oracle solution.
- Harbor's reward is execution evidence, not an Agent Assurance capability or
  autonomy decision.

Decision: reuse execution, isolation, and raw trial records; adapt those records
to `Evidence` without importing Harbor's broader benchmark semantics.

## Selected flow

```text
Click history
    |
    v
CodeProbe mine + provenance
    |
    v
fail-before / pass-after acceptance gate
    |
    v
thin CodeProbe-to-Harbor task adapter
    |
    v
Harbor agent trials + results.json
    |
    v
thin Harbor-to-Evidence adapter
    |
    v
Capability aggregation -> advisory Decision
```

## Smallest pilot

Use Click PR
[#3013](https://github.com/pallets/click/pull/3013), which fixes Fish
completion for quoted or escaped parameters.

The pilot is complete only when:

1. the repository can be reconstructed at pre-change commit
   `1c68e531ef5e45f6facdb777c720d0f984614b81`;
2. the verifier demonstrably fails before the fix and passes after it;
3. the task converts into a valid Harbor package without solution leakage;
4. Harbor's oracle run passes;
5. one real agent trial produces a valid Agent Assurance `Evidence` record.

## Adapter boundary

The first adapter should map fields, not create a new framework:

| Source | Destination |
| --- | --- |
| CodeProbe task ID and ground-truth commit | `Task` provenance/reference fields |
| CodeProbe instruction | Harbor `instruction.md` and `Task` description |
| CodeProbe test command plus held-out checks | Harbor hidden verifier |
| Pinned pre-change repository state | Harbor environment build input |
| Harbor task checksum and resolved config | `Evidence` provenance |
| Harbor agent/version/model and tool configuration | `Evidence` subject configuration |
| Harbor verifier result, timing, tokens, cost, and errors | `Evidence` outcome and measurements |

Any field that cannot map to one of the four existing primitives should first be
recorded as experiment feedback, not added automatically to a schema.
