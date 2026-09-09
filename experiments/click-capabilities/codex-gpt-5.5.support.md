# Codex 0.152.1 Default Capability Support

This sidecar records the exact support set for
`experiments/click-capabilities/codex-gpt-5.5.yaml`. It is an experiment
manifest, not a fifth Agent Assurance primitive or a v0 schema extension.

Configuration digest:
`sha256:3810c2f1b478418758d7588c996eebab8977c38d8adb19c39d65f9685d2ee183`

## Included Evidence

| Evidence ID | Task | Result |
| --- | --- | --- |
| `evidence-click-pr-3004-codex-gpt-5-5-20260902` | `click-pr-3004` | success, verifier pass |
| `evidence-click-pr-3079-codex-gpt-5-5-20260902` | `click-pr-3079` | success, verifier pass |

The reconstructed aggregate is 2 attempted, 2 successful, and 2 independent
trials. All included records contain the exact configuration digest above.

## Excluded Evidence

`evidence-click-pr-3013-codex-gpt-5-5-20260830` is excluded. It identifies
`harbor/codex@0.151.0/gpt-5.5` and does not contain a configuration digest, so
it cannot support a Capability for Codex 0.152.1. The Evidence remains
unchanged as a historical observation.

`evidence-click-pr-2930-codex-gpt-5-5-20260906` is excluded because its
configuration digest identifies Codex 0.153.4. It is follow-up Evidence for a
different configuration, not confirmation of this Capability.

All #3152 Evidence is excluded because a 2026-09-09 Harbor no-op control passed
the hidden verifier with reward 1.0. The verifier therefore does not establish
that an executor changed the pre-change workspace to meet the requirement.

## Correction

The Capability previously reported 4/4 by including #3013 based on filename
and suite convention. On 2026-09-09 it was corrected to 3/3 after exact lineage
reconstruction exposed the version mismatch, then to 2/2 when the #3152 no-op
control invalidated that verifier. No Evidence was modified.
