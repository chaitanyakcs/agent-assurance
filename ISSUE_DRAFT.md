# Evolve assurance from point-in-time qualification to a persistent evidence graph

## Why this issue exists

Agent Assurance currently has a deliberately small v0 object model:

- Task
- Evidence
- Capability
- Decision

That model has been good enough to reach the first meaningful milestone. The historical replay experiment has produced real Evidence, provisional Capability records, and an advisory Decision. The project has also already validated an important principle: capability belongs to an exact agent configuration, not merely a model name, and configuration drift must not silently inherit prior qualification.

The next design question is whether assurance should remain primarily a sequence of point-in-time records, or evolve toward a persistent relationship model that accumulates what an agent configuration has demonstrated over time.

This issue explores the second direction.

The motivating mental model comes from recent discussion around loop engineering, harness engineering, and persistent graphs. The useful distinction is between:

1. a control graph, which describes orchestration such as agent/task transitions; and
2. a knowledge/evidence graph, which describes durable relationships accumulated across runs.

Agent Assurance should not become an orchestration graph or an agent runtime. The potentially relevant idea is the second one: an evidence graph.

## Current model

Today the conceptual path is approximately:

```text
Task
  ↓
controlled execution / replay
  ↓
Evidence
  ↓
Capability
  ↓
new Task + risk
  ↓
Decision
```

This is intentionally simple and should remain valid.

However, as the number of evaluated configurations, tasks, verifiers, environments, and runtime outcomes grows, the relationships between these records become as important as the records themselves.

For example, these questions become difficult to answer robustly if every result is treated as an isolated document:

- Which exact agent configurations have demonstrated capability for security-sensitive work?
- Which Capability statements depend on evidence from a harness version that has since changed?
- Which failures correlate with a tool version, instruction digest, permission set, or environment?
- Which Decision was supported by which Capability, and which underlying Evidence supported that Capability?
- If one verifier is later found to be invalid, which Capability and Decision records should be considered weakened or invalidated?
- Which pieces of qualification are still applicable when only one component of the agent configuration changes?
- What evidence supports increasing or decreasing autonomy for a configuration over time?

The data already forms a graph conceptually even if it is stored as JSON or relational rows.

## Proposed evolution

Treat the four existing primitives as the stable assurance vocabulary, but make their relationships and provenance explicit enough to support a persistent assurance graph.

Conceptually:

```text
                         ┌──────── model/version
                         ├──────── harness/version
                         ├──────── instructions/digest
Agent Configuration ─────┼──────── tools/tool versions
                         ├──────── retrieval/context strategy
                         ├──────── permissions
                         ├──────── environment
                         └──────── verifier setup
                                  │
                                  │ executed
                                  ↓
Task ─────────────────────────> Trial / attempt
                                  │
                                  │ produces
                                  ↓
                               Evidence
                              /    |    \
                             /     |     \
                    verified_by   |   observed_in
                          /         |         \
                     Verifier      |       Environment
                                   |
                            contributes_to
                                   ↓
                              Capability
                                   │
                        supports / invalidates
                                   ↓
                               Decision
                                   │
                                   ↓
                           runtime outcome
                                   │
                                   └────────→ future Evidence
```

Important: this diagram does **not** imply adding `Trial`, `Verifier`, `Environment`, or `AgentConfiguration` as new top-level assurance primitives. D-002 remains in force. They may remain fields, references, identities, or external entities unless experiments prove otherwise.

The design question is whether the existing schemas need stronger linkage semantics so that assurance can be reconstructed as a graph over time.

## What "evidence graph" should mean here

The phrase should refer to the **domain model**, not a database choice.

Do not introduce Neo4j, a graph database, a graph query language, or a new persistence platform merely because the relationships form a graph.

A first implementation may remain:

- JSON documents;
- SQLite/Postgres tables;
- append-only files;
- existing provenance records;
- a lightweight index derived from current schemas.

The requirement is that the relationships are explicit and queryable/reconstructable, not that storage is graph-native.

## Why this fits the existing project thesis

The current mission is:

> Build a vendor-neutral engineering assurance layer that lets software agents earn autonomy through demonstrated capability and verifiable evidence.

