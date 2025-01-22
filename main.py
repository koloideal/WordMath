import socket
from typing import Callable
from lang_func.init_user_lang import init_user_lang
from main_func.start_word2math import start_word2math
from art import text2art
from rich.console import Console


console = Console()


def main():
    pc_name = socket.gethostname().replace(" ", "_")
    init_user_lang(pc_name)

    text = text2art('WordMath', font='varsity')
    console.print(f'[bold blue]{text}[/bold blue]')
    work_points: Callable = lambda m, x: console.print(f'[bold red][{m}][/bold red] [blue]*=*=*[/blue] [bold yellow italic]{x}[/bold yellow italic]')
    work_points(0, 'Get Help')
    work_points(1, 'Start Solving')
    print()
    settings_points: Callable = lambda m, x: console.print(f'[bold green][{m}][/bold green] *=*=* [bold purple italic]{x}[bold purple italic]')
    settings_points('L', 'Change Language')
    settings_points('Q', 'Quit')

    # start_word2math()

if __name__ == "__main__":
    main()
