from typing import Any


class Monads:
    def __init__(self, parameter, exception_message=None):
        self._parameter = parameter
        self._exception_message = exception_message

    def get_exception_message(self):
        return self._exception_message

    def get_result(self):
        return self._parameter

    def is_failed(self):
        return bool(self._exception_message)

    # Pipe
    def __or__(self, function):
        return self._bind(function)

    def _bind(self, function):
        if self.is_failed():
            return self
        try:
            self._parameter = function(self._parameter)
            # next monad keeping result of previous monad
            return Monads(self._parameter)
        except Exception as e:
            # from now next function in the chain just keep exception_message doing nothing
            return Monads(None, str(e))


def square(x):
    return x * x


def add_five(x):
    return x + 5


def monad(par: Any):
    monad_result = Monads(par) | square | add_five
    if monad_result.is_failed():
        print(monad_result.get_exception_message())
    else:
        print(monad_result.get_result())


if __name__ == "__main__":
    print("Chained functions without error : ")
    monad(3)
    print("String cannot be squared :")
    monad("X")
