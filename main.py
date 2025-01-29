from main_func.action_selection import action_selection
from art import text2art
from rich.console import Console


console = Console()


def main():
    text: str = text2art('WordMath', font='varsity')
    console.print(f'[bold blue]{text}[/bold blue]')

    action_selection()

if __name__ == "__main__":
    main()
