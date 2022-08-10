from tkinter import *  
from tkinter import scrolledtext, messagebox
from .csv_linereader import csv_linereader as csvl
from pathlib import Path

def delete_clicked(info_txt: scrolledtext.ScrolledText) -> None:
    
    if (info_txt.get(1.0, END) == "\n"):
        messagebox.showinfo('Удаление', 'Сначала найдите контакты для удаления!')
    else:
        confirm_delete = messagebox.askyesno('Удаление', 'Вы действительно хотите удалить выбранные контакты?')

        if confirm_delete:
            phonebook = csvl(path = "phonebook", filename = "phonebook.csv")
            
            phonebook = [line.rstrip('\n') for line in phonebook]
            print(phonebook) 

            new_phonebook = list()
            search_results = list(info_txt.get(1.0, END).split('\n'))
            print(search_results)
            # for contact in search_results:
            #     print( f'[{contact}]')
            #     contact+=r'\n'
            #     print( f'[{contact}]')

            # print(search_results)
            for contact in phonebook:
                contact_match = False

                for contact_to_delete in search_results:

                    if contact == contact_to_delete:
                        contact_match = True

                if not contact_match:
                    new_phonebook.append(contact+'\n')

            filepath = Path('phonebook', 'phonebook.csv')
            with open (filepath, 'w') as file:
                file.writelines(new_phonebook)

