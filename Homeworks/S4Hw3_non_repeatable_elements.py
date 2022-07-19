# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

import func as f

def list_of_non_repeated_elements(initial_list: list) ->list:
    non_repeated_list = []
    for i in initial_list:
        count = 0
        for j in initial_list:
            if (j == i):
                count+=1
        if (count == 1): non_repeated_list.append(i)
    return non_repeated_list


num = int(input('\nВведите кол-во элементов произвольной последовательности целых чисел: '))
int_list = f.random_int_list_minus_n_to_n(num)
print(f'\nСоставленный произвольный список целых чисел:\n{int_list}')
print(f'\nСписок неповторяющихся элементов исходной последовательности:')
print(f'{list_of_non_repeated_elements(int_list)}\n')