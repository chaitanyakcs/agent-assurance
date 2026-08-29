# Community Reuse and Competitive Landscape

**Purpose:** keep Agent Assurance thin and avoid rebuilding fast-moving community infrastructure.

**Last reviewed:** 2026-08-30

This is not an exhaustive market map. It captures projects materially relevant to current design decisions. Re-check before major implementation because this space changes rapidly.

## Reuse map

| Concern | Default approach | Agent Assurance responsibility |
|---|---|---|
| Spec/plan/process workflow | GitHub Spec Kit, OpenSpec, existing SDLC | Consume metadata/artifacts only when useful |
| Coding-agent execution | Codex, Claude Code, Gemini CLI, OpenHands, etc. | Describe the evaluated configuration |
| Multi-agent eval execution / isolation | Harbor | Adapter + assurance record emission |
| Historical task mining | CodeProbe / AIBench Arena where suitable | Normalize task/evidence; extend beyond implementation over time |
| Tool access | MCP | No replacement protocol |
| Tests/lint/security | Existing repo/CI tooling | Normalize outcomes into Evidence |
| Policy | OPA optional, CI logic for small deployments | Decision input/output semantics |
| CI enforcement | GitHub Actions first | Advisory decision action initially |
| Telemetry | OpenTelemetry | Define assurance-specific attributes only if needed |
| Provenance | SLSA / in-toto / Sigstore / GitHub attestations | Explore an agent-capability/evidence predicate, do not invent signing |
| Model routing | Existing routers/provider tools | Capability can be one input to routing; no router implementation |
| Agent control plane | Agentplane / Nexus / vendor tooling | Portable records those systems could eventually consume |

## Adjacent projects

### Anthropic AI-Native SDLC Playbook

https://claude.com/blog/the-ai-native-sdlc-playbook

Useful insight: as agentic coding accelerates implementation, planning, review, test, deployment, and maintenance become the next bottlenecks. Anthropic proposes version-controlled artifacts and automated handoffs with human attention concentrated at gates.

Agent Assurance takes the control/evidence insight but does not assume Claude is the execution layer.

### GitHub Spec Kit

https://github.com/github/spec-kit
https://github.github.com/spec-kit/

As of this review, Spec Kit is an extensible, intent-driven process/SDLC harness and supports many coding-agent integrations. It also has agent-native runtime event adapters.

**Implication:** do not build a provider-neutral spec/plan workflow engine. Integrate if needed.

### OpenAI Symphony

https://openai.com/index/open-source-codex-orchestration-symphony/

A specification/reference approach for continuously assigning issue-tracker tasks to coding agents in isolated workspaces.

**Implication:** generic task-to-agent orchestration is not our whitespace.

### Harbor

https://github.com/harbor-framework/harbor

Evaluation infrastructure supporting multiple pre-integrated coding agents including Claude Code, Codex CLI, Gemini CLI, OpenHands, and others, with custom agent integration.

**Implication:** likely execution substrate for early multi-agent replay experiments; avoid building sandboxes/runners.

### Agentplane

https://agentplane.org/

Git-native control plane for coding agents, focusing on bounded authority, approvals, observed proof, verification, recovery, and Agent Change Records.

**Implication:** runtime control/evidence is becoming crowded. Portable assurance records should complement rather than replace control planes.

### Nexus Agents

https://github.com/nexus-substrate/nexus-agents

Coding-agent governance/control plane with adversarial review, audit, closed-loop outcome-based routing, and an authority model that includes earned promotion.

**Implication:** "earned autonomy" is not unique wording/concept. Our differentiation must be rigorous qualification from task-specific historical evidence into portable capability semantics, not simply an authority ladder.

### AIBench Arena

https://github.com/Elnino0009/aibench-arena

Turns a repository's own git history into a private benchmark and runs multiple coding agents against historical tasks.

**Implication:** do not position SDLCBench merely as "your private SWE-bench." Historical mining for coding tasks already exists.

### CodeProbe

https://github.com/sjarmak/codeprobe

Mines merged PRs/commits, reconstructs pre-change state, generates verification contracts, runs agent configurations, and records quality/cost/latency/failure outcomes.

**Implication:** this is especially close to our historical implementation-eval mechanics. Prefer consuming/extending its outputs or adapting it rather than reimplementing mining from scratch.

### AgentGovBench

https://github.com/agentic-control-plane/agentgovbench

Vendor-neutral governance benchmark covering identity, policy enforcement, and observability across agent runtimes.

**Implication:** governance benchmark suites may become producers of assurance evidence. Keep our Evidence/Capability concepts general enough that external benchmark systems could emit them.

## Supersession risk

High risk of being commoditized/superseded:

- provider-neutral SDLC/process harnesses;
- coding-agent orchestration/control planes;
- sandboxes/runners;
- generic model routing;
- agent observability;
- generic historical coding benchmarks.

More defensible as an open semantic layer, if validated:

- task/risk-scoped capability records;
- qualification confidence/validity tied to agent configuration;
- capability-to-autonomy decisions;
- continuous requalification after configuration or production outcome changes;
- portable evidence/capability attestations;
- evaluation that expands across full SDLC stages rather than only code implementation.

## Strategic stance

This should remain a small option-value OSS bet, not a large platform build.

Success could include another ecosystem project adopting the semantics or the work being merged upstream into a larger standard. Being subsumed at the standards layer is not necessarily failure.
