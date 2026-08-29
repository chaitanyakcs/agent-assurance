# Pre-RFC Roadmap

The first milestone is evidence, not architecture.

## M0 — Prove the objects

- [x] Define Task, Evidence, Capability, and Decision v0 schemas.
- [x] Provide valid minimal examples.
- [x] Provide a CLI that validates assurance documents.
- [ ] Test the schemas against 10–15 historical tasks from one public OSS repository.
- [ ] Identify where the four-object model breaks down before adding new primitives.

## M1 — Historical replay spike

- [ ] Select a public repository with good merged-PR history and deterministic tests.
- [ ] Reconstruct the repository at the pre-change commit for each task.
- [ ] Create task classifications and deterministic evaluation contracts.
- [ ] Execute at least two agent configurations using an existing runner such as Harbor.
- [ ] Emit Evidence records for each trial.
- [ ] Aggregate Evidence into Capability records.
- [ ] Verify that experienced engineers consider the resulting capability statements defensible.

## M2 — One autonomy decision

- [ ] Classify one incoming task.
- [ ] Match it against demonstrated capability.
- [ ] Combine risk, qualification, and current CI evidence.
- [ ] Emit a Decision record such as `assist`, `implement`, `open_pr`, or `merge`.
- [ ] Keep enforcement advisory-only initially.

## M3 — Community validation

Before an RFC, show the prototype to maintainers/users of adjacent systems and engineering teams deploying coding agents.

Questions:

1. Would you consume a portable capability record?
2. Would your benchmark/runtime emit this evidence format?
3. Which fields are impossible or misleading in practice?
4. What existing standard are we duplicating?
5. What would prevent adoption without replacing the current SDLC?

## Explicit kill criteria

Stop, merge upstream, or narrow the project if:

- an established community standard covers the same capability-to-autonomy semantics;
- capability records cannot be made defensible across real tasks;
- task classification requires so much organization-specific configuration that portability disappears;
- engineering teams value benchmark reports but do not use them to inform autonomy decisions.
