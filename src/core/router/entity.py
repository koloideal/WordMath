from functools import wraps
from typing import Callable, Any
from src.core.router.exceptions import (InvalidCommandInstanceException,
                                        UnknownCommandHandlerHasAlreadyBeenCreatedException,
                                        InvalidDescriptionInstanceException)


class Router:
    def __init__(self,
                 name: str,
                 ignore_command_register: bool = False):

        self.processed_commands: list[dict[str, Callable[[], None] | str]] = []
        self.ignore_command_register: bool = ignore_command_register
        self._name = name
        self.unknown_command_func: Callable[[str], None] | None = None

    def command(self, command: str, description: str) -> Callable[[Any], Any]:
        if not isinstance(command, str):
            raise InvalidCommandInstanceException()
        if not isinstance(description, str):
            raise InvalidDescriptionInstanceException()
        else:
            def command_decorator(func):
                self.processed_commands.append({'func': func,
                                                'command': command,
                                                'description': description})
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
        for command_entity in self.processed_commands:
            if input_command.lower() == command_entity['command'].lower():
                if self.ignore_command_register:
                    return command_entity['func']()
                else:
                    if input_command == command_entity['command']:
                        return command_entity['func']()
        if self.unknown_command_func:
            return self.unknown_command_func(input_command)

    def get_registered_commands(self) -> list[dict[str, Callable[[], None] | str]]:
        return self.processed_commands

    def get_name(self) -> str:
        return self._name

