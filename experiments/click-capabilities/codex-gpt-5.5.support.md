# Codex 0.152.1 Default Capability Support

This sidecar records the exact support set for
`experiments/click-capabilities/codex-gpt-5.5.yaml`. It is an experiment
manifest, not a fifth Agent Assurance primitive or a v0 schema extension.

Configuration digest:
`sha256:3810c2f1b478418758d7588c996eebab8977c38d8adb19c39d65f9685d2ee183`

## Included Evidence

| Evidence ID | Task | Result |
| --- | --- | --- |
| `evidence-click-pr-3152-codex-gpt-5-5-20260902` | `click-pr-3152` | success, verifier pass |
| `evidence-click-pr-3004-codex-gpt-5-5-20260902` | `click-pr-3004` | success, verifier pass |
| `evidence-click-pr-3079-codex-gpt-5-5-20260902` | `click-pr-3079` | success, verifier pass |

The reconstructed aggregate is 3 attempted, 3 successful, and 3 independent
trials. All included records contain the exact configuration digest above.

## Excluded Evidence

`evidence-click-pr-3013-codex-gpt-5-5-20260830` is excluded. It identifies
`harbor/codex@0.151.0/gpt-5.5` and does not contain a configuration digest, so
it cannot support a Capability for Codex 0.152.1. The Evidence remains
unchanged as a historical observation.

`evidence-click-pr-2930-codex-gpt-5-5-20260906` is excluded because its
configuration digest identifies Codex 0.153.4. It is follow-up Evidence for a
different configuration, not confirmation of this Capability.

## Correction

The Capability previously reported 4/4 by including #3013 based on filename
and suite convention. On 2026-09-09 it was corrected to 3/3 after exact lineage
reconstruction exposed the version mismatch. No Evidence was modified.
