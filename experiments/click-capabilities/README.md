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
produces a separate Capability record based only on that one successful trial.
The configuration drift is material because the agent version is part of the
configuration identity and changes its digest; it does not extend or update the
four-trial `0.152.1` profile.

No schema change was required for this first profile.
