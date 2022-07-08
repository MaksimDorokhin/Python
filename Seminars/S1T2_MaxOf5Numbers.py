# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

def Input_List(count):
    l = list()
    i = 0
    while i < count:
        x = int(input(f'Введите число {i+1}: '))
        l.append(int(x))
        i += 1
    return l


check_list = Input_List(5)

max = check_list[0]

for i in check_list:
    if i > max:
        max = i

print(f'Максимальное число равно  {max}')
