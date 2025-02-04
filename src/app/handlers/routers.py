from src.core.router.entity import Router
from src.core.app.entity import App

from src.app.handlers.handlers_implementation.help_command import help_command
from src.app.handlers.handlers_implementation.solving_command import start_solving_command
from src.app.handlers.handlers_implementation.upgrade_command import upgrade_command


router: Router = Router(ignore_command_register=True)
app: App = App()


@router.command('u')
def command_update():
    upgrade_command()


@router.command('0')
def command_help():
    help_command()


@router.command('1')
def command_start_solving():
    start_solving_command()


@router.unknown_command
def command_unknown_command(command):
    print(f'Unknown command: {command}')
