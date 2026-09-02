# Enum choice default rendering

Click can build `Choice` parameters from Enum classes. When help text displays
a default value for an Enum-backed choice, the visible default should use the
Enum member name rather than the Python representation of the Enum object.

Update Click so Enum choice defaults render cleanly in help output. Preserve
existing help rendering for non-Enum defaults and do not coerce the stored
default value only for display.
