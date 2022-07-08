# Написать программу, которая получает на вход 2 числа и проверяет, является одно квадратом другого.

number_a = int(input('Введите первое число: '))
number_b = int(input('Введите второе число: '))

if number_b == number_a ** 2:
    print(f'Число {number_b} является квадратом числа {number_a}!')
elif number_a == number_b ** 2:
    print(f'Число {number_a} является квадратом числа {number_b}!')
else:
    print(f'Число {number_b} не является квадратом числа {number_a}!')
