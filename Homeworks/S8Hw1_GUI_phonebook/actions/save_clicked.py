from .csv_writer import csv_writer as csv
from tkinter import messagebox

def save_clicked(*args: str) -> None: 
    all_empty = True 

    for item in args:
        if (item != ''):
            all_empty = False

    if not all_empty:
        for item in args:
            csv(field = item + ';', path = "phonebook", filename = "phonebook.csv")
        csv(field = '\n', path = "phonebook", filename = "phonebook.csv")
        messagebox.showinfo('Сохранение', 'Сохранение успешно выполнено!')
    else:
        messagebox.showinfo('Сохранение', 'Не введено ни одно поле для сохранения!')
