# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

def sequence_list(number: float) -> list:
    tmp_list = []

    for i in range(1, number+1):
        tmp_list.append((1 + 1 / i) ** i)

    return tmp_list


def sum_floats_in_list(list: list) -> float:
    sum = 0

    for i in list:
        sum += i

    return sum


num = int(input('\nВведите N: '))
list = sequence_list(num)
sum = sum_floats_in_list(list)
print(f'\nПоследовательность для заданного N: \n{list}')
print(f'\nСумма элементов последовательности равна {sum}\n')
