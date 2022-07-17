# Часто используемые функции, написанные мной.

import random


def random_int_list_minus_n_to_n(number: int) -> list:
    list = []

    for i in range(0, number):
        list.append(random.randint(-number, number+1))

    return list

def random_float_list_minus_n_to_n(number: int) -> list:
    list = []

    for i in range(0, number):
        list.append(round(random.randint(-number, number+1) + random.random(), 2))

    return list


def sum_of_elements_in_list(list: list) ->int:
    sum = 0

    for i in list:
        sum+=i

    return sum
