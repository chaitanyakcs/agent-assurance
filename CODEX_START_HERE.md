# Codex: Start Here

This repository is the result of a design exploration around agentic software development. The important context is **not** the original chat transcript; the durable decisions are captured in this repository.

## Mission

> Build a vendor-neutral engineering assurance layer that lets software agents **earn autonomy through demonstrated capability and verifiable evidence**.

The project is deliberately **not** another coding agent, model router, agent orchestrator, SDLC workflow engine, sandbox, policy engine, or observability platform.

The core question is:

> Given a specific **agent configuration** (model + harness + instructions + tools + context), what engineering work has it demonstrated it can perform in this environment, with what confidence, and what autonomy should policy allow for an incoming task?

The conceptual loop is:

```text
historical engineering work
        ↓
controlled replay / evaluation
        ↓
Evidence
        ↓
Capability
        ↓
new Task + risk
        ↓
Decision
        ↓
allowed autonomy
        ↓
runtime evidence / production outcomes
        └──────────────→ future qualification
```

A shorter mental model:

> **Can it? → May it? → Did it prove it?**

- **Can it?** — historical/full-SDLC capability evaluation.
- **May it?** — capability + risk + qualification → autonomy decision.
- **Did it prove it?** — deterministic/runtime evidence and provenance.

## The four v0 objects

The repository currently owns exactly four assurance primitives:

1. **Task** — what engineering work is being attempted, including stage/family/risk.
2. **Evidence** — what happened during an attempt and how it was verified.
3. **Capability** — what an agent configuration has demonstrated across a task class.
4. **Decision** — what autonomy is permitted for an incoming task given capability, risk, qualification, and required evidence.

Do not add a fifth primitive until a real experiment proves it is necessary.

## Crucial design decisions

### Capability belongs to an agent configuration, not a model name

These are different qualification subjects:

```text
Codex + model version A + repo instructions v3 + tools X/Y + retrieval Z
Codex + model version B + repo instructions v3 + tools X/Y + retrieval Z
Claude Code + model C + CLAUDE.md v5 + MCP tools
```

A model/harness/tool/instruction change may invalidate prior qualification. Do not let a model brand inherit autonomy blindly.

### Autonomy is task- and risk-specific

A high score on routine bug fixes does not imply authority for:

- authorization or tenant-isolation changes;
- database migrations;
- security-sensitive code;
- high-blast-radius cross-service work;
- deployment/production remediation.

The output we want is a capability profile, not a global leaderboard.

### Deterministic evidence outranks agent self-assessment

Prefer:

- existing test suites;
- new held-out tests;
- type checks / compilers;
- linters;
- static/security analysis;
- integration/API/browser checks;
- independently observed repository/CI facts.

LLM rubric judging may supplement these, but an agent saying "all tests pass" is not evidence by itself.

### Humans are valid executors

The assurance data model should work for human, agent, or hybrid execution. This lets organizations compare agent outcomes against human baselines where useful.

### Observe before enforce

Adoption levels should be:

1. **Observe** — evaluate historical work; change no workflow.
2. **Advise** — emit an autonomy recommendation in CI/PRs.
3. **Enforce** — block/permit actions only when teams choose to adopt enforcement.

## Why this project exists

The exploration started from Anthropic's 2026 AI-Native SDLC Playbook. Its useful insight is that SDLC stages become an artifact/evidence loop with humans concentrating at gates rather than manually doing every handoff.

However, a multi-provider organization should not encode the SDLC around Claude-specific constructs. We initially considered an open provider-neutral SDLC framework, then found that this layer is rapidly becoming crowded:

- GitHub Spec Kit is an agent-neutral, extensible SDLC/process harness with many coding-agent integrations.
- OpenAI Symphony specifies task-board-driven coding-agent orchestration.
- Agentplane, Nexus Agents, and similar projects address coding-agent control planes, approvals, evidence, and governance.

So this repository intentionally moved **above** those systems.

The remaining opportunity is the bridge:

```text
offline/private evidence                    runtime autonomy

historical tasks                            incoming task
      ↓                                          ↓
controlled eval                             classify risk
      ↓                                          ↓
capability evidence  ─────────────────→ qualification lookup
                                                 ↓
                                          autonomy decision
                                                 ↓
                                         execution evidence
                                                 ↓
                                           future re-eval
```

The thesis is not "we orchestrate agents." It is:

> **Agents earn engineering autonomy from demonstrated capability.**

## Community infrastructure we should reuse

Do not replace these unless a concrete experiment proves an incompatibility:

| Concern | Reuse / integrate |
|---|---|
| SDLC/spec workflows | GitHub Spec Kit, OpenSpec, existing company processes |
| Agent execution | Codex, Claude Code, Gemini CLI, OpenHands, others |
| Multi-agent eval execution | Harbor |
| Historical PR task mining | Learn from / interoperate with CodeProbe and AIBench Arena rather than duplicating blindly |
| Tool access | MCP |
| Verification | Existing CI/test/security tools |
| Policy engine | OPA optionally; simple local policy for small users |
| CI enforcement | GitHub Actions first; other CI later |
| Telemetry | OpenTelemetry |
| Provenance/attestations | SLSA / in-toto / Sigstore / GitHub artifact attestations |
| Sandboxes | Harbor/Docker/cloud sandboxes |
| Model routing | Existing routers/provider tools |

