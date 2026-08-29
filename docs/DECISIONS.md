# Decision Log

This is a lightweight pre-RFC decision log. Add entries when a choice materially constrains the project. Do not use this as a changelog.

## D-001 — Own assurance semantics, not the agent runtime

**Status:** Accepted

We will not build a coding agent, model gateway, sandbox, orchestration runtime, generic SDLC engine, observability backend, or general policy engine.

**Why:** These layers are already crowded and moving quickly. GitHub Spec Kit, OpenAI Symphony, Harbor, Agentplane, Nexus Agents, provider-native agents, CI systems, OPA, and OpenTelemetry cover much of this territory.

**Consequence:** Agent Assurance must integrate with or consume these systems through small adapters and portable records.

---

## D-002 — Four primitives for v0

**Status:** Accepted

The v0 model contains exactly:

- Task
- Evidence
- Capability
- Decision

**Why:** They are the minimum objects needed to express `Can it? → May it? → Did it prove it?` without committing to a full workflow protocol.

**Consequence:** New primitives require evidence from a real replay/runtime experiment.

---

## D-003 — Agent configuration is the capability subject

**Status:** Accepted

Capability attaches to the full evaluated configuration, not the model brand alone.

A configuration may include model/version, harness, system/repository instructions, tool surface, retrieval/context strategy, permissions, and verifier setup.

**Why:** Changes outside the base model can materially change engineering outcomes.

**Consequence:** Material configuration changes may invalidate qualification and require re-evaluation.

---

## D-004 — Capability is scoped, not global

**Status:** Accepted

Capability should be expressed over a task/risk scope such as stage, task family, subsystem/domain, and relevant risk properties.

**Why:** Routine implementation success does not justify autonomy for authorization, migration, or high-blast-radius work.

**Consequence:** The framework should produce capability profiles rather than one agent score.

---

## D-005 — Evidence before autonomy

**Status:** Accepted

Autonomy recommendations must be grounded in observed/verified evidence. Deterministic evidence is preferred when available.

**Why:** Agent self-report is insufficient for engineering assurance.

**Consequence:** Tests, CI results, static analysis, security checks, and independently observed state should be first-class inputs to Evidence.

---

## D-006 — Observe before enforce

**Status:** Accepted

The adoption path is Observe → Advise → Enforce.

**Why:** Teams should get value from evaluation without migrating workflow or granting new automation authority.

**Consequence:** v0 decisions are advisory. CI enforcement is a later optional integration.

---

## D-007 — Historical replay is the first validation method

**Status:** Accepted

Use completed engineering work to reconstruct realistic tasks from pre-change repository state and evaluate agents against behavioral/verification contracts.

**Why:** Historical work reflects the codebase and engineering environment better than generic public leaderboards.

**Consequence:** Do not require generated patches to match the historical human patch exactly; evaluate required behavior and constraints.

---

## D-008 — Reuse existing historical-eval infrastructure where possible

**Status:** Accepted

Before implementing mining/execution, evaluate interoperability or adapters with CodeProbe, AIBench Arena, and Harbor.

**Why:** Historical task reconstruction and isolated agent execution are no longer unique whitespace.

**Consequence:** Our differentiated output is portable Evidence/Capability/Decision semantics and the connection from evaluation to autonomy.

---

## D-009 — Pre-RFC project with explicit kill criteria

**Status:** Accepted

Do not stabilize a protocol until real experiments demonstrate that the objects are useful and defensible.

Stop, narrow, or merge upstream if an established standard covers the same semantics, portability fails, or teams do not use capability evidence to inform autonomy.

---

## D-010 — Use Click for the first historical replay

**Status:** Accepted

Use [pallets/click](https://github.com/pallets/click) as the first historical
replay repository. Use attrs as the leading candidate for a later
cross-repository transfer experiment.

**Why:** Click ranked highest against the experiment criteria after comparison
with attrs, HTTPX, Rich, and itsdangerous. It combines a large merged-PR corpus,
a compact Python-only implementation, pytest-based verification, and diverse
behavioral tasks. HTTPX carries more network and protocol-environment
complexity, Rich has more rendering ambiguity, and attrs and itsdangerous have
less varied candidate corpora for the first suite.

**Consequence:** Reconstruct 10–15 Click tasks at their recorded pre-change
commits. Keep all evaluation activity local and do not submit generated work or
automated feedback upstream. Re-evaluate the choice if historical dependencies
or held-out tests cannot be reproduced reliably.

---

## D-011 — Split mining and execution across CodeProbe and Harbor

**Status:** Accepted for the first experiment

Use CodeProbe for candidate mining, historical-state reconstruction, task
provenance, and initial verification-contract generation. Convert accepted
tasks through a small adapter into Harbor tasks, then use Harbor for isolated
multi-agent execution and trial result capture.

Apply AIBench Arena's fail-to-pass validation rule before accepting any mined
task: its verifier must fail at the pre-change state and pass after the
historical fix is applied. A task that does not demonstrate this transition is
rejected or receives a purpose-built held-out verifier.

**Why:** CodeProbe most directly covers repository-history mining, but its
Codex execution path is marked unsupported. Harbor supports Codex, Claude Code,
and other agents in reproducible container environments and emits structured
trial results. AIBench Arena has strong validation and contamination controls,
but its agent process currently runs on the host and its task format is not the
best interoperability boundary for this experiment.

**Consequence:** Agent Assurance owns only two thin mappings:

- CodeProbe task/provenance to the existing `Task` record and Harbor task
  package;
- Harbor `results.json` to the existing `Evidence` record.

Do not adopt another project's ranking, capability, or policy model. Do not
build an executor, sandbox, benchmark miner, or leaderboard.
