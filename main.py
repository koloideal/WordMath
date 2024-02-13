from word2number import w2n
import operator


def main(string) -> str:

    try:

        act = {
            ('without', 'lacking', 'deprived_of', 'bereft_of', 'destitute_of', 'minus'): 'minus',
            ('added_to', 'add', 'coupled_with', 'with_the_addition_of', 'plus'): 'plus',
            ('separate', 'part', 'split', 'divide', 'divide_by'): 'divide',
            ('extend', 'expand', 'spread', 'build_up', 'accumulate', 'augment', 'multiply', 'times'): 'multiply',
            ('stage', 'extent', 'grade', 'proportion', 'gradation', 'to_the_power_of', 'degree'): 'degree'
        }

        action = {
            'plus': operator.add,
            'minus': operator.sub,
            'divide': operator.truediv,
            'multiply': operator.mul,
            'degree': operator.pow
        }

        list_of_words = string.split(' ')

        need_operator = None

        need_ = None

        for i in list_of_words:

            for j in list(act.keys()):

                if i in j:

                    need_operator = act[j]
                    need_ = i

            else:

                continue

        new_list_of_words = [' '.join(list_of_words[:list_of_words.index(need_)]),
                             need_operator, ' '.join(list_of_words[list_of_words.index(need_) + 1:])]

        first_num = new_list_of_words[0]

        first_int_num = w2n.word_to_num(first_num)

        actions = new_list_of_words[1]

        second_num = new_list_of_words[2]

        second_int_num = w2n.word_to_num(second_num)

        return action[actions](first_int_num, second_int_num)

    except ValueError:

        return 'Invalid input data'

    except ZeroDivisionError:

        return "Can't divide by zero"


print('if you want to stop the code, enter "stop"\n')

while True:

    line = input('Enter a string expression : ')

    if line == 'stop':

        print('GoodBye')

        break

    else:

        print(main(line))
