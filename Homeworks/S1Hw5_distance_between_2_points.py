# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from cmath import sqrt

first_point_x = float(input('Введите значение координаты X первой точки: '))
first_point_y = float(input('Введите значение координаты Y первой точки: '))
second_point_x = float(input('Введите значение координаты X второй точки: '))
second_point_y = float(input('Введите значение координаты Y второй точки: '))

dist = sqrt((second_point_x - first_point_x)**2 + (second_point_y - first_point_y)**2)
print(f'Расстояние между точками = {round(dist.real, 2)}')