# lambda - анонимные функции
# включения - генератор (list comprehension)
# map - применяет функцию с выражением к элементам
# filter -применяет функцию с логическим выражением к элементам
# zip - комбинирует коллекции
# enumerate - нумерует


f = lambda x: x**2

print(f(20))

# map

def f(x):
    return x**2



# for item in my_list:
#         print(f(item))

# new_f = lambda x: True if (x > 10) else False
# my_list = [1, 413, 65, 346]
# res = list(map(new_f, my_list))
# print(res)

# list comprehension (что сделать, с кем сделать, опционально условия)

# my_test = [i for i in range(20) if i > 10]
# print(my_test)
# my_list = [input() for i in range(5)]
# # [print(i) for i in range(20)]
# print(my_list)

# listt = tuple([(i, i) for i in range(1, 21) if (i % 2 == 0)])
# print(listt)

# fliter

# my_list = list(filter(lambda x: x >10, [12, 121, 3, 4, 122]))
# print(my_list)

# my_list = list(filter(lambda x: type(x)==int, [124, 1.2, 42, 65, 76]))
# print(my_list)

# zip

# name = ['a', 'b', 'c', 'd', 'f']
# money = [123, 345, 678]
# new = [1, 2, 3]

# my_list = list(zip(name, money, new))
# print(my_list)

# enumerate

name = ['a', 'b', 'c', 'd', 'f']

my_list = tuple(enumerate(name))
print(my_list)