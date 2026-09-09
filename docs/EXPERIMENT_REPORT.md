# Click Historical Replay Experiment Report

Date: 2026-09-08

## Executive summary

The first historical replay experiment supports continuing Agent Assurance as
a small assurance-semantics project, but it does not yet justify an RFC.

Ten Click changes were reconstructed as replayable Harbor tasks. Every hidden
verifier demonstrated a fail-before/pass-after transition, every task passed a
Harbor Oracle run, and `harbor/codex@0.153.4/gpt-5.5` passed all ten completed
agent trials. Earlier runs also produced results for two distinct Codex 0.152.1
configurations. Twenty-one Evidence records, six Capability records, and one
advisory Decision now exercise all four v0 primitives.

The four primitives were sufficient to complete the experiment without adding
a fifth object or changing a schema. They were not sufficient to represent all
important provenance, failure classification, and aggregation rationale as
structured data. Those gaps are documented below and should be tested with a
second agent and repository before any schema expansion.

Recommendation: **continue with adjustments**. Keep the project pre-RFC and
thin. Next validate vendor neutrality on the same tasks, then test transfer to
a second repository. Do not build execution, mining, policy, or observability
infrastructure.

## Experiment delivered

The accepted Click suite contains ten implementation tasks:

| Task | Family | Risk | Deterministic verifier |
| --- | --- | --- | --- |
| #3152 | bugfix | low | option parsing tests |
| #3013 | bugfix | low | Fish completion tests |
| #3004 | bugfix | low | Enum default help tests |
| #2930 | bugfix | low | typed flag-value tests |
| #3079 | bugfix | low | default order-invariance tests |
| #2940 | bugfix | low | stdin/EOF chain tests |
| #2935 | bugfix | low | nested completion tests |
| #3058 | feature | medium | context-resource exception tests |
| #2630 | typing | low | pinned mypy assertions |
| #3023 | refactor | low | direct import-boundary test |

For every task, the verifier failed at the pinned pre-change commit and passed
after the historical source fix. The historical patch was hidden from the
agent, and verification checked behavior or static typing rather than patch
equality.

## Observed capability

The experiment produced configuration-specific, task-scoped results:

| Configuration | Scope | Completed result | Qualification |
| --- | --- | --- | --- |
| `harbor/codex@0.152.1/gpt-5.5` | Click bugfix | 2/2 valid exact-digest records | L0, insufficient evidence |
| `harbor/codex@0.152.1/gpt-5.5 (reasoning_effort=low)` | Click bugfix | 3/4 | L0, insufficient evidence |
| `harbor/codex@0.153.4/gpt-5.5` | Click bugfix | 6/6 valid records | L1, low confidence |
| `harbor/codex@0.153.4/gpt-5.5` | Click feature | 1/1 | L0, insufficient evidence |
| `harbor/codex@0.153.4/gpt-5.5` | Click typing | 1/1 | L0, insufficient evidence |
| `harbor/codex@0.153.4/gpt-5.5` | Click refactor | 1/1 | L0, insufficient evidence |

The 0.153.4 results must not be read as a global 10/10 agent score. Seven
bugfixes support only a low-confidence Click bugfix statement. The other three
families each have one trial and remain insufficient evidence. No result
supports autonomy for high-risk work, other repositories, review, operations,
or incident response.

The low-reasoning timeout on #3079 shows why a model name is not a capability
subject. Agent version and reasoning configuration changed observed outcomes.

## Advisory Decision result

The first Decision allowed implementation of held-out, low-risk bugfix #2930
while requiring human involvement before opening or merging a pull request.
That autonomy boundary remains defensible for a low-confidence pilot.

The held-out run passed, but Harbor installed Codex CLI 0.153.4 while the
Decision referenced 0.152.1. The result therefore supported the task strategy
without strictly confirming the selected Capability. Keeping the two digests
separate prevented silent capability inheritance and validated configuration
change as an invalidation condition.

## Answers to experiment questions

### Are the four primitives sufficient?

Yes for the first end-to-end loop. Task described the work and risk, Evidence
recorded each trial, Capability aggregated matching trials, and Decision
expressed advisory permissions. No additional primitive was required.

The schemas are intentionally lossy. Important details had to remain in text
notes, and Capability aggregation was performed manually. This is acceptable
for a pilot but not yet a stable interchange contract.

### Which fields were hard to populate objectively?

- Task family, complexity, blast radius, and risk required human judgment.
- A single task can plausibly fit more than one family, while v0 records one.
- Qualification level and confidence have labels but no normative calculation.
- “Independent” verification was easy to assert but not rigorously defined.
- The complete agent configuration was only partially observable from Harbor.
- Historical issue text sometimes contained solution hints and required manual
  rewriting to form a fair instruction.

### Was classification consistent enough for policy?

Consistent enough for a narrow advisory Decision, not for enforcement. Low-risk
Click bugfixes were reasonably distinguishable from the medium-risk resource
lifecycle feature. Boundaries between bugfix, feature, typing, and refactor
still depended on judgment and could change aggregation outcomes.

