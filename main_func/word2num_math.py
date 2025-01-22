from word2number import w2n
import operator
from local_data_func.get_operator_synonyms import get_operator_synonyms


def word2num_math(string: str) -> str:
    print(string)
    operator_synonyms: dict[str, list[str]] = get_operator_synonyms()

    def variables_to_operator(synonym):
        for key in operator_synonyms.keys():
            if synonym in operator_synonyms[key]:
                return key

    action = {
        "plus": operator.add,
        "minus": operator.sub,
        "divide": operator.truediv,
        "multiply": operator.mul,
        "degree": operator.pow,
    }

    process_list = []
    all_variables_of_operators: list[str] = [x for l in operator_synonyms.values() for x in l]
    operators = {}

    while True:
        is_clear = True
        number_of_operator = 1
        for ope in all_variables_of_operators:
            try:
                ope_index = string.index(ope)
                if ope_index in operators.keys():
                    is_clear = True
                    break
            except ValueError:
                continue
            else:
                is_clear = False
                operators[number_of_operator] = variables_to_operator(ope)
                number_of_operator += 1
                string = string.replace(ope, "&&", 1)
        if is_clear:
            break
    print(string)
    print(operators.items())
    total = string.split("&&")
    for k, v in operators.items():
        total.insert(k, v)

    print(' '.join(total))





'''    new_list_of_words = [
        " ".join(list_of_words[: list_of_words.index(need_)]),
        need_operator,
        " ".join(list_of_words[list_of_words.index(need_) + 1 :]),
    ]

    first_num = new_list_of_words[0]
    first_int_num = w2n.word_to_num(first_num)

    actions = new_list_of_words[1]

    second_num = new_list_of_words[2]
    second_int_num = w2n.word_to_num(second_num)

    return action[actions](first_int_num, second_int_num)'''

'''    except ValueError:
        return "Invalid input data\n"

    except ZeroDivisionError:
        return "Can't divide by zero\n"'''
