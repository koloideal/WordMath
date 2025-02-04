from functools import wraps
from typing import Callable
from src.core.router.exceptions import InvalidCommandInstanceException, UnknownCommandHandlerHasAlreadyBeenCreatedException


class Router:
    def __init__(self,
                 ignore_command_register: bool = False):

        self.processed_commands: dict[Callable[[], None], str] = {}
        self.ignore_command_register: bool = ignore_command_register
        self.unknown_command_func: Callable[[str], None] | None = None

    def command(self, command: str):
        if not isinstance(command, str):
            raise InvalidCommandInstanceException()
        else:
            def command_decorator(func):
                self.processed_commands[func] = command
                @wraps(func)
                def wrapper(*args, **kwargs):
                    return func(*args, **kwargs)
                return wrapper
            return command_decorator

    def unknown_command(self, func):
        if self.unknown_command_func is not None:
            raise UnknownCommandHandlerHasAlreadyBeenCreatedException()
        else:
            self.unknown_command_func = func
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper

    def input_command_handler(self, input_command):
        for func, command in self.processed_commands.items():
            if input_command.lower() == command.lower():
                if self.ignore_command_register:
                    return func()
                else:
                    if input_command == command:
                        return func()
        if self.unknown_command_func:
            return self.unknown_command_func(input_command)

