# Evidence Graph Exploration

Date: 2026-09-09

## Scope

This Stage 0 note tests whether the current Click records can answer useful
lineage questions when viewed as a graph. It does not propose a graph database,
a fifth assurance primitive, or a schema change. The source of truth remains
the existing Task, Evidence, Capability, and Decision documents.

The exercise covers the ten Click Tasks, twenty-one Evidence records, six
Capability records, and one Decision committed after the historical replay
experiment.

## Conceptual graph

The four assurance primitives are the durable nodes. Several external or
derived identities are useful graph targets without becoming new primitives:

| Node | Source | Identity available today |
| --- | --- | --- |
| Task | Task record | `metadata.id` |
| Evidence | Evidence record | `metadata.id` |
| Capability | Capability record | file path plus subject, scope, and validity fields |
| Decision | Decision record | file path plus task and subject fields |
| Agent configuration | derived from Evidence/Capability/Decision | `configuration_digest` when present, otherwise a configuration name |
| Source revision | Task source | repository and revision |
| Execution trial | Harbor output | trial name/URI in Evidence notes |
| Verification artifact | Evidence verification | artifact path |

The relationships that can be derived are:

| Relationship | Status | Derivation |
| --- | --- | --- |
| Evidence `attempted` Task | explicit | `Evidence.task.id` equals `Task.metadata.id` |
| Evidence `was-produced-by` configuration | mostly explicit | executor configuration digest, or weaker configuration name |
| Task `replays` source revision | explicit | source repository and revision |
| Evidence `came-from` Harbor trial | implicit | parse `trial_name` or `trial_uri` from notes |
| Evidence `was-verified-by` artifact | explicit but weak | verification artifact path; no content digest or verifier identity |
| Capability `describes` configuration | explicit | subject configuration digest and name |
| Capability `aggregates` Evidence | implicit | manually select matching configuration, repository, stage, family, risk, and benchmark records |
| Decision `applies-to` Task | explicit | task ID |
| Decision `uses` configuration | explicit | subject configuration digest and name |
| Decision `relies-on` Capability | implicit | infer from subject, demonstrated level, scope, and prose |
| Decision `requires` runtime Evidence | semantic only | string labels, not references or predicates |

This is already a graph in the ordinary data-model sense. The problem is not
storage. It is that important edges are inferred from conventions, filenames,
and prose rather than recorded as stable references.

## Query test

The following queries were evaluated manually against the committed records.

| Query | Result | Finding |
| --- | --- | --- |
| What may Codex 0.153.4 do for low-risk Click bugfixes? | answerable | After excluding #3152's invalid verifier, the matching Capability reports 6/6 and L1 with low confidence. |
| Which Evidence records support that Capability? | partially answerable | Seven records can be inferred by exact digest and task scope, but the Capability does not identify its support set or exclusion rule. |
| Why did the Decision for Click #2930 permit implementation but not publication? | partially answerable | Permissions and prose explain the boundary; there is no direct Capability reference, and the held-out Evidence used a different configuration. |
| What changed between the 0.152.1 and 0.153.4 configurations? | not answerable | Different digests prove different identities, but records do not retain a canonical component manifest or a `derived-from` relation. |
| Did low reasoning change outcomes? | partially answerable | Separate configuration names/digests and 3/4 versus 4/4 results show a difference, but no structured relation identifies reasoning effort as the sole change. |
| Which qualifications depend on a verifier later found invalid? | not reliably answerable | Verification artifacts and details lack verifier identity/version/digest, and Capability-to-Evidence edges are implicit. |
| Which failures were infrastructure failures rather than agent failures? | partially answerable | Aborted Evidence and notes preserve the distinction for this experiment, but phase and exception class require text interpretation. |
| Is a qualification fresh for the current environment? | partially answerable | `valid_from` and Evidence timestamps exist; environment, harness, verifier, instructions, and expiry are incomplete. |
| What evidence supports security-sensitive autonomy? | answerable as absent | No current Task or Capability covers that risk; no extrapolation is justified. |
| Can the 0.152.1 default Capability's 4/4 support set be reconstructed exactly? | no | The expected #3013 record identifies Codex 0.151.0 and has no configuration digest. Only three exact 0.152.1 default records are committed. |

The final query exposes an integrity problem, not merely poor query ergonomics.
`experiments/click-capabilities/codex-gpt-5.5.yaml` claims four attempts for
digest `sha256:3810c2f1...`, while the corresponding #3013 Evidence names
`harbor/codex@0.151.0/gpt-5.5` and has no digest. This exploration does not
rewrite that historical record or weaken identity matching to make the claim
appear consistent. The Capability was first corrected to three exact-digest
trials, then to two after a no-op control invalidated #3152. Its support set and
exclusions are recorded in a sidecar manifest. A new pinned #3013 trial and a
repaired #3152 verifier would be required to rebuild that coverage.

