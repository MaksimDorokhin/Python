# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти (1 - 4): '))
if quarter == 1:
    print('Возможный диапазон значений координат Х: от 0 до + \u221e; Y: от 0 до + \u221e')
elif quarter == 2:
    print('Возможный диапазон значений координат Х: от - \u221e до 0; Y: от 0 до + \u221e')
elif quarter == 3:
    print('Возможный диапазон значений координат Х: от - \u221e до 0; Y: от - \u221e до 0')
elif quarter == 4:
    print('Возможный диапазон значений координат Х: от 0 до + \u221e; Y: от - \u221e до 0')
else:
    print("Вы ввели неверное значение номера четверти!")