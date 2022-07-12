# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.

#     *Пример:*

#     - Для N = 5: 1, -3, 9, -27, 81

def sequence(n: int):
    sequence_list = [1]
    i = 0
    while i < n-1:
        sequence_list.append(sequence_list[i]*-3)
        i += 1
    return sequence_list


n = int(input('Введите n: '))
print(sequence(n))
