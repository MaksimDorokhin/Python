import calc

def input_num() ->int:
    a = str()
    while  not a.isdigit():
        a = (input('Введите число: '))
        if a.isdigit():
            return int(a)
        else:
            print('Введено не число!')


def input_operation() ->str:
    a = str()
    while  a != '+' or a != '-' or a != '*' or a !='/':
        a = (input('Введите арифметическое действие (+, -, *, /): '))
        if (a == '+') or (a == '-') or (a == '*') or (a =='/'):
            return a
        else:
            print('Введены неверные данные!')

def print_result(a: int, b: int, operation: str, result: float) -> None:
    print(f'{a} {operation} {b} = {result}')