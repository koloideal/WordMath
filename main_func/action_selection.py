from typing import Callable
import requests
from rich.console import Console
from main_func.word2num_math import word2num_math
from main_func.update_script import UpdateScript
from art import text2art


console = Console()
print_line_separator = lambda: print('\n--------------------------------------\n')


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

        console.print("\n[italic white bold]What do you want to do(enter number of action)? [/italic white bold]")
        action = input()
        if not action.lower() in ['0', '1', 'u', 'q']:
            print_line_separator()
            console.print("[red bold]Enter a valid meaning[/red bold]")
        else:
            match action.lower():
                case '0':
                    print_line_separator()
                    console.print("[italic bold]The main functionality of the script is to convert an expression from a string"
                                  " to a mathematical one and then calculate this expression. Project GitHub: https://github.com/koloideal/WordMath[/italic bold]")
                case '1':
                    while True:
                        console.print("\n[italic]Enter a string expression or [bold italic green] Q [/bold italic green] for exit:[/italic]")
                        string_expression = input()
                        if string_expression.lower() == 'q':
                            break
                        else:
                            print_line_separator()
                            console.print(
                                f'[bold green]Answer:[/bold green]  [bold blue]{word2num_math(string_expression)}[/bold blue]')
                            print_line_separator()
                case 'q':
                    text = text2art("GoodBye", font="small")
                    console.print(f'[bold red]\n{text}{' '*12}made by kolo\n[/bold red]')
                    break
                case 'u':
                    try:
                        requests.get('https://ya.ru')
                    except requests.exceptions.ConnectionError:
                        print_line_separator()
                        console.print('[bold red]No internet connection[/bold red]')
                    else:
                        is_upgrade = UpdateScript.start_update()
                        if is_upgrade:
                            exit(0)
                        else:
                            print_line_separator()
                            console.print('[bold red]You have the latest version installed[/bold red]')

        print_line_separator()


