from .csv_linereader import csv_linereader as csvl
from .get_items import getItemsPerLine
from tkinter import messagebox

def search_clicked(info_txt, *args: str) -> None:
    all_empty = True 

    for item in args:
        if (item != ''):
            all_empty = False

    search_results = list()

    if not all_empty:
        phonebook = csvl(path = "phonebook", filename = "phonebook.csv")
    
        for contact_line in phonebook:
            found = False
            for contact_search in args:
                if contact_search in contact_line and (contact_search != '') and not found:
                    search_results.append(contact_line)
                    found = True
        if (search_results == []):
            messagebox.showinfo('Поиск', 'Контакты по заданным условиям поиска не найдены!')
    else:
        messagebox.showinfo('Поиск', 'Вы не заполнили ни одно поле для поиска!')
    
    getItemsPerLine(search_results, info_txt)   