A persistent evidence model strengthens that thesis rather than broadening it into orchestration.

The system becomes capable of answering not only:

> What did this evaluation say?

but:

> What has this exact configuration demonstrated over time, what evidence supports that statement, what has changed since the evidence was collected, and how much of that qualification remains valid?

That is a stronger foundation for earned autonomy.

## Relationship to existing design decisions

This direction should preserve all current accepted decisions.

### D-001: own assurance semantics, not runtime

No agent runtime, router, policy engine, sandbox, graph orchestrator, or observability backend should be added.

The evidence graph is an assurance representation that consumes data from those systems.

### D-002: four primitives for v0

Do not add a fifth primitive just to represent a graph node.

First test whether references and linkage fields across Task, Evidence, Capability, and Decision are sufficient.

### D-003: configuration is the capability subject

This issue makes D-003 more important.

A useful evidence graph needs a stable way to identify an evaluated configuration and relate changes in its components to prior Evidence and Capability.

### D-004: capability is scoped

The graph should preserve scope such as task family, risk, subsystem, stage, and other qualification boundaries.

### D-005: evidence before autonomy

Every Capability and Decision should remain traceable to supporting Evidence.

### D-006: observe before enforce

The graph should initially improve reporting, inspection, and requalification analysis. It should not introduce enforcement behavior.

### D-008: reuse community infrastructure

Execution, provenance, telemetry, policy, and attestations should still come from Harbor, CodeProbe, CI systems, OpenTelemetry, SLSA/in-toto/Sigstore, GitHub, or other community infrastructure where appropriate.

## Core hypothesis

A durable assurance system will need to treat qualification as **continuously accumulated and selectively invalidated evidence**, rather than as a static score attached to an agent.

Put differently:

```text
configuration identity
        +
evaluation evidence
        +
provenance
        +
capability qualification
        +
configuration/environment changes
        +
runtime outcomes
        =
persistent assurance state
```

This may be the mechanism that turns "earned autonomy" from a benchmark report into an operationally useful trust model.

## Key design problem: evidence validity and decay

The most important problem is not storing more history. It is determining when old evidence still applies.

Suppose a configuration has demonstrated strong capability, then one component changes:

```text
model                 unchanged
harness               unchanged
instructions          v3 → v4
tools                 unchanged
permissions           unchanged
environment           unchanged
```

Should all prior capability disappear?

Probably not.

Should it be inherited automatically?

Also probably not.

The assurance layer may eventually need rules or evidence about how much qualification survives a configuration change.

Examples:

- patch-level CLI version change may require little or no requalification;
- material harness control-flow change may invalidate a large portion of prior evidence;
- adding a tool may expand capability but introduce new failure modes;
- changing permissions may alter risk without altering raw task success;
- verifier changes may invalidate prior conclusions without changing the agent at all;
- repository/environment changes may make evidence stale even when the agent configuration is identical.

The graph model could make these dependencies explicit enough that validity can be recomputed instead of manually reasoned about.

## Configuration identity

The current project already treats the full configuration as the qualification subject. This issue should explore whether configuration identity needs to become more structured.

A configuration fingerprint might derive from components such as:

```text
agent/harness + version
model identifier/version
system/repository instructions digest
tool inventory + versions
retrieval/context strategy
network/permission limits
sandbox/runtime image
evaluator/verifier configuration
```

Questions:

- Which components belong in the identity versus merely in Evidence provenance?
- Which fields are stable enough to fingerprint deterministically?
- Can two configurations express a "derived from" relationship?
- Should component-level changes be classified as material/non-material, or should that be learned empirically?
- Can external runtimes produce this identity without adopting Agent Assurance internally?

Avoid inventing a universal agent identity standard unless required. Prefer a portable, provider-neutral configuration descriptor or digest that adapters can populate.

## Evidence lineage

A useful graph should let us traverse from a Decision all the way back to observed facts.

Conceptually:

```text
Decision
  ↓ based_on
Capability
  ↓ supported_by
Evidence[]
  ↓ produced_from
Task + configuration + execution environment
  ↓ verified_by
CI/tests/static analysis/security checks/etc.
```

This is especially important when evidence changes status later.

Example:

