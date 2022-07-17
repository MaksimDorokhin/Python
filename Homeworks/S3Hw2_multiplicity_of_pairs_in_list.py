# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.
#     *Пример:*
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

import func as f

def multiplicity_of_pairs_in_list(list: list) ->list:
    mult_pair_list = []
    if (len(list) % 2 == 0):
        length = len(list)
    else: length = len(list)+1

    for i in range(0,int(length/2)):
        mult_pair_list.append(list[i] * list[(len(list)) - 1 - i])

    return mult_pair_list


num = int(input('\nВведите N для задания длины произвольного списка: '))
list = f.random_int_list_minus_n_to_n(num)
print(f'\nПолученный список из {num} элементов:\n{list}')
mult_list = multiplicity_of_pairs_in_list(list)
print(f'\nСписок произведений пар элементов начального списка:\n{mult_list}\n')