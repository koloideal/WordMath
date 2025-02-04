from src.app.handlers.routers import router
from src.core.app.entity import App
from art import text2art
from rich.console import Console


app: App = App(prompt='[bold italic blue]Select action:[/bold italic blue]',
               line_separate='[bold green]\n----------------------------\n[/bold green]',
               print_func=Console().print)


def main():
    ascii_name: str = text2art('WordMath', font='nancyj')
    initial_greeting: str = f'[bold red]\n\n{ascii_name}[/bold red]'

    '''        work_points: Callable = lambda m, x: console.print(
            f'[bold red][{m}][/bold red] [blue]*=*=*[/blue] [bold yellow italic]{x}[/bold yellow italic]')
        work_points(0, 'Get Help')
        work_points(1, 'Start Solving')
        print()
        settings_points: Callable = lambda m, x: console.print(
            f'[bold green][{m}][/bold green] *=*=* [bold purple italic]{x}[bold purple italic]')
        settings_points('U', 'Update WordMath')
        settings_points('Q', 'Quit')

        console.print("\n[italic white bold]What do you want to do(enter number of action)? [/italic white bold]")'''

    ascii_goodbye_message: str = text2art('GoodBye', font='small')
    goodbye_message: str = f'[bold red]\n{ascii_goodbye_message}{' '*12}made by kolo\n[/bold red]'

    app.include_router(router)
    app.set_initial_greeting(initial_greeting)
    app.set_goodbye_message(goodbye_message)

    app.start_polling()

if __name__ == "__main__":
    main()
