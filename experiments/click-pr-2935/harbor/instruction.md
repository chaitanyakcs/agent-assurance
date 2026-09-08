# Fix nested-group shell completion

Shell completion loses the active argument state while descending through
multiple nested Click groups. As a result, subcommands and options can be
resolved from the wrong context.

Ensure completion follows the parsed nested context and offers the correct
commands and options at every depth without regressing top-level completion.
