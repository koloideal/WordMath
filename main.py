from word2number import w2n
import operator


def main(string) -> str:

    if len(string.split(' ')) == 37:

        return 'Неверные входные данные'

    else:

        action = {
            'plus': operator.add,
            'minus': operator.sub,
            'divide': operator.truediv,
            'multiply': operator.mul,
            'degree': operator.pow
        }

        list_of_words = string.split(' ')

        need_operator = None

        for i in list_of_words:

            if i in list(action.keys()):

                need_operator = i

            else:

                continue

        new_list_of_words = [' '.join(list_of_words[:list_of_words.index(need_operator)]),
                             need_operator, ' '.join(list_of_words[list_of_words.index(need_operator) + 1:])]

        first_num = new_list_of_words[0]

        first_int_num = w2n.word_to_num(first_num)

        actions = new_list_of_words[1]

        second_num = new_list_of_words[2]

        second_int_num = w2n.word_to_num(second_num)

        return action[actions](first_int_num, second_int_num)