### What was a material configuration change?

The experiment treated agent version, model, agent kwargs such as reasoning
effort, skills, and MCP server configuration as digest inputs. Codex CLI
0.152.1 and 0.153.4, and default versus low reasoning, produced separate
subjects.

This identity is still incomplete. The digest does not yet cover Harbor
version, container image, repository instructions, effective tool permissions,
network policy, or broader environment state. Those omissions should be
resolved before configuration digests are treated as portable attestations.

### Did historical replay overestimate capability?

Probably, but this experiment cannot quantify the effect. Tasks were selected
for deterministic reconstruction and had historical fixes in public history.
Agents may have prior exposure to the repository or change. One successful run
per task also hides non-determinism. The results demonstrate repeatable task
completion in this setup, not novel-task reliability or production safety.

### How should failures affect qualification?

Agent execution failures and infrastructure failures must remain separate.
Observed infrastructure failures included Codex installation failures, an
agent setup timeout, and a hidden-test patch collision. These produced aborted
Evidence with verification `not_run` and were excluded from Capability attempt
counts. Corrected retries were recorded separately.

The low-reasoning #3079 timeout occurred during agent execution and remained an
aborted trial in that configuration's four-trial aggregate. This distinction
prevented broken infrastructure from lowering capability while preserving an
agent configuration's inability to finish within its budget.

### Was the autonomy recommendation defensible?

Yes as an advisory, low-risk recommendation with human gates. Allowing local
implementation while requiring human review before pull request and merge was
originally appeared proportionate to three exact-digest bugfix passes and low
confidence. After #3152's verifier failed a no-op control, the exact support
fell to 2/2 and L0; implementation now requires human involvement. The evidence
does not support unattended publication or merge authority.

## Schema mismatches observed

No schema was changed during the experiment. The following mismatches should
be candidates for later testing, not automatic additions:

### Evidence

- Harbor job ID, trial ID, task checksum, token/cache counts, exception class,
  verifier environment mode, and network enforcement are stored in free-text
  notes or details.
- Failure phase is not structured, making setup, execution, and verification
  aborts difficult to aggregate reliably.
- Cost has no currency or pricing provenance.
- Verification artifacts are paths, without digest or retention semantics.
- Evidence has no structured environment or harness-version provenance.

### Capability

- Capability does not reference the Evidence records used in aggregation.
- Confidence has no method, interval, sample exclusions, or repeat-trial data.
- Failure severity and infrastructure exclusion counts are not represented.
- One `task_family` value prevents multi-label tasks but usefully discourages
  broad aggregation.

### Task

- Requirements are strings rather than structured functional, regression,
  constraint, and risk checks.
- Classification provenance and reviewer agreement are not represented.
- The source can identify a revision and issue but not a complete reconstruction
  recipe or dependency lock provenance.

### Decision

- Decision embeds demonstrated level and confidence but does not reference a
  specific Capability record.
- Reasoning and required runtime evidence are strings without shared semantics.
- There is no decision timestamp, issuer, expiry, or policy identity.

## Reuse findings

The reuse-first design held up:

- Harbor provided container execution, agent integration, Oracle runs,
  structured results, logs, verifier artifacts, costs, tokens, and errors.
- AIBench Arena's fail-before/pass-after rule prevented accepting weak tests.
  It caught the initial #3023 verifier, which passed before the fix and had to
  be strengthened.
- CodeProbe remains the preferred source for future mining and provenance, but
  this small suite still required manual reconstruction and packaging.
- Agent Assurance needed only a thin Harbor-results-to-Evidence adapter and the
  four assurance documents. No runtime, sandbox, router, policy engine,
  dashboard, or proprietary telemetry was needed.

## Limitations

- One repository, language, ecosystem, and implementation stage.
- Only Codex configurations; vendor neutrality is a schema claim, not yet an
  empirical result.
- Mostly low-risk tasks and no security-sensitive task.
- One completed trial per task/configuration in most cases.
- Public network access was enabled because local Harbor Docker could not
  enforce isolation.
- Public historical changes create contamination risk.
- Capability levels and confidence thresholds remain provisional.
- No experienced external engineer has reviewed the classifications or
  autonomy Decision.

## Recommendation and next gates

Continue, with the following order:

1. Run a second agent implementation against the same ten packages and verify
   that equivalent configuration and failure data map cleanly into Evidence.
2. Repeat a subset of tasks per configuration to measure non-determinism and
   test confidence aggregation.
3. Replay a small suite from a second repository, with attrs as the current
   candidate, to test transfer and repository scoping.
4. Ask experienced engineers and maintainers of adjacent projects to review
   the Task classifications, Capability statements, and advisory Decision.
5. Revisit only the schema mismatches that recur across those experiments.

Do not begin enforcement or write an RFC until vendor neutrality, repeat-trial
behavior, and cross-repository portability have been demonstrated. Stop or
narrow the project if teams find the benchmark useful but would not consume
Capability or Decision records in autonomy workflows.
