import os
import shutil

from main_func.action_selection import action_selection
from art import text2art
from rich.console import Console

from main_func.update_script import update_script, get_latest_release

console = Console()


def main():
    text: str = text2art('WordMath', font='varsity')
    console.print(f'[bold blue]{text}[/bold blue]')

    action_selection()

if __name__ == "__main__":
    shutil.move('func', 'local_data', )
    #update_script(get_latest_release()['url'])
