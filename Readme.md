# Monad design pattern
Recently, I came across a Monad design pattern used as a basic design block in functional programming. The same pattern can help handle exceptions in composing functions.
 Monad design pattern chain functions passing arguments between functions accompanied by metadata about the possible exception. If an exception arises in the middle of the chain, the rest functions pass the info about the exception down the chain. Monad never raises its own exceptions, just setting error metadata. The caller thus does not need to take care of exception handling, which results in more conscious code.