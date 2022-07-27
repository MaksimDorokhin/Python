# Сздайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
import func as f


def player_turn(player_num: int, candies_amount: int, game_mode: int) -> int:
    match game_mode:
        case 1:
            while True:
                try:
                    turn = int(input(f'Игрок {player_num}, берите конфеты (от 1 до 28): '))
                    if ( 1 <= turn <= 28) and (turn <= candies_amount):
                        return turn
                    else: 
                        print('Вы пытаетесь взять недопустимое кол-во конфет, попробуйте снова!')
                except: 
                    print('\nВы ввели неверные данные, попробуйте снова!')
        case 2:
            if (candies_amount >= 28):
                turn = random.randint(1,28)
                print(f'\nБот забирает {turn} конфет!')
                return turn
            else:
                turn = candies_amount
                print(f'\nБот забирает {turn} конфет!')
                return turn
        case 3:
            if (candies_amount >= 28):
                turn = candies_amount % 29
                if (turn == 0):
                    turn+=1
                print(f'\nБот забирает {turn} конфет!')
                return turn
            else:
                turn = candies_amount
                print(f'\nБот забирает {turn} конфет!')
                return turn       

        

def game(game_mode: int) -> None:
    turn = 1
    player_candies = [0, 0]
    total_candies = 2021
    player = random.randint(1,2)
    match game_mode:
        case 1: 
            print(f'\n Жеребьевкой определено, что первый ход у игрока {player}!')
        case 2: 
            if (player == 1):
                print(f'\n Жеребьевкой определено, что первый ход у Вас!')
            else: 
                print(f'\n Жеребьевкой определено, что первый ход у бота!')
        case 3: 
            if (player == 1):
                print(f'\n Жеребьевкой определено, что первый ход у Вас!')
            else: 
                print(f'\n Жеребьевкой определено, что первый ход у сверхразума!')

    while total_candies > 0:

        print(f'\nХод {turn}. \nНа столе осталось {total_candies} конфет!')

        match game_mode:
            case 1: 
                print(f'\nУ игрока 1: {player_candies[0]} конфет \nУ игрока 2: {player_candies[1]} конфет')
            case 2: 
                print(f'\nУ Вас: {player_candies[0]} конфет \nУ бота: {player_candies[1]} конфет')
            case 3: 
                print(f'\nУ Вас: {player_candies[0]} конфет \nУ сверхразума: {player_candies[1]} конфет')

        if (player == 1):
            candies = player_turn(1, total_candies, game_mode = 1)
            player_candies[0] += candies
            total_candies -= candies
            player = 2
        else: 
            match game_mode:
                case 1:
                    candies = player_turn(2, total_candies, game_mode = 1)
                case 2:
                    candies = player_turn(2, total_candies, game_mode = 2)
                case 3:
                    candies = player_turn(2, total_candies, game_mode = 3)
            player_candies[1] += candies
            total_candies -= candies
            player = 1
        turn+=1

    match game_mode:
        case 1:
            if (player == 2):
                print(f'\nВыиграл игрок 1, и он забирает все конфеты!\n')
            else: 
                print(f'\nВыиграл игрок 2, и он забирает все конфеты!\n')
        case 2:
            if (player == 2):
                print(f'\nВы выиграли и забираете все конфеты!\n')
            else: 
                print(f'\nВыиграл бот, и он забирает все конфеты!\n')
        case 3:
            if (player == 2):
                print(f'\nВы выиграли и забираете все конфеты!\n')
            else: 
                print(f'\nВыиграл сверхразум, и он забирает все конфеты!\n')


    
print(f'\nДобро пожаловать в игру 2021 конфета!'
        '\nВыберите режим игры:'
        '\n1: Игра против человека'
        '\n2: Игра против бота'
        '\n3: Игра против сверхразума')
check_select = False
while not check_select:
    select_mode = input(f'\nВведите номер режима: ')
    match select_mode:
        case '1': 
            print(f'Выбрана игра против человека!')
            game(int(select_mode))
            check_select = True
        case '2': 
            print(f'Выбрана игра против бота!')
            game(int(select_mode))
            check_select = True
        case '3': 
            print(f'Выбрана игра против сверхразума!')
            game(int(select_mode))
            check_select = True
    if (select_mode != '1') and (select_mode != '2') and (select_mode != '3'):
        print('\nВы ввели неверные данные, попробуйте снова!')