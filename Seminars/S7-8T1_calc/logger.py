from pathlib import Path
from datetime import datetime as dt
from time import time

def logger(data: str) -> None:
    time = dt.now().strftime('%D - %H:%M')
    filepath = Path('log', 'log.csv')
    with open (filepath, 'a') as file:
        file.write(time + ';'+ data + ';\n')