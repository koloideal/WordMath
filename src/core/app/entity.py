from typing import Callable
from ..router.entity import Router
from .exceptions import InvalidRouterInstanceException


class App:
    def __init__(self,
                 prompt: str = 'Enter a command',
                 exit_command: str = 'q',
                 ignore_exit_command_register: bool = True,
                 initial_greeting: str = 'Hello',
                 goodbye_message: str = 'GoodBye',
                 line_separate: str = '\n',
                 print_func: Callable[[str], None] = print) -> None:
        self.routers: list[Router] = []
        self.prompt = prompt
        self.print_func = print_func
        self.exit_command = exit_command
        self.ignore_exit_command_register = ignore_exit_command_register
        self.goodbye_message = goodbye_message
        self.initial_greeting = initial_greeting
        self.line_separate = line_separate

    def start_polling(self) -> None:
        self.print_func(self.initial_greeting)
        while True:
            self.print_func(self.prompt)
            command: str = input()

            if command.lower() == self.exit_command.lower():
                if self.ignore_exit_command_register:
                    self.print_func(self.goodbye_message)
                    exit(0)
                else:
                    if command == self.exit_command:
                        self.print_func(self.goodbye_message)
                        exit(0)

            self.print_func(self.line_separate)

            for router in self.routers:
                router.input_command_handler(command)
                self.print_func(self.line_separate)


    def set_initial_greeting(self, greeting: str) -> None:
        self.initial_greeting = greeting


    def set_goodbye_message(self, message: str) -> None:
        self.goodbye_message = message


    def include_router(self, router: Router) -> None:
        if not isinstance(router, Router):
            raise InvalidRouterInstanceException()
        self.routers.append(router)

