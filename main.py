import socket
from lang_func.init_user_lang import init_user_lang
from main_func.start_word2math import start_word2math
from art import tprint
from rich.console import Console


console = Console()


def main():
    pc_name = socket.gethostname().replace(" ", "_")
    init_user_lang(pc_name)

    tprint('WordMath', font='rnd-large')
    pretty_print = lambda m, x: console.print(f'[bold red][{m}][/bold red] [blue]*=*=*[/blue] {x}')
    pretty_print(0, 'Change Language')
    pretty_print(1, 'Get Help')
    pretty_print(2, 'Start Solving')

    pretty_print
    pretty_print('Q', 'Quit')

    start_word2math()

if __name__ == "__main__":
    main()