## Minimum linkage gaps

The query failures suggest a small set of candidate links, but they do not yet
justify schema additions:

1. Capability needs a stable identity and an explicit list, query, or manifest
   for the Evidence included in its evaluation, including exclusions.
2. Decision needs a stable identity and an explicit reference to the Capability
   it relied on; runtime Evidence should be attachable without prose parsing.
3. Agent configuration needs a canonical, inspectable component manifest so a
   digest difference can be explained, not only detected.
4. Evidence needs structured execution and verification identities, including
   harness, trial, verifier, artifact digest, environment, and failure phase.
5. Invalidation or supersession needs to identify both the affected record and
   the event or changed component that caused it.

These are linkage and provenance properties of the existing four objects. A
configuration manifest, execution trial, verifier, or invalidation event can be
an external resource identified by URI and digest. None must become an Agent
Assurance primitive.

## Minimal configuration-drift experiment

Use the Click replay suite to test whether those candidate links are necessary
before changing a schema:

1. Select Codex 0.152.1 default as configuration A and Codex 0.153.4 default as
   configuration B.
2. Run the same four bugfix Tasks (#3013, #3152, #3004, and #3079) twice per
   configuration. Pin model, reasoning settings, instructions, skills, MCP
   servers, task checksum, container image, Harbor version, verifier digest,
   network policy, and budget; change only the Codex CLI version.
3. Store an external canonical configuration manifest for each run and digest
   it. Emit new append-only Evidence rather than editing the historical files.
4. Build each Capability from an explicit support manifest and record excluded
   infrastructure aborts separately from agent outcomes.
5. Evaluate three interpretations: no transfer, full invalidation, and an
   explicitly marked provisional transfer. Do not silently inherit Evidence
   across configuration digests.

The experiment succeeds if a reviewer can identify the changed component,
reconstruct every aggregate exactly, distinguish direct from transferred
support, and list every Capability and Decision affected by the drift. Until
then, a design-note manifest is sufficient; adding `derived_from`, evidence
references, or invalidation fields would be premature.

## Relevant provenance standards

Existing standards cover useful pieces and should be reused at integration
boundaries:

- [OpenTelemetry traces](https://opentelemetry.io/docs/concepts/signals/traces/)
  provide trace/span identities, parent-child structure, attributes, events,
  and links. They are suitable for correlating an agent execution and verifier
  activity, not for defining qualification or autonomy semantics.
- The [in-toto Statement v1](https://in-toto.io/Statement/v1) provides a typed
  attestation envelope with digest-addressed subjects and a predicate. An Agent
  Assurance record or support manifest could be carried as a predicate without
  replacing the four-object model.
- [SLSA provenance](https://slsa.dev/spec/v1.1/provenance) models artifact build
  provenance, including subjects, builders, inputs, and build metadata. Its
  digest and provenance practices are useful for configuration, verifier, and
  artifact identity, but software-build provenance is not agent capability.
- [Sigstore attestation verification](https://docs.sigstore.dev/cosign/verifying/attestation/)
  can provide signer identity and integrity for in-toto attestations. Signing a
  claim does not establish that its assurance method or conclusion is sound.

The compatibility direction should therefore be export, embed, reference, and
verify. Agent Assurance should not clone a telemetry backend, provenance
schema, signing service, or graph store.

## Four-primitives assessment

The four primitives remain sufficient:

- Task is the assurance subject for work and risk.
- Evidence records observations and verification.
- Capability aggregates Evidence for a scoped configuration.
- Decision applies a Capability and risk boundary to a Task.

Persistent evidence changes the lifetime and connectivity of these records,
not their meanings. Configuration, execution, verifier, source revision, and
artifact identities are provenance resources connected to the four objects.
Invalidation is a state transition or relationship, not a fifth business
object.

## Stage 0 conclusion

Do not add a graph database. Ten Tasks and a few dozen records are directly
queryable, and a database would not repair missing or ambiguous edges. Do not
add a new primitive: all tested questions concern provenance or references
among the existing four.

The next implementation decision should wait for the controlled drift
experiment. If it reproduces the query failures, the smallest likely change is
stable Capability and Decision identities plus explicit support/reliance
references, accompanied by externally digestible configuration and verifier
manifests. That is a hypothesis to test, not a v0 schema commitment.
