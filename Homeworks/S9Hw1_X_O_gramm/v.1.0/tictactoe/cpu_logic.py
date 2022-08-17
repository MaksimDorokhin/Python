from random import randint


def cpu_turn(cpu_id: str, turns: list) -> list:
    ready = True if " " in turns else False
    while ready:
        turn = randint(0, 8)
        if turns[turn] == " ":
            turns[turn] = cpu_id
            return turns
