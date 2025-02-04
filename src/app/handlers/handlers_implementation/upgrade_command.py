import requests
from rich.console import Console
from src.app.business_logic.script_updater import UpdateScript


console = Console()
print_line_separator = lambda: console.print('\n[bold blue]--------------------------------------[/bold blue]\n')


def upgrade_command():
    try:
        requests.get('https://ya.ru')
    except requests.exceptions.ConnectionError:
        print_line_separator()
        console.print('[bold red]No internet connection[/bold red]')
    else:
        latest_tag = UpdateScript.start_update()
        if latest_tag:
            print_line_separator()
            console.print(
                f"[bold green]The newest version ({latest_tag}) of the script has been successfully installed![/bold green]")
            print_line_separator()
            console.print("[bold green]Rerun the script for the changes to take effect[/bold green]")
            print_line_separator()
            exit(0)
        else:
            print_line_separator()
            console.print('[bold red]You have the latest version installed[/bold red]')

