import socket
from typing import Callable
from local_data_func.init_user_lang import init_user_lang
from main_func.action_selection import action_selection
from art import text2art
from rich.console import Console


console = Console()


def main():
    pc_name = socket.gethostname().replace(" ", "_")
    init_user_lang(pc_name)

    text = text2art('WordMath', font='varsity')
    console.print(f'[bold blue]{text}[/bold blue]')

    action_selection()

if __name__ == "__main__":
    main()
