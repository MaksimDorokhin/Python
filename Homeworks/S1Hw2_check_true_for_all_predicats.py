# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
    
x = bool(input('Введите значение X (любое значение для True или просто ENTER для False): '))
print(f'Х = {x}')
y = bool(input('Введите значение X (любое значение для True или просто ENTER для False): '))
print(f'Y = {y}')
z = bool(input('Введите значение X (любое значение для True или просто ENTER для False): '))
print(f'Z = {z}')

if not (x or y or z) == (not x and not y and not z):
    print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z) истинно')
else:
    print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z) ложно')