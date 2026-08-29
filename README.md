# Agent Assurance

**Agents earn autonomy through demonstrated capability and verifiable evidence.**

Agent Assurance is an early, vendor-neutral specification and reference implementation for deciding what software-engineering agents should be trusted to do in a particular engineering environment.

It does **not** try to be another coding agent, model router, sandbox, SDLC workflow, or policy engine. It is designed to sit above existing tools such as Claude Code, Codex, Gemini, Spec Kit, Harbor, CI systems, OpenTelemetry, SLSA/Sigstore, and OPA.

## The four v0 objects

1. **Task** — what engineering work is being attempted, including stage, family, and risk.
2. **Evidence** — what happened when an executor attempted the task and how the result was verified.
3. **Capability** — what an agent configuration has demonstrated across a class of tasks.
4. **Decision** — what autonomy is permitted for an incoming task given capability, risk, and required evidence.

The initial loop is:

```text
historical tasks ──> evidence ──> capability
                                  │
new task ─────────────────────────┼──> decision ──> allowed autonomy
                                  │
runtime evidence ─────────────────┘
```

## Why this exists

Model leaderboards answer whether a model performs well on a general benchmark. Engineering organizations need a different answer:

> Given this model + agent harness + instructions + tools + context, what may it safely do in this repository and task class?

Agent Assurance aims to make that answer empirical, portable, and provider-neutral.

## Non-goals

Agent Assurance v0 will not build:

- an agent runtime or coding assistant;
- a model gateway or router;
- a sandbox/container platform;
- a replacement for Spec Kit or existing SDLC workflows;
- a new policy language;
- an observability backend;
- a dashboard.

Where possible, the project will integrate with community infrastructure instead.

## Quick start

Requirements: Python 3.11+

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'

aa init
aa validate task examples/minimal/task.yaml
aa validate evidence examples/minimal/evidence.yaml
aa validate capability examples/minimal/capability.yaml
aa validate decision examples/minimal/decision.yaml
```

`aa init` creates a local `.agent-assurance/` directory with a minimal config and policy example. It does not change your existing development workflow.

## Example capability

```yaml
apiVersion: assurance.agent/v0
kind: Capability
subject:
  agent: codex
  configuration: company-default-v3
scope:
  stage: implementation
  task_family: bugfix
  risk_domain: payments
evaluation:
  attempted: 42
  successful: 38
  independent_trials: 3
qualification:
  level: L3
  confidence: high
  status: valid
```

A runtime or CI policy can consume this capability record without needing to know how the evidence was produced.

## Planned integrations

The project should **reuse rather than replace**:

| Concern | Intended reuse |
|---|---|
| Multi-agent eval execution | Harbor |
| Agent execution | Claude Code, Codex, Gemini, OpenHands, others |
| Spec / plan generation | Existing SDLC, Spec Kit, OpenSpec |
| Tool access | MCP |
| Verification | Existing tests, linters, static analysis, security tooling |
| Policy | OPA or existing CI policy |
| Enforcement | GitHub Actions / CI initially |
| Telemetry | OpenTelemetry |
| Provenance / attestations | SLSA, in-toto, Sigstore / GitHub attestations |

Integrations are optional. The schemas are the interoperability boundary.

## Project context for coding agents

If you are continuing this project with Codex or another coding agent, start with [CODEX_START_HERE.md](CODEX_START_HERE.md). The durable design context is intentionally stored in-repo rather than in a chat transcript.

Key supporting docs:

- [Design principles](docs/DESIGN_PRINCIPLES.md)
- [Decision log](docs/DECISIONS.md)
- [Community reuse / landscape](docs/COMMUNITY_REUSE.md)
- [First historical replay experiment](docs/EXPERIMENT_PLAN.md)
- [Pre-RFC roadmap](docs/ROADMAP.md)

## Project status

**Pre-RFC / experimental.** The goal of v0 is to validate the primitives against real historical engineering tasks before stabilizing a protocol.

See [docs/ROADMAP.md](docs/ROADMAP.md) for the first experiment.

## Contributing

This project is intentionally small while the abstraction is being validated. The most useful early contributions are:

- historical engineering-task replay experiments;
- examples from different languages/repositories;
- feedback on the four schemas;
- adapters that emit evidence from existing tools;
- critiques of the capability-to-autonomy model.

## License

Apache-2.0. See [LICENSE](LICENSE).
