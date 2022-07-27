# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from curses.ascii import isdigit
from func import import_string_from_file as impstr
from func import export_string_to_file as expstr

def RLE_encoder(input_string: str) ->str:
    output_string = str()
    count = 1
    for i in range(1,len(input_string)):
        if input_string[i] == input_string[i-1] and i != len(input_string)-1:
            count+=1
        elif input_string[i] != input_string[i-1] and i != len(input_string)-1:
            if (count == 1):
                output_string += input_string[i-1]
            else:
                output_string +=f'{count}'+input_string[i-1]
                count = 1
        elif  input_string[i] == input_string[i-1] and i == len(input_string)-1:
            count+=1
            output_string +=f'{count}'+input_string[i]
        elif  input_string[i] != input_string[i-1] and i == len(input_string)-1:
            if (count == 1):
                output_string += input_string[i-1] + input_string[i]
            else:
                output_string +=f'{count}'+input_string[i-1] + input_string[i]
    return output_string

def RLE_decoder(input_string: str) ->str:
    counter = str()
    output_string = str()
    for i in range(0,len(input_string)):
        if input_string[i].isdigit():
            counter += input_string[i]
        elif not input_string[i].isdigit():
            if counter == '':
                output_string += input_string[i]
            else:
                output_string += int(counter) * input_string[i]
                counter = str()
    return(output_string)

input_string = impstr('HWfiles', 'S5Hw4_RLE_input.txt')
print(f'\nИсходная строка из файла:\n{input_string}')
encoded_string = RLE_encoder(input_string)
print(f'\nСжатая строка:\n{encoded_string}')
expstr(encoded_string, 'HWfiles', 'S5Hw4_RLE_encoded.txt')
decoded_string = RLE_decoder(encoded_string)
print(f'\nДекодированная строка:\n{decoded_string}\n')
expstr(decoded_string, 'HWfiles', 'S5Hw4_RLE_decoded.txt')