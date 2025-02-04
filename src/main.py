from main_func.action_selection import action_selection
from art import text2art
from rich.console import Console


console = Console()


def main():
    text: str = text2art('WordMath', font='nancyj')
    console.print(f'[bold blue]\n\n{text}[/bold blue]')

    action_selection()

if __name__ == "__main__":
    main()
