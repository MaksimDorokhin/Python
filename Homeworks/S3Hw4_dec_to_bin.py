# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#     *Пример:*

#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

def dec_to_bin(decimal: int) -> int:
    bit = decimal % 2
    binary = bit
    decimal = decimal // 2
    i = 1

    while (decimal > 0):
        bit = decimal % 2
        decimal = decimal // 2
        binary += bit * (10)**i
        i += 1

    return binary


decimal = int(input('\nВведите десятичное число: '))
print(
    f'\nДесятичное число {decimal} в двочиной системе: {dec_to_bin(decimal)}\n')
