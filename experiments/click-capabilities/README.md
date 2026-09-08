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
suite passed all four tasks under the same `0.153.4` configuration. Two more
bugfix replays, #2940 and #2935, bring that bugfix record to seven successful
completed trials. The configuration drift is
material because the agent version is part of the configuration identity and
changes its digest; it does not extend or update the `0.152.1` profile.

The same configuration also passed one feature task (#3058), one typing task
(#2630), and one refactor task (#3023). These are separate L0 profiles with
insufficient evidence after one trial each; they are not folded into the
bugfix qualification.

One #3004 attempt aborted during agent setup because npm did not install the
platform-specific Codex binary. Agent execution and verification never started,
so the separate aborted Evidence record is classified as infrastructure and is
excluded from the Capability's attempted and successful trial counts. The retry
completed and passed.

This second batch also produced two excluded infrastructure records: #2940's
initial hidden-test collision after agent execution, and #2630's agent setup
timeout before execution. Both retries completed and passed.

No schema change was required for this first profile.