The schemas/semantics should be the interoperability boundary.

## Important adjacent projects

Before designing new infrastructure, inspect the current state of these projects. They may move quickly.

- Anthropic AI-Native SDLC Playbook: https://claude.com/blog/the-ai-native-sdlc-playbook
- GitHub Spec Kit: https://github.com/github/spec-kit and https://github.github.com/spec-kit/
- Harbor: https://github.com/harbor-framework/harbor
- OpenAI Symphony: https://openai.com/index/open-source-codex-orchestration-symphony/
- Agentplane: https://agentplane.org/
- Nexus Agents: https://github.com/nexus-substrate/nexus-agents
- AIBench Arena: https://github.com/Elnino0009/aibench-arena
- CodeProbe: https://github.com/sjarmak/codeprobe
- AgentGovBench: https://github.com/agentic-control-plane/agentgovbench

The existence of these projects is a reason to stay thin, not a reason to recreate their features.

## Where we believe the whitespace is

Crowded / high supersession risk:

- generic coding-agent orchestration;
- provider-neutral SDLC workflows;
- sandboxes;
- model routing;
- generic coding benchmarks;
- generic policy engines;
- agent observability.

More open / worth testing:

- full-SDLC capability evaluation (not only implementation);
- risk-specific capability profiles;
- historical + production continuous qualification;
- capability → autonomy policy;
- portable capability/evidence attestations;
- qualification invalidation when model/harness/context changes.

A larger vendor, especially GitHub, could eventually subsume much of this. Therefore this is intentionally a small, standards-oriented OSS bet with explicit kill/merge-upstream criteria.

## What SDLCBench means here

`SDLCBench` is a module/concept, not necessarily the umbrella project name.

Its job is to answer **Can it?** by turning historical engineering work into repeatable tasks and evidence. The initial concept was roughly 30 historical tasks across categories such as:

- routine bug fixes;
- complex/debugging bugs;
- feature implementation;
- cross-component/integration work;
- refactoring/tech debt;
- security/permissions;
- review;
- incident diagnosis.

The eval should not compare generated code line-by-line with the historical human patch. It should verify an **engineering contract**: acceptance behavior, regression tests, constraints, safety, and optional human/rubric review.

We later discovered AIBench Arena and CodeProbe already mine repository history for coding-agent evals. Therefore reuse/interoperate where possible. Our distinctive aim is to turn evidence into **portable capability and autonomy decisions**, and eventually broaden evaluation across the SDLC (spec, plan, implementation, review, incident response).

## The target adoption experience

The project should never require a company to "adopt our SDLC."

An eventual user journey should feel approximately like:

```bash
pip install agent-assurance

aa init

aa discover --history 30

aa eval --agent codex --agent claude-code --sample 10

aa report
```

Conceptual output:

```text
Agent capability report

                         Claude   Codex
Routine bugfix              L3      L3
Feature implementation      L3      L2
Refactoring                 L2      L3
Security                    L1      L1

Recommendation for current task:
  implement       ALLOW
  open PR         ALLOW
  merge           REQUIRE HUMAN

Reason:
  task class            backend.bugfix
  risk                  medium
  required capability   L3
  demonstrated          L3 / high confidence
  mandatory evidence    passed
```

This output is the product hypothesis we need to validate.

## Immediate task for Codex

**Do not write the RFC yet. Do not build an orchestration platform.**

Continue the Pre-RFC Roadmap with the smallest experiment that can falsify the design:

1. Review `README.md`, `AGENTS.md`, `docs/DESIGN_PRINCIPLES.md`, `docs/ROADMAP.md`, and the four schemas.
2. Inspect CodeProbe, AIBench Arena, and Harbor closely enough to propose the smallest reuse strategy for historical replay. Avoid duplicating repository mining or sandbox execution if an adapter is sufficient.
3. Select one public OSS repository with 10–15 high-quality historical changes and deterministic tests.
4. Design the replay experiment and record any schema deficiencies **before changing schemas**.
5. Implement only enough tooling/adapters to emit valid `Task` and `Evidence` records from the first few replayed tasks.
6. Aggregate evidence into a first `Capability` record.
7. Demonstrate one advisory `Decision` record.
8. Update the decision log when a material design choice is made.

Success is not "lots of code." Success is proving or disproving this statement:

> We can produce a defensible, portable statement about what a particular software-agent configuration has demonstrated it can do, and use that statement to make a sensible autonomy recommendation for a new engineering task.

## Stop conditions

Do not silently expand scope. Stop and document the finding if:

- an established project already provides the exact semantic object we were about to invent;
- the four-object model cannot represent a real experiment without major contortions;
- task classification is too subjective to support meaningful policy;
- the historical replay cannot produce defensible evidence;
- capability scores do not sensibly translate into task-specific autonomy guidance.

Those are valuable outcomes for the pre-RFC phase.
