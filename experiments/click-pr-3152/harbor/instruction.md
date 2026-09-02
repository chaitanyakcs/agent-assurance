# Optional flag values on non-flag options

An option can be configured with `is_flag=False` and `flag_value`. In that
configuration, the option should accept either zero values or one explicit
value.

Update Click so:

- omitting the option keeps its default;
- providing the option without a value uses `flag_value`;
- providing the option with a value uses the explicit value;
- existing option parsing behavior remains unchanged.
