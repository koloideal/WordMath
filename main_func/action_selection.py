from rich.console import Console
from main_func.word2num_math import word2num_math


console = Console()


def action_selection():
    console.print("\n[italic]What do you want to do(enter number of action)?[/italic]")
    action = input()
    if not action.lower() in ['0', '1', 'l', 'q']:
        console.print("[red bold]Please enter a valid meaning[/red bold]")
    else:
        match action:
            case '0':
                print('help')
            case '1':
                while True:
                    string_expression = input("\nPlease enter a string expression or q for exit:\n")
                    if string_expression.lower() == 'q':
                        break
                    else:
                        console.print(f'[bold blue]{word2num_math(string_expression)}[/bold blue]')




