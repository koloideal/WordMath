from rich.console import Console

from src.core.router.entity import Router
from src.core.app.entity import App

from src.app.handlers.handlers_implementation.help_command import help_command
from src.app.handlers.handlers_implementation.solving_command import start_solving_command
from src.app.handlers.handlers_implementation.upgrade_command import upgrade_command


work_router: Router = Router(name='Work points:',
                             ignore_command_register=False)
settings_router: Router = Router(name='Settings points:',
                                 ignore_command_register=True)
app: App = App()

console = Console()


@work_router.command(command='0', description='Get Help')
def command_help():
    help_command()


@work_router.command(command='1', description='Start Solving')
def command_start_solving():
    start_solving_command()


@settings_router.command(command='U', description='Update WordMath')
def command_update():
    upgrade_command()


@work_router.unknown_command
def command_unknown_command(command):
    console.print(f'[bold red]Unknown command: [/bold red]{command}')
