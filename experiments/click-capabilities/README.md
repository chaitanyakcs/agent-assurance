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

No schema change was required for this first profile.
