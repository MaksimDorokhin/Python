# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
n = int(input('Введите N: '))
i = -n

while i <= n:
    print(i, end=' ')
    i+=1
