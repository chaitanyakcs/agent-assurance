# Typed flag implicit values

Click flags can be declared with `is_flag=True` and an explicit type. The
explicit type should not prevent Click from computing the implicit flag value.

Update Click so a typed flag still toggles correctly:

- the omitted flag keeps its default;
- passing the flag uses the logical opposite of its default when no
  `flag_value` is supplied;
- `type=bool` and `type=click.BOOL` behave consistently;
- existing option parsing behavior remains unchanged.
