# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число

# Мое недопиленное

# from pathlib import Path
# path = Path('Testfiles', 'S5T1.txt')
# with open (path, 'r') as file:
#     col = file.readline().split()
# print(col)

# f = lambda x, y: True if y == x - 1 else False
# new_col = list(map(f, col))
# print(new_col)

# От Славы

# my_list = [1, 2, 4, 5, 6]

# f = lambda i: (my_list[i] - my_list[i - 1]) != 1
# x = tuple(filter(f, range(1, len(my_list))))
# print(x[0] + 1)

# Если по обычному

def f(my_list: list):
    for i in range(1, len(my_list)):
        if my_list[i] - my_list[i - 1] != 1:
            return my_list[i - 1] + 1
    return 'Not found'