# Напишите программу, удаляющую из текста все слова, содержащие "абв".

from pathlib import Path
path_input = Path('HWfiles', 'S5Hw1_input.txt')
path_output = Path('HWfiles', 'S5Hw1_output.txt')

with open (path_input, 'r') as file:
    input_string = file.readline()

print(f'\nИсходная строка из файла:\n{input_string}')
col = input_string.split()
new_col = [item for item in col if 'абв' not in item]
output_string = ' '.join(new_col)
print(f'\nСтрока после удаления слов, содержащих "абв":\n{output_string}\n')

with open (path_output, 'w') as file:
    file.write(output_string)