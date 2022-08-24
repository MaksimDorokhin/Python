import sys
from random import randint

from .game_win import game_win


def empty_indexes(board: list) -> list:
    index_list = []

    for i in range(0, len(board)):
        if (board[i] != 'X') and (board[i] != '0'):
            index_list.append(i)

    return index_list


def minimax(new_board: list, player: str, cpu_id: str, depth: int = 0):
    avail_spots = empty_indexes(new_board)

    if cpu_id == 'X':
        player_id = '0'
    else:
        player_id = 'X'

    if game_win(player_id, new_board):
        return -1000 + 10 * depth
    elif game_win(cpu_id, new_board):
        return 1000 - 10 * depth
    elif not avail_spots:
        return 0

    for i in avail_spots:

        if player == cpu_id:
            move_index = new_board[i]
            new_board[i] = cpu_id
            best_score = -sys.maxsize
            result = minimax(new_board, player_id, cpu_id, depth + 1)
            new_board[i] = move_index
            best_score = max(result, best_score)
        else:
            move_index = new_board[i]
            new_board[i] = player_id
            best_score = sys.maxsize
            result = minimax(new_board, cpu_id, cpu_id)
            new_board[i] = move_index
            best_score = min(result, best_score)

    return best_score


def cpu_turn(cpu_id: str, turns: list, cpu_mode: str = 'noob') -> list:
    if cpu_mode == 'noob':
        ready = True if ' ' in turns else False
        while ready:
            turn = randint(0, 8)
            if turns[turn] == ' ':
                turns[turn] = cpu_id
                return turns
    else:
        if cpu_id == 'X':
            player_id = '0'
        else:
            player_id = 'X'
        orig_board = turns
        avail_spots = empty_indexes(orig_board)
        best_score = -sys.maxsize
        for i in avail_spots:
            orig_board[i] = cpu_id
            score = minimax(orig_board, player_id, cpu_id)
            orig_board[i] = ' '

            if score > best_score:
                best_score = score
                max_i = i

        orig_board[max_i] = cpu_id
        return orig_board