```text
Verifier V17 later found invalid
        ↓
Evidence E22 and E24 become suspect
        ↓
Capability C7 confidence decreases
        ↓
Decision D18 should no longer be interpreted with the same assurance
```

The system should ideally be able to identify that dependency chain without rewriting historical records.

## Evidence should remain append-oriented

Historical Evidence should not be silently mutated to match current beliefs.

Prefer a model where new facts annotate, supersede, invalidate, or reduce the confidence of earlier evidence while retaining provenance.

This supports auditability and makes qualification evolution inspectable.

## Runtime outcomes as future qualification evidence

The current conceptual loop already includes runtime evidence / production outcomes feeding future qualification.

The evidence graph gives this idea a clearer structure.

For example:

```text
historical replay evidence
          +
CI execution evidence
          +
production/runtime outcome
          +
human review outcome
          ↓
updated capability state
```

The challenge is not to let production frequency swamp controlled evidence. A thousand trivial successful changes should not automatically outweigh a small number of severe failures.

Future work may need evidence weighting by:

- task/risk scope;
- verifier strength;
- independence of observations;
- recency;
- severity;
- configuration similarity;
- environment similarity.

Do not implement a sophisticated weighting model before real data requires it.

## Relationship to provenance standards

Agent Assurance should not invent signing or supply-chain provenance infrastructure.

Where useful, explore whether graph edges or Evidence references can point to existing provenance objects from:

- SLSA;
- in-toto;
- Sigstore;
- GitHub artifact attestations;
- CI run identifiers;
- OpenTelemetry trace/span identifiers.

The assurance layer should add semantics such as "this evidence supports this capability" rather than replacing underlying attestation systems.

## Relationship to harness engineering

Recent harness-engineering work reinforces why configuration-level qualification matters.

For a fixed base model, changes in:

- context assembly;
- tools;
- REPL/execution environment;
- memory;
- sub-agents;
- control loops;
- self-improvement logic;

can materially alter observed capability.

As harnesses become adaptive or self-modifying, a static model identifier becomes even less meaningful as a qualification subject.

This creates a longer-term question:

> What exactly was evaluated if the harness itself changed during or between runs?

The evidence graph should be capable of representing configuration lineage and provenance without requiring Agent Assurance to own the harness.

## Relationship to control graphs

Do not confuse this proposal with agent orchestration graphs.

A control graph answers:

```text
Which agent/task executes next?
```

An assurance evidence graph answers:

```text
What relationship exists between tasks, configurations, evidence, capabilities, decisions, and outcomes?
```

Agent Assurance should only own the latter semantics.

## Potential queries this model should eventually support

These are useful acceptance tests for the domain model even before any graph query engine exists.

### Qualification lookup

> What has configuration X demonstrated for backend bug fixes at medium risk?

### Evidence lineage

> Which Evidence records support Capability C, and which deterministic verifiers produced them?

### Decision explanation

> Why was configuration X allowed to implement task T but not merge it?

### Drift impact

> Configuration X changed from harness version 1.2 to 1.3. Which existing Capability records remain potentially applicable and which require requalification?

### Failure clustering

> Which configurations experienced the same failure category on authentication-related tasks?

### Verifier invalidation

> Which Capability and Decision records depend on verifier V whose test contract has been found defective?

### Evidence freshness

> Which qualifications rely entirely on evidence older than the current environment/repository baseline?

### Cross-configuration transfer

> Configuration B differs from qualified configuration A only in one component. What evidence is shared, transferable, or missing?

These queries should guide semantics before storage technology.

## What not to build

This issue must not become justification for:

- a graph database platform;
- agent orchestration;
- workflow execution;
- a proprietary telemetry backend;
- another policy engine;
- an agent memory system;
- a model router;
- a general identity provider;
- a visualization/dashboard project;
- a broad digital-twin representation of software engineering activity.

Stay focused on assurance semantics.

## Suggested staged exploration

### Stage 0: inspect current records

Using the completed Click replay data, construct the conceptual relationship graph without changing schemas.

Answer:

- Which nodes/relationships can already be derived?
- Which relationships currently depend on convention or implicit knowledge?
- Which queries above cannot be answered reliably?

Produce a short design note, not implementation.

