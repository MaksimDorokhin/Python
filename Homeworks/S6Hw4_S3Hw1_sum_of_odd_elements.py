# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
#     *Пример:*
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import func as f
from random import randint

# def list_of_odd_elements_from_list(list: list) -> list:
#     odd_list = []

#     for i in range(1, len(list), 2):
#         odd_list.append(list[i])

#     return odd_list


num = int(input('\nВведите N для задания длины произвольного списка: '))
# list = f.random_int_list_minus_n_to_n(num)

# Применение lambda и list comprehension для составления списка рандомных элементов

randlam = lambda n: randint(-n,n+1)
list = [randlam(num) for i in range(0, num)]

print(f'\nПолученный список из {num} элементов:\n{list}')
# odd_list = list_of_odd_elements_from_list(list)

# Применение list comprehension для составления списка элементов, стоящих на нечётной позиции начального

odd_list = [list[i] for i in range(1, len(list), 2)]

print(f'\nЭлементы списка с нечетными индексами:\n{odd_list}')
sum = f.sum_of_elements_in_list(odd_list)
print(f'\nCумма элементов списка, стоящих на нечетных индексах равна: {sum}\n')
