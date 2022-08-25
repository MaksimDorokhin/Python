from random import randint


def cat_dictionary() -> str:
    cat_type = ['кот', 'кошка', 'кошечка', 'котик', 'котенок']
    cat_actions = ['бежит', 'лежит', 'спит', 'охотится', 'мяукает', 'мурлычет', 'крадется']
    return f'{cat_type[randint(0, 4)]} {cat_actions[randint(0, 6)]} {randint(0, 100)}'
