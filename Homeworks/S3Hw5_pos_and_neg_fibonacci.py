# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
#  - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def negative_fibonacci(num: int) -> int:
    if num == -1:
        return 1
    elif num == -2:
        return -1
    else:
        return negative_fibonacci(num + 2) - negative_fibonacci(num + 1)


def positive_fibonacci(num: int) -> int:
    if (num <= 1):
        return num
    else:
        return positive_fibonacci(num - 1) + positive_fibonacci(num - 2)


def fibonacci_list(num: int) -> list:
    list = []

    for i in range(-num, 0):
        list.append(negative_fibonacci(i))

    for i in range(0, num+1):
        list.append(positive_fibonacci(i))

    return list


num = int(input(
    '\nВведите число для составления списка чисел Фибоначчи с положительными и отрицательными индексами: '))
print(f'\nСписок чисел Фибоначчи для коэффициента {num}:\n {fibonacci_list(num)}\n')