def game_win(player_id: str, turns: list) -> bool:
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    player_combinations = list()

    for i in range(0, len(turns)):
        if turns[i] == player_id:
            player_combinations.append(i)

    for i in win_combinations:
        if set(i).issubset(player_combinations):
            return True
