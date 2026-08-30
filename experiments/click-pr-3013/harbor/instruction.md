# Fish completion with quoted partial values

Fish completion can provide an incomplete command value that begins with a
quote or contains shell escaping. The incomplete value should be interpreted as
the logical token the user is typing before completion candidates are selected.

Update Click so a quoted partial value such as `"b` completes the command `b`.
Preserve existing Bash, Zsh, and Fish completion behavior.
