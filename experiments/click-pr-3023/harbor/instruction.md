# Keep shutil lazy during import

Importing Click currently imports Python's `shutil` module even when no feature
that needs it is used. This adds avoidable startup work.

Make `shutil` imports local to the code paths that require them. Preserve pager,
editor, terminal sizing, progress rendering, and `CliRunner` cleanup behavior.
