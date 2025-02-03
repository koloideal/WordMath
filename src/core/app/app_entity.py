from typing import Callable
from src.core.router.router_entity import Router
from src.core.app.app_exceptions import InvalidRouterInstanceException


class App:
    def __init__(self,
                 prompt: str = 'Enter a command',
                 exit_command: str = 'q',
                 ignore_exit_command_register: bool = True,
                 goodbye_message: str = 'GoodBye',
                 print_func: Callable[[str], None] = print) -> None:
        self.routers: list[Router] = []
        self.prompt = prompt
        self.print_func = print_func
        self.exit_command = exit_command
        self.ignore_exit_command_register = ignore_exit_command_register
        self.goodbye_message = goodbye_message

    def start_polling(self):
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

            for router in self.routers:
                router.input_command_handler(command)


    def include_route(self, route):
        if not isinstance(route, Router):
            raise InvalidRouterInstanceException()
        self.routers.append(route)

