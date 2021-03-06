# Часто используемые функции, написанные мной.

import random
from pathlib import Path

def random_int_list_minus_n_to_n(number: int) -> list:
    list = []

    for i in range(0, number):
        list.append(random.randint(-number, number+1))

    return list

def random_int_list_0_to_100(number: int) -> list:
    list = []

    for i in range(0, number):
        list.append(random.randint(0, 101))

    return list

def random_float_list_minus_n_to_n(number: int) -> list:
    list = []

    for i in range(0, number):
        list.append(round(random.randint(-number, number+1) + random.random(), 2))

    return list


def sum_of_elements_in_list(list: list) ->int:
    sum = 0

    for i in list:
        sum+=i

    return sum

def check_for_int(check_number: str) ->bool:
    try:
        int(check_number)
        return True
    except: 
        return False

def import_string_from_file(file_path: str, input_file: str) ->str:
    final_path = Path(file_path, input_file)
    with open (final_path, 'r') as file:
        return file.readline()

def export_string_to_file(output_string: str,file_path: str, output_file: str) -> None:
    final_path = Path(file_path, output_file)
    with open (final_path, 'w') as file:
        file.write(output_string)
    return

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