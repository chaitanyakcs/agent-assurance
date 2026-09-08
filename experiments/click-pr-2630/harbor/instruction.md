# Specialize length-only progressbar typing

Calling `click.progressbar(length=N)` without an iterable produces integer
positions at runtime, but its static return type is not specialized accordingly.

Add typing support so type checkers infer `ProgressBar[int]` for length-only
calls while preserving generic inference for iterable-based calls. Do not alter
runtime behavior.
