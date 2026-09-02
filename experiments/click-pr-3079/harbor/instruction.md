# Shared flag defaults

Multiple flag options can target the same parameter name with different
`flag_value` values. When one of those flags declares `default=True`, the
command should use that flag's value by default regardless of declaration
order.

Update Click so shared flag defaults are order-insensitive, explicit flag
values still override the default, and user callbacks do not receive Click's
internal unset sentinel.
