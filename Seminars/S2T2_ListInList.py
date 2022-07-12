# Напишите программу, в которой пользователь будет задавать
# две строки, а программа - определять количество вхождений одной строки в другой.

# Мое недоделанное

# def find_list_inside(str_1, str_2):
#     count = 0
#     for i in range(0, len(str_1)):
#         if str_2[0] == str_1[i]:
#             for j in range(1,len(str_2)):
#                 if str_2[j] == str_1[i+j]:
                    

# От Стоуна

# str_1 = input('Введите строку 1: ')
# str_2 = input('Введите строку 2: ')


# org_text = input("Введите строку: ")
# find_text = input("Введите искомую строку: ")

# def text_finder(org_text: str, find_text: str):
#     counter = 0
#     for index in range (0, len(org_text) - len(find_text)+1):
#         if find_text in org_text[index:index+len(find_text)]: counter += 1
#     return counter

# print(f"Текст '{find_text}' втречается в тексте {text_finder(org_text, find_text)} раз")

# Решение от Славы:

# str_1 = 'Hello, world!ll'
# str_2 = 'll'
# count = 0
# for i in range(len(str_1) - len(str_2) + 1):
#     if str_1[i : i + len(str_2)] == str_2:
#         count += 1
# print(count)

# Решение методами Питона:

str_1 = 'Heeeello, world!ll'
str_2 = 'll'
print(str_1.find(str_2))