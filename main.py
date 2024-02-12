from word2number import w2n
import operator


def main(string) -> str:

    if len(string.split(' ')) != 3:

        return 'Неверные входные данные'

    else:

        list_of_words = string.split(' ')

        first_num = list_of_words[0]

        first_int_num = w2n.word_to_num(first_num)

        actions = list_of_words[1]

        second_num = list_of_words[2]

        second_int_num = w2n.word_to_num(second_num)

        action = {
            'plus': operator.add,
            'minus': operator.sub,
            'divide': operator.truediv,
            'multiply': operator.mul,
            'degree': operator.pow
        }

        return action[actions](first_int_num, second_int_num)


