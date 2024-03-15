from translate import Translator
from func.get_lang import get_lang
from func.word2num_math import word2num_math
from func.change_lang import change_lang


def helper() -> None:

    lang = get_lang()

    if lang == 'en':

        print('\nif you want to stop the code, enter "stop"')
        print('Supported languages: ru and en')
        print(f'if you want to change language, enter "lang" or "язык", current language - {lang}\n')

        while True:

            line = input('Enter a string expression : ')

            if line.lower() == 'stop':

                print('GoodBye')

                break

            elif line.lower() in ['lang', 'язык']:

                change_lang()
                helper()

            else:

                try:

                    print(word2num_math(line.replace('to the', 'to_the')))
                    print()

                except ValueError:

                    print('An unacceptably large result\n')

    elif lang == 'ru':

        print('\nЕсли хотите закончить - введите "стоп"')
        print('Поддерживаемые языки: ru и en')
        print(f'Если хотите изменить язык - введите "язык" или "lang", текущий язык - {lang}\n')

        while True:

            line = input('Введите строковое выражение : ')

            if line.lower() == 'стоп':

                print('До свидания!')

                break

            elif line.lower() in ['язык', 'lang']:

                change_lang()
                helper()

            else:

                try:

                    translator = Translator(to_lang='en', from_lang='ru')

                    result = translator.translate(line)

                except ConnectionError:

                    print('Сервер не отвечает...')

                else:

                    result = result.replace('to the power of', 'to_the_power_of').replace('to the', 'to_the').replace('divided', 'divide')

                    try:

                        print(word2num_math(result))
                        print()

                    except ValueError:

                        print('Недопустимо большой результат\n')
