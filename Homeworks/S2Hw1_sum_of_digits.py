# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#     *Пример:*

#     - 6782 -> 23
#     - 0,56 -> 11

def digits_count(number: float) -> int:
    sum = 0
    digits_string = str(number)
    for num in digits_string:
        if num != '.':
            sum += int(num)
    return sum


num = float(input('\nВведите число: '))
print(f'\nСумма цифр введенного числа равна {digits_count(num)}\n')
