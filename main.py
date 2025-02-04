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

    ascii_goodbye_message: str = text2art('GoodBye', font='small')
    goodbye_message: str = f'[bold red]\n{ascii_goodbye_message}{' '*12}made by kolo\n[/bold red]'

    app.include_router(router)
    app.set_initial_greeting(initial_greeting)
    app.set_goodbye_message(goodbye_message)

    app.start_polling()

if __name__ == "__main__":
    main()
