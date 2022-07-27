
# Создайте программу для игры в ""Крестики-нолики"".

from curses.ascii import isdigit
from random import randint


def player_turn(player_num: int, row1: list, row2: list, row3: list) -> None:

    match player_num:
        case 1: 
            print(f'Ходит игрок {player_num} (крестики)')
        case 2: 
            print(f'Ходит игрок {player_num} (нолики)')

    good_turn = False

    while not good_turn:

        good_row = False
        good_column = False
        
        while not good_row:
            turn_row = input('Введите номер ряда для вашего хода (от 1 до 3): ') 
            if turn_row.isdigit():
                turn_row = int(turn_row)
                if (1 <= turn_row <= 3):
                    good_row = True
                else: 
                    print('Вы ввели число вне диапазона рядов, повторите ввод!')
            else: 
                print('Вы ввели некорректные данные, повторите ввод!')
            
        while not good_column:
            turn_column = input('Введите номер колонки для вашего хода (от 1 до 3): ')
            if turn_column.isdigit():
                turn_column = int(turn_column)
                if (1 <= turn_column <= 3):
                    good_column = True
                else: 
                    print('Вы ввели число вне диапазона столбцов, повторите ввод!')
            else: 
                print('Вы ввели некорректные данные, повторите ввод!')

        match turn_row:
            case 1:
                if (row1[turn_column-1] == ' '):
                    if (player_num == 1):
                        row1[turn_column-1] = 'X'
                    else: row1[turn_column-1] = '0'
                    good_turn = True
                else:
                        print('Упс, тут уже кто-то походил, попробуйте снова!')
            case 2:
                if (row2[turn_column-1] == ' '):
                    if (player_num == 1):
                        row2[turn_column-1] = 'X'
                    else: row2[turn_column-1] = '0'
                    good_turn = True
                else:
                        print('Упс, тут уже кто-то походил, попробуйте снова!')
            case 3:
                if (row3[turn_column-1] == ' '):
                    if (player_num == 1):
                        row3[turn_column-1] = 'X'
                    else: row3[turn_column-1] = '0'
                    good_turn = True
                else:
                        print('Упс, тут уже кто-то походил, попробуйте снова!')
    return

def cpu_turn(row1: list, row2: list, row3: list) -> None:
    good_turn = False
    print(f'Ходит бот (нолики)')

    while not good_turn:
    
        turn_row = randint(1,3)
        turn_column = randint(1,3)
        
        match turn_row:
            case 1:
                if (row1[turn_column-1] == ' '):
                    row1[turn_column-1] = '0'
                    good_turn = True
            case 2:
                if (row2[turn_column-1] == ' '):
                    row2[turn_column-1] = '0'
                    good_turn = True
            case 3:
                if (row3[turn_column-1] == ' '):
                    row3[turn_column-1] = '0'
                    good_turn = True
    return
                    

def end_game(row1: list, row2: list, row3: list) -> bool:
    if    (row1[0] == row1[1] == row1[2] != ' ' 
        or row2[0] == row2[1] == row2[2] != ' '
        or row3[0] == row3[1] == row3[2] != ' '
        or row1[0] == row2[0] == row3[0] != ' '
        or row1[1] == row2[1] == row3[1] != ' '
        or row1[2] == row2[2] == row3[2] != ' '
        or row1[0] == row2[1] == row3[2] != ' '
        or row1[2] == row2[1] == row3[0] != ' '
        or (row1[0] != ' ' and row1[1] != ' ' and row1[2] != ' '
        and row2[0] != ' ' and row2[1] != ' ' and row2[2] != ' '
        and row3[0] != ' ' and row3[1] != ' ' and row3[2] != ' ')):
        return True
    return False


print('Добро пожаловать в консольные крестики-нолики!'
            '\nИгрок 1 играет крестиками'
            '\nИгрок 2 или бот играет ноликами')

good_game_mode = False

while not good_game_mode:
    game_mode = input(
            '\nВыберите режим игры: 1 - игра против человека'
            '\nВыберите режим игры: 2 - игра против бота\n')
    try:
        game_mode = int(game_mode)
        if (1 <= game_mode <= 2):
            good_game_mode = True
        else:
            print('Вы ввели неверные данные, попробуйте снова"')
    except:
        print('Вы ввели неверные данные, попробуйте снова"')


row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

print(f'{row1}\n{row2}\n{row3}')

if (game_mode == 1):

    while not end_game(row1,row2,row3):
        player_turn(1,row1,row2, row3)
        print(f'{row1}\n{row2}\n{row3}')
        if not end_game(row1,row2,row3):
            player_turn(2,row1,row2, row3)
            print(f'{row1}\n{row2}\n{row3}')

else:

    while not end_game(row1,row2,row3):
        player_turn(1,row1,row2, row3)
        print(f'{row1}\n{row2}\n{row3}')
        if not end_game(row1,row2,row3):
            cpu_turn(row1,row2, row3)
            print(f'{row1}\n{row2}\n{row3}')

print('Конец игры!')