# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Выводит список простых множителей (без их кол-ва!)

def list_of_simple_multipliers(num: int) ->list:
    simple_list = []
    for i in range(2,num):
        simple_i = True

        for j in range(2,i):
            if (i % j == 0):
                simple_i = False

        if simple_i and (num % i == 0):
            simple_list.append(i)

    return simple_list


num = int(input('\nВведите число для вывода списка его простых множителей (не кол-ва!): '))
simple_list = list_of_simple_multipliers(num)
print(f'\nСписок простых множителей числа {num}:\n{simple_list}\n')

# Нерабочая рекурсия

# def list_of_simple_multipliers(simple_list: list, num: int) ->None:

#     for i in range(2,num):
#         simple_i = True

#         for j in range(2,i):
#             if (i % j == 0):
#                 simple_i = False

#         if simple_i and (num % i == 0):
#             simple_list.append(i)
#             list_of_simple_multipliers(simple_list, num // i)

#     return

# simple_list = []
# num = int(input('Введите число: '))
# list_of_simple_multipliers(simple_list, num)
# print(simple_list)