# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from pathlib import Path
import func as f

k_exp = int(input('\nВведите натуральную степень :'))
coefficient_list = f.random_int_list_0_to_100(k_exp+1)
# coefficient_list[2] = 0
# coefficient_list[3] = 1   использовал для проверки выполения всех следующих условий
# coefficient_list[5] = 0
# print(coefficient_list)

polynomial = str()

for i in range(0,len(coefficient_list)):
    plus_element = False
    if (k_exp > 1) and (coefficient_list[i] > 1):
        polynomial+= str(coefficient_list[i])+'*x**('+str(k_exp)+')'
        plus_element = True
    elif (k_exp > 1) and (coefficient_list[i] == 1):
        polynomial+='x**('+str(k_exp)+')'
        plus_element = True
    elif (k_exp == 1) and (coefficient_list[i] > 1):
        polynomial+= str(coefficient_list[i])+'*x'
        if (coefficient_list[i+1] != 0):
            plus_element = True
    elif (k_exp == 1) and (coefficient_list[i] == 1):
        polynomial+='x'
        if (coefficient_list[i+1] != 0):
            plus_element = True
    elif (k_exp == 0) and (coefficient_list[i] != 0):
        polynomial+=str(coefficient_list[i])+' = 0'
    elif (k_exp == 0) and (coefficient_list[i] == 0):
        polynomial+=' = 0'

    if plus_element:
        polynomial+=' + '
    k_exp-=1

# print(polynomial)

path = Path("HWfiles", "S4Hw4.txt") # работает только если в терминале находишься в директории программы
with open (path, 'a') as poly:
    poly.writelines(f'{polynomial}\n')
print(f'\nФайл записан в {path}\n')