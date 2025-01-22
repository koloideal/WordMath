from translate import Translator
from lang_func.get_lang import get_lang
from main_func.word2num_math import word2num_math
from lang_func.change_lang import change_lang


def start_word2math() -> None:
    language: str = get_lang()

    if language == "en":
        print('\nif you want to stop the code, enter "stop"')
        print("Supported languages: ru and en")
        print(f'if you want to change language, enter "lang" or "язык", current language - {language}\n')

        while True:
            line = input("Enter a string expression : ")

            if line.lower() == "stop":
                print("GoodBye")
                return

            elif line.lower() in ["lang", "язык"]:
                change_lang()
                start_word2math()

            else:
                try:
                    print(word2num_math(line.replace("to the", "to_the")))
                    print()

                except ValueError:
                    print("An unacceptably large result\n")

    elif language == "ru":
        print('\nЕсли хотите закончить - введите "стоп"')
        print("Поддерживаемые языки: ru и en")
        print(f'Если хотите изменить язык - введите "язык" или "lang", текущий язык - {language}\n')

        while True:
            line = input("Введите строковое выражение : ")

            if line.lower() == "стоп":
                print("До свидания!")
                return

            elif line.lower() in ["язык", "lang"]:
                change_lang()
                start_word2math()

            else:
                try:
                    translator = Translator(to_lang="en", from_lang="ru")
                    result = translator.translate(line)

                except ConnectionError:
                    print("Сервер не отвечает...")

                else:
                    result = (
                        result.replace("to the power of", "to_the_power_of")
                        .replace("to the", "to_the")
                        .replace("divided", "divide")
                    )

                    try:
                        print(str(word2num_math(result))+'\n')

                    except ValueError:
                        print("Недопустимо большой результат\n")
