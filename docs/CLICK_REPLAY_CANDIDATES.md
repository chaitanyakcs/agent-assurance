# Click Historical Replay Candidates

This is the working candidate set for the first historical replay experiment.
It is not yet an executable benchmark manifest.

## Selection method

On 2026-08-30, we screened 50 merged Click pull requests from 2024–2025 and
inspected metadata and changed files for 15 promising candidates. Candidates
were favored when they had:

- a problem statement that can be separated from the historical solution;
- a precise pre-change commit;
- deterministic verification or a feasible held-out regression test;
- a small enough change surface for repeatable agent trials;
- useful diversity across task family and difficulty;
- no required proprietary service or upstream interaction.

Release chores, dependency refreshes, documentation-only changes, and tasks
whose main difficulty was unavailable platform infrastructure were excluded.

## Proposed suite

| PR | Family | Pre-change commit | Change surface | Verification basis |
| --- | --- | --- | --- | --- |
| [#3152](https://github.com/pallets/click/pull/3152) | routine bug | `7f7bbe4569ea68e8dabee232eade069ef3310aea` | option parsing | Existing and held-out option tests for `is_flag=False` with `flag_value` |
| [#3013](https://github.com/pallets/click/pull/3013) | routine bug | `1c68e531ef5e45f6facdb777c720d0f984614b81` | Fish completion | Existing shell-completion tests for quoted and escaped values |
| [#3004](https://github.com/pallets/click/pull/3004) | routine bug | `a1235aacb1be55dc66ddcfefbf64dec44b6ab54d` | help rendering | Existing option tests plus held-out Enum-default cases |
| [#2930](https://github.com/pallets/click/pull/2930) | routine bug | `011b9f9d190c71310264e6c54bae6259f5e38a9f` | flag typing/value | Existing option tests covering typed flags and falsey types |
| [#3079](https://github.com/pallets/click/pull/3079) | debugging bug | `6a1c0d077311f180b356965914e2de5b9e0fdb44` | default resolution | Existing default tests plus order-invariance cases |
| [#2940](https://github.com/pallets/click/pull/2940) | debugging bug | `36deba8a95a2585de1a2aa4475b7f054f52830ac` | `CliRunner` input | Existing chain tests plus stdin/EOF regression coverage |
| [#2935](https://github.com/pallets/click/pull/2935) | debugging bug | `884af5c20fdc95c9c7352df35c37273391464fb9` | nested completion | Existing shell-completion tests with held-out nesting cases |
| [#3058](https://github.com/pallets/click/pull/3058) | feature/API | `16fe802a3f96c4c8fa3cd382f1a7577fda0c5321` | context resources | Existing context tests for exception propagation and normal close behavior |
| [#2630](https://github.com/pallets/click/pull/2630) | typing feature | `0d69b6ce8b25fe31ea580c608adb8e45df3805bb` | progress-bar overloads | Historical typing suite and runtime tests |
| [#3023](https://github.com/pallets/click/pull/3023) | refactor/performance | `4f936ac1981645488f396953bc59e50445de00b6` | import boundaries | Existing import tests plus a deterministic module-import assertion |
| [#2855](https://github.com/pallets/click/pull/2855) | tool integration | `b88c4841ad53247e9ca6f9fd39d510e99d6c18f7` | Pyright compatibility | Pinned Pyright verification; historical patch added no test file |
| [#3055](https://github.com/pallets/click/pull/3055) | risk-sensitive bug | `35e6a78646c58a8cc1ba3cda603a6bd4fb87f9d5` | pager subprocess | Held-out `Popen` argument/behavior test required; historical patch added no regression test |

The mix is four routine bugs, three debugging-heavy bugs, two feature/API
changes, one refactor/performance task, one tool-integration task, and one
risk-sensitive subprocess task.

## Alternates

| PR | Reason to keep in reserve |
| --- | --- |
| [#2944](https://github.com/pallets/click/pull/2944) | Useful multi-call binary behavior, but the historical patch has no regression test and realistic verification may require BusyBox or an equivalent fixture. |
| [#3070](https://github.com/pallets/click/pull/3070) | Deterministic packaging metadata task, but the one-line dependency-bound change may be too easy for the first suite. |
| [#3129](https://github.com/pallets/click/pull/3129) | Good BSD/GNU portability example, but it changes only a test and depends on platform tool behavior. |

## Reconstruction rules

For each selected task:

1. Check out the recorded pre-change commit, not the current branch.
2. Build the task narrative from the linked issue and information available
   before the PR, removing patch-specific solution hints.
3. Preserve the historical patch as an oracle, never as agent-visible context.
4. Verify behavior rather than patch equality.
5. Pin the repository dependencies and verifier versions used by the replay.
6. Add at least one held-out assertion where practical, and require it for
   candidates whose historical patch did not add a regression test.
7. Record platform-specific skips or failures as evidence, not silent success.

## Gate before execution

Before turning these rows into Task manifests, complete the reuse-first spike
for CodeProbe, AIBench Arena, and Harbor. The spike should determine whether an
existing miner can reconstruct these tasks and whether Harbor can execute them
while Agent Assurance only emits the four assurance records.
