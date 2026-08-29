# Agent Instructions

This repository is pre-RFC and intentionally minimal.

## Core constraint

Do not add an agent runtime, model router, sandbox, policy engine, dashboard, or proprietary observability system unless an accepted design decision explicitly changes the project scope.

The project currently owns only four assurance primitives:

- Task
- Evidence
- Capability
- Decision

Prefer adapters to existing community systems over replacement implementations.

## Change quality

- Keep schemas provider-neutral.
- Treat a complete agent configuration, not a model brand, as the capability subject.
- Prefer deterministic verification evidence over model self-assessment.
- Preserve human executors as valid participants.
- Add new schema fields only when a real experiment requires them.

## Required context before substantive work

Read these in order before making architectural or scope changes:

1. `CODEX_START_HERE.md`
2. `docs/DESIGN_PRINCIPLES.md`
3. `docs/DECISIONS.md`
4. `docs/COMMUNITY_REUSE.md`
5. `docs/EXPERIMENT_PLAN.md`
6. `docs/ROADMAP.md`

Do not use a shared-chat transcript as the project's source of truth. If new discussion changes a durable decision, update the repository documentation and decision log.

## Current priority

The current milestone is the first historical replay experiment. Prefer learning from real replayed tasks over adding framework abstractions. Do not write a formal RFC until the experiment has produced at least one defensible Capability and one advisory Decision.
