# Click Mini-Suite Capability Profiles

These Capability records summarize the first four replayable Click implementation
tasks: #3013, #3152, #3004, and #3079.

Important caveats that the v0 Capability schema does not yet represent
structurally:

- sample size is very small;
- all tasks come from one repository and one ecosystem;
- Harbor local Docker used the public-network baseline because local network
  isolation was not enforceable;
- historical replay tests may overestimate current-task capability;
- low-reasoning timeout evidence is represented as an aborted Evidence outcome,
  not as a verifier failure.

The held-out #2930 trial ran under `harbor/codex@0.153.4/gpt-5.5`, not the
`0.152.1` configuration named by the advisory Decision. Its result therefore
started a separate Capability record. A subsequent run of the four-task mini-
suite passed all four tasks under the same `0.153.4` configuration, bringing
that record to five successful completed trials. The configuration drift is
material because the agent version is part of the configuration identity and
changes its digest; it does not extend or update the `0.152.1` profile.

One #3004 attempt aborted during agent setup because npm did not install the
platform-specific Codex binary. Agent execution and verification never started,
so the separate aborted Evidence record is classified as infrastructure and is
excluded from the Capability's attempted and successful trial counts. The retry
completed and passed.

No schema change was required for this first profile.
