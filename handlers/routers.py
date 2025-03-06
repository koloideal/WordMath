from rich.console import Console
from argenta.router import Router
from argenta.command import Command

from handlers.handlers_implementation.help_command import help_command
from handlers.handlers_implementation.solving_command import start_solving_command
from handlers.handlers_implementation.upgrade_command import upgrade_command


work_router: Router = Router(title='Work points:')
settings_router: Router = Router(name='Settings points:')

console = Console()


@work_router.command(Command(trigger='0', description='Get Help'))
def command_help():
    help_command()


@work_router.command(Command(trigger='1', description='Start Solving'))
def command_start_solving():
    start_solving_command()


@settings_router.command(Command(trigger='U', description='Update WordMath'))
def command_update():
    upgrade_command()
