import cmd

class MyCLI(cmd.Cmd):
    intro = 'Добро пожаловать в интерактивную CLI-утилиту! Введите help или ? для списка команд.\n'
    prompt = '(cli) '

    def do_hello(self, arg):
        """Приветствие"""
        print("Привет, пользователь!")

    def do_goodbye(self, arg):
        """Прощание"""
        print(f"До свидания, {arg}!")
        return True  # Завершает работу приложения

    def do_exit(self, arg):
        """Выход из приложения"""
        print("Выход из приложения.")
        return True  # Завершает работу приложения

if __name__ == '__main__':
    MyCLI().cmdloop()
