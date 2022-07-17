# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
#     *Пример:*
#     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import func as f


def difference_of_min_and_max_fractional_part_in_list(list: list) -> float:
    fract_list = []

    for element in list:
        is_fract = False
        fract_element = '0.'

        for j in range(0, len(str(element))):
            if is_fract:
                fract_element += str(element)[j]
            if not is_fract and (str(element)[j] == '.'):
                is_fract = True

        fract_list.append(float(fract_element))

    min_float = fract_list[0]
    max_float = fract_list[0]

    for f in fract_list:
        if f < min_float:
            min_float = f
        if f > max_float:
            max_float = f

    diff = round((max_float - min_float), 2)
    return diff


num = int(
    input('\nВведите N для задания длины произвольного списка вещественных чисел: '))
list = f.random_float_list_minus_n_to_n(num)
print(f'\nПолученный список из {num} элементов:\n{list}')
diff = difference_of_min_and_max_fractional_part_in_list(list)
print(
    f'\nРазница между максимальным и минимальным значением дробной части элементов: {diff}\n')
