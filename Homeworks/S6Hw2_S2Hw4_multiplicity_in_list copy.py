# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.

import random


# def random_list_minus_n_to_n(number: int) -> list:
#     list = []

#     for i in range(0, number):
#         list.append(random.randint(-number, number+1))

#     return list


def int_list_from_string(positions: str) -> list:
    positions_list = positions.split(' ')

    # for i in range(0, len(positions_list)):
    #     positions_list[i] = (int(positions_list[i]))

    # Применение list comprehension
    
    positions_list = [int(pos) for pos in positions_list]

    return positions_list


def multiplicity_in_list(list: list, positions_list: list) -> int:
    multiplicity = 1

    for i in positions_list:
        multiplicity *= list[i-1]

    return multiplicity


num = int(input('\nВведите N: '))
# list = random_list_minus_n_to_n(num)

# Применение lambda и list comprehension для составления списка рандомных элементов

randlam = lambda n: random.randint(-n,n+1)
list = [randlam(num) for i in range(0, num)]


print(f'\nПолученный список с числами из промежутка -{num} до {num}\n{list}\n')
positions = input(
    f'Введите позиции элементов для вычисления произведения через пробел (от 1 до {num}):\n')
pos_list = int_list_from_string(positions)
print(
    f'\nПроизведение элементов на указанных позициях равно {multiplicity_in_list(list, pos_list)}\n')