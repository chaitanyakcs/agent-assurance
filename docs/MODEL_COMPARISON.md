# Codex Model Comparison

Date: 2026-09-09

## Question

How do two models behave when the Codex harness, CLI version, task, verifier,
reasoning setting, permissions, and environment are held constant?

## Control

Click #3013 was used after a Harbor no-op run confirmed that the hidden
verifier fails on the pre-change workspace:

- no-op job: `jobs/2026-09-09__20-36-18`;
- task checksum: `e9485f424688c79660b983da9e5d53588f66c305d9885da13b31b076555a007d`;
- no-op reward: `0.0`.

Click #3152 was rejected for this comparison because a no-op run earned reward
`1.0`. Its prior Evidence is retained but excluded from Capability aggregates.

## Results

Both supported models ran through Codex CLI 0.153.4 with high reasoning and
passed the same deterministic verifier.

| Model | Outcome | Reward | Duration | Input tokens | Cache tokens | Output tokens | Cost |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `gpt-5.5` | success | 1.0 | 298.377 s | 693,557 | 634,624 | 5,721 | $0.783607 |
| `gpt-5.6-sol` | success | 1.0 | 307.948 s | 428,506 | 360,320 | 4,374 | $0.504352 |

On this single trial, `gpt-5.6-sol` used 38.2% fewer input tokens, 23.5% fewer
output tokens, and cost 35.6% less. It took 3.2% longer end to end. These are
observations, not estimates of general model efficiency or capability.

Evidence:

- `evidence-click-pr-3013-model-comparison-gpt-5-5-20260909`
- `evidence-click-pr-3013-model-comparison-gpt-5-6-sol-20260909`

## Unsupported model attempt

An attempted `gpt-5.4` run was rejected by the ChatGPT-backed Codex account
before agent work began. It is recorded as an aborted model-availability event,
not a model failure. Harbor subsequently ran the #3152 verifier, but its pass
cannot be attributed to the model and helped expose that verifier's invalid
no-op behavior.

## Conclusion

The experiment demonstrates that model identity must remain part of the exact
Capability subject. It does not establish that either model is more capable:
both are 1/1 on one low-risk Click bugfix. At least several valid tasks and
repeats are needed before producing separate L1 Capability statements or a
comparative recommendation.
