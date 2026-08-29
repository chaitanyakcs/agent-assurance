# First Historical Replay Experiment

This experiment is the gate before an RFC.

## Question

Can we make a defensible statement about what a **specific agent configuration** has demonstrated it can do, and use that statement to make a sensible autonomy recommendation for a new task?

## Scope

Use one public OSS repository and initially select **10–15 historical changes**, not 30. Thirty is a useful first internal suite target once the mechanics and taxonomy are validated.

The selected repository should have:

- deterministic, reasonably fast tests;
- meaningful merged PR history with issue/PR descriptions;
- enough non-trivial bug/feature/refactor work;
- reproducible historical dependencies/builds;
- no unusually complex proprietary infrastructure requirements;
- a license and contributor history compatible with this evaluation use.

## Reuse-first spike

Before implementing historical mining or agent execution:

1. Inspect **CodeProbe** for task reconstruction and verification-contract support.
2. Inspect **AIBench Arena** for its repo-history task model and model-comparison workflow.
3. Inspect **Harbor** for execution/isolation and multi-agent integration.
4. Decide whether the smallest path is:
   - emit Agent Assurance records from one of these directly;
   - write an adapter/importer;
   - use Harbor as execution while another tool mines tasks;
   - write only missing glue.

Record the decision in `docs/DECISIONS.md`.

## Initial task mix

Do not chase perfect balance with 10–15 tasks. Prefer diversity and replay quality.

Target roughly:

- 3–4 routine bug fixes;
- 2–3 harder/debugging bugs;
- 2–3 feature changes;
- 1–2 refactors;
- 1–2 integration/API changes;
- 1 security/risk-sensitive example if a safe, well-tested historical task exists.

Review and incident-response evals can follow after implementation replay proves the core objects.

## Historical task reconstruction

For each task, reconstruct only information plausibly available at the beginning:

- base/pre-change commit;
- issue/PR problem narrative (remove solution leakage where necessary);
- repository instructions/docs available at that commit;
- normal tooling/dependencies;
- relevant public context that an engineer would have had.

Keep the historical patch/merge commit as oracle/reference, but **do not require patch equality**.

## Evaluation contract

Each task should specify success through behavior and constraints, e.g.:

```yaml
functional:
  - duplicate request is idempotent
  - valid request behavior remains unchanged

verification:
  - existing unit tests
  - held-out regression test
  - lint/typecheck

constraints:
  - no unrelated schema change
  - no new external dependency

risk_checks:
  - authorization boundary unchanged
```

Prefer held-out tests or verification artifacts that the evaluated agent cannot trivially optimize against.

## Trials

Use at least two agent configurations. Example:

- Codex configuration A
- Claude Code configuration B

Record the exact configuration sufficiently to distinguish meaningful changes:

- agent/harness/version;
- model identifier/version where available;
- repository instruction digest;
- tool surface;
- network/permission limits;
- relevant context/retrieval setup;
- verifier/evaluator version.

Where cost permits, repeat tasks to expose non-determinism rather than treating a single run as absolute capability.

## Evidence

Emit one `Evidence` record per trial containing, at minimum:

- task reference;
- subject configuration;
- execution outcome;
- deterministic verification results;
- timing/cost/token data when reliably available;
- failure category;
- provenance needed to reproduce the run.

Do not let an LLM judge be the only successful verifier.

## Capability aggregation

The first aggregation can be simple, but must not hide sample size.

A Capability record should communicate:

- scope/task family;
- number of tasks/trials;
- success rate;
- failure severity where relevant;
- confidence/qualification level;
- configuration identity;
- freshness/validity conditions.

Avoid pretending that `9/10 = 90% certain autonomy`.

Initial qualification levels (`L0`–`L3`, etc.) are provisional and should be treated as a usability experiment, not a normative standard.

## First Decision

After the capability report exists, classify one new/held-out task and emit an advisory `Decision` such as:

```text
implement       ALLOW
open_pr         ALLOW
merge           REQUIRE_HUMAN
```

The decision explanation must make the chain inspectable:

```text
Task class/risk
   +
matching Capability and qualification
   +
required current Evidence
   =
Decision
```

## What to learn

The experiment should explicitly answer:

1. Are `Task`, `Evidence`, `Capability`, and `Decision` sufficient?
2. Which fields were hard to populate objectively?
3. Can task classifications be consistent enough for policy?
4. What qualifies as a material agent-configuration change?
5. Does historical test evidence overestimate capability?
6. How should sample size/confidence/failure severity affect qualification?
7. Does the resulting autonomy recommendation feel defensible to experienced engineers?
8. Which mechanics should be delegated to existing OSS projects?

## Output before RFC

Produce:

- 10–15 replayable tasks;
- Evidence records for at least two agent configurations;
- at least one Capability profile;
- one advisory Decision;
- a short experiment report documenting schema failures and reuse decisions.

Only then consider an RFC.
