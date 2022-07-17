# Напишите программу, которая определит позицию второго вхождения строки 
# в списке либо сообщит, что её нет.

list2 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
count2 = 'qwe'
chec = 0

for index in range(len(list2)):
    if count2 == list2[index]:
        chec += 1
        if chec > 1:
            print(f'второе вхождение: {index}')
            break
else:
    print('нет таких')