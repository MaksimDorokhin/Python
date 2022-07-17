# list() -  список: изменяемый, индексируемый
# tuple() - кортеж: неизменяемый, индексируемый. Занимает меньше памяти чем список
# set() - множество: изменяемый, только уникальные элементы, неиндексируемый
# dict() - словарь: изменяемый, индексируемый по ключу


# my_tuple = tuple([1, 2, 3])
# my_tuple = 1, 2, 3
# print(my_tuple)

# my_set = set()
# my_set = {4, 2, 7}
# my_set.add('a')
# my_set.add('b')
# print(my_set)

my_dict = dict()
my_dict = {
    123: 'cool',
    321: 'supercool'
}
print(my_dict[123])
my_dict[523] = 'wtf'
print(my_dict)

for key, val in my_dict.items():
    print(f'{key} - {val}')