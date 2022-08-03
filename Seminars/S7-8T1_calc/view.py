import calc
from logger import logger

def input_num() ->int:
    a = str()
    while  not a.isdigit():
        a = (input('Введите число: '))
        if a.isdigit():
            return int(a)
        else:
            print('Введено не число!')
            logger(f'Wrong input of number = {a}')


def input_operation() ->str:
    a = str()
    while  a != '+' or a != '-' or a != '*' or a !='/':
        a = (input('Введите арифметическое действие (+, -, *, /): '))
        if (a == '+') or (a == '-') or (a == '*') or (a =='/'):
            return a
        else:
            print('Введены неверные данные!')
            logger(f'Wrong input of operation = {a}')

def print_result(a: int, b: int, operation: str, result: float) -> None:
    print(f'{a} {operation} {b} = {result}')