path = 'file.txt'
with open (path, 'r') as data:
    list = data.readline().split()
    for i in list:
        i = int(i)
print(list)
print(type(list[0]))

# доделать по лекции