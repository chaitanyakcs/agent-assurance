# Forward exceptions to Context resources

Resources entered through `Context.with_resource` currently close without the
active exception information. Their `__exit__` methods therefore cannot inspect
or suppress exceptions raised inside the Click context.

Make Context unwinding preserve the standard context-manager contract for both
normal closure and exceptional exit, including exception suppression.
