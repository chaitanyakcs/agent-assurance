# Fix CliRunner stdin EOF handling

A chain command accepts `-f -` to consume text from standard input. Under
`CliRunner`, reaching normal EOF currently turns a successful command into an
Abort even though all input was processed.

Fix the regression so stdin-backed `click.File` values finish normally. Keep
the existing behavior that interactive prompt helpers raise `EOFError` when
their simulated input is exhausted.
