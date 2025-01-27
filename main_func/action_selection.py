from typing import Callable
from rich.console import Console
from main_func.word2num_math import word2num_math


console = Console()


def action_selection():
    while True:
        work_points: Callable = lambda m, x: console.print(
            f'[bold red][{m}][/bold red] [blue]*=*=*[/blue] [bold yellow italic]{x}[/bold yellow italic]')
        work_points(0, 'Get Help')
        work_points(1, 'Start Solving')
        print()
        settings_points: Callable = lambda m, x: console.print(
            f'[bold green][{m}][/bold green] *=*=* [bold purple italic]{x}[bold purple italic]')
        settings_points('U', 'Update WordMath')
        settings_points('Q', 'Quit')

        console.print("\n[italic]What do you want to do(enter number of action)?[/italic]")
        action = input()
        if not action.lower() in ['0', '1', 'u', 'q']:
            console.print("[red bold]Please enter a valid meaning[/red bold]")
        else:
            match action.lower():
                case '0':
                    print('help')
                case '1':
                    while True:
                        string_expression = input("\nPlease enter a string expression or q for exit:\n")
                        if string_expression.lower() == 'q':
                            break
                        else:
                            console.print(f'[bold blue]{word2num_math(string_expression)}[/bold blue]')
                case 'q':
                    console.print('[bold red]GoodBye[/bold red]')
                    break
        print('\n\n')




