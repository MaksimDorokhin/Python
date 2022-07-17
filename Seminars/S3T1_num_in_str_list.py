# Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.

str_list = ['12asd36', '256', 'dsds89358', '5698a']

s_nym = input('Enter the number: ')
is_Found = False

for item in str_list:
    print(item)
    if item.__contains__(s_nym):
        is_Found = True
        break

print(is_Found)