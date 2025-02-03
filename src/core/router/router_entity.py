from functools import wraps
from typing import Callable
from src.core.router.router_exceptions import InvalidCommandInstanceException


class Router:
    def __init__(self,
                 ignore_command_register: bool = False):

        self.processed_commands: dict[Callable[[], None], str] = {}
        self.ignore_command_register: bool = ignore_command_register
        self.unknown_command_func = None

    def command(self, command = False):
        if not command:
            if not self.unknown_command_func:
                self.unknown_command_func = command
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

    def input_command_handler(self, input_command):
        for func, command in self.processed_commands.items():
            if input_command.lower() == command.lower():
                if self.ignore_command_register:
                    return func()
                else:
                    if input_command == command:
                        return func()




router = Router()

@router.command('1')
def some_command():
    print('a')

@router.command('2')
def some_command():
    print('b')

@router.command('3')
def some_command():
    print('c')

@router.command('T')
def some_command():
    print('d')

router.input_command_handler('T')


