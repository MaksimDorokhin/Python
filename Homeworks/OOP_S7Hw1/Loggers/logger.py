from datetime import datetime as dt
from pathlib import Path


def get_log(res, oper):
    dtime = dt.now()
    path = Path('Loggers/log.txt')
    with open(path, 'a', encoding='utf-8') as file:
        file.write('{};\nоперация: {}; результат: {}\n'.format(dtime, oper, res))
