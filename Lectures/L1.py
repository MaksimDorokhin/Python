
# типы данных и переманная
# int, float, boolean, str, list, None
# value = None
# print(type(value))
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))
# s = 'hello \nworld'  # вывод строки \n перенос на новую строку
# s = 'hello world'
# a = 123
# b = 1.23
# print(s)
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)

# list = ['1','2','3']
# col = ['hello', 1,2,4.5,True]
# print(list)
# print(col)

# Ввод и вывод данных
# print, input

# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, ' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции
# +, -, *, /, %, //, **
# **, + унарный, - унарный, *, /, //, %, +, -
# (), Сокращенные операции
# a = 1.312312223
# b = 3
# c = round(a * b, 7)
# print(c)

# a = 3
# a = a + 5
# a += 5

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, (верхняя крышка)
# is, is not, in, not in
# gen

# f = [1,2,3,4]
# print(f)
# print (not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я ждал Вас, Марина!')
# elif username == 'Ильнар':
#      print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющие конструкции
# for

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i)


# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwe - rty':
#     print(i)

text = 'съещь еще этих мягких французских булок'

# print(len(text)) #39
# print('еще' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('еще','ЕЩЕ')) #

# print(text[0]) # с
# print(text[1]) # ъ
# print(text[len(text)]) #IndexError
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) #ешь еще
# print(text[6:-18]) #еще этих мягких
# print(text[0:len(text):6]) #сеикакл
# print(text[::6]) #сеикакл

# text = text[2:9] + text[-5] + text[:2] #...
# for c in text:
#     print(c)


# help(int) # помощь по неизвестной команде


# Списки введение
## list = list

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#     i*=2
#     print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e) # red green blue

# for e in colors:
#     print(e*2) # redred greengreen blueblue

# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# Функции

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 2
# print(f(arg))
# print(type(f(arg)))