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
