# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#     *Пример:*

#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def list_of_multiplies(number: int) -> list:
    list = []
    multiply = 1

    for i in range(1, number+1):
        multiply *= i
        list.append(multiply)

    return list


n = int(input('\nВведите N: '))
print(f'\nНабор произведений от 1 до N:\n{list_of_multiplies(n)}\n')