### Stage 1: identify minimum linkage gaps

Only after Stage 0, identify the smallest schema changes necessary to make lineage explicit.

Candidate areas to inspect, not pre-approved changes:

- stable configuration reference/fingerprint;
- Evidence → configuration linkage;
- Evidence → verifier/provenance references;
- Capability → supporting Evidence references;
- Capability validity/freshness metadata;
- Decision → Capability/Evidence lineage;
- supersedes/invalidates/derived-from relationships.

Respect D-002. Prefer references/fields over new primitives.

### Stage 2: derive an assurance graph view

Implement a read-only derived view/index over existing assurance documents.

For example, a small CLI command could eventually answer lineage questions without changing the canonical storage model.

Possible shape only after semantics are proven:

```bash
aa explain decision <id>
aa lineage capability <id>
aa impact --config-change old.json new.json
```

Do not implement these commands merely because they sound useful. First prove that the existing experiment data supports meaningful answers.

### Stage 3: test configuration drift

Use an actual controlled configuration change from the existing experiments.

Examples already present in the project include Codex CLI version drift and reasoning-effort variants.

Test whether the model can correctly keep evidence separated while still expressing useful relationships between configurations.

This should be the first real experiment for evidence transfer/decay semantics.

### Stage 4: runtime feedback

Only after the offline model is sound, ingest one real downstream outcome type and evaluate whether it improves qualification meaningfully.

Avoid building a telemetry collection platform. Consume an existing record or fixture.

## Codex task

When this issue is picked up, do **not** immediately implement a graph store or change schemas.

Start by reading, in order:

1. `AGENTS.md`
2. `CODEX_START_HERE.md`
3. `docs/DESIGN_PRINCIPLES.md`
4. `docs/DECISIONS.md`
5. `docs/COMMUNITY_REUSE.md`
6. `docs/EXPERIMENT_PLAN.md`
7. `docs/ROADMAP.md`
8. current schemas and the real generated Task/Evidence/Capability/Decision examples

Then perform Stage 0 only.

### Expected first deliverable

Create a design note such as:

`docs/EVIDENCE_GRAPH_EXPLORATION.md`

It should contain:

1. the graph that can already be reconstructed from current records;
2. concrete examples using real Click replay artifacts;
3. five to ten important queries and whether they are currently answerable;
4. exact linkage gaps in the current schemas;
5. whether the four-primitives model remains sufficient;
6. a minimal proposal for the next experiment around configuration drift;
7. community standards/projects that may already solve part of the provenance or identity problem;
8. explicit reasons **not** to introduce a graph database or new primitive yet.

Do not modify schemas in the first pass unless an existing record is objectively malformed or inconsistent.

## Success criteria for this exploration

This issue is valuable if it helps answer these questions:

1. Can Agent Assurance represent qualification as accumulated evidence without becoming an orchestration/runtime platform?
2. Can every Capability and Decision be traced to concrete Evidence and configuration identity?
3. Can configuration drift be represented without either blindly inheriting or completely discarding prior evidence?
4. Can invalid/verifier-stale evidence propagate into understandable qualification impact?
5. Can the four existing primitives remain the core semantic model?
6. Can community provenance/attestation infrastructure handle the low-level integrity layer while Agent Assurance owns only assurance relationships?
7. Does this make autonomy decisions more defensible to engineers?

## Kill / narrowing criteria

Do not pursue this direction if the first exploration shows that:

- current records already provide all useful lineage with trivial joins and no semantic gap;
- graph terminology adds conceptual complexity without improving decisions;
- an existing open standard already provides the assurance semantics we need;
- configuration similarity/decay is too arbitrary to produce defensible guidance;
- users do not need historical lineage to make autonomy decisions;
- implementing the model would pull the project into observability, runtime control, or orchestration.

## Source / motivation

The immediate trigger for this exploration was a discussion around persistent graphs in agent systems, including the distinction between temporary agent outputs and durable relationship state:

https://x.com/polydao/status/2096128417108287566?s=20

Treat that post as inspiration, not authority. The durable rationale for this issue comes from problems already visible in Agent Assurance itself: configuration drift, qualification validity, evidence provenance, and continuous requalification.
