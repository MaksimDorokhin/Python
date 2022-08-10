from tkinter import *  
from tkinter import scrolledtext
from actions import *

  
def main_window() -> None:
  
    window = Tk()  
    window.title("Добро пожаловать в телефонную книгу!")  
    window.geometry('650x300')  
    surname = Label(window, text="Фамилия")  
    surname.grid(column=0, row=0)  
    surname_txt = Entry(window,width=30)  
    surname_txt.grid(column=1, row=0)  

    name = Label(window, text="Имя")  
    name.grid(column=0, row=1)  
    name_txt = Entry(window,width=30)  
    name_txt.grid(column=1, row=1)  

    middlename = Label(window, text="Отчество")  
    middlename.grid(column=0, row=2)  
    middlename_txt = Entry(window,width=30)  
    middlename_txt.grid(column=1, row=2)  

    phone = Label(window, text="Телефон")  
    phone.grid(column=0, row=3)  
    phone_txt = Entry(window,width=30)  
    phone_txt.grid(column=1, row=3)  

    description = Label(window, text="Описание")  
    description.grid(column=0, row=4)  
    description_txt = Entry(window,width=30)  
    description_txt.grid(column=1, row=4) 

    save_button = Button(window, text="Сохранить", command=lambda: save_clicked(
        surname_txt.get(), name_txt.get(), middlename_txt.get(), phone_txt.get(), description_txt.get()))  
    save_button.grid(column=2, row=0)  

    info_txt = scrolledtext.ScrolledText(window, width=60, height=10)  
    info_txt.grid(column=1, row=6)

    find_button = Button(window, text="Найти",command=lambda: search_clicked(info_txt,
        surname_txt.get(), name_txt.get(), middlename_txt.get(), phone_txt.get(), description_txt.get()))  
    find_button.grid(column=0, row=6)  

    delete_button = Button(window, text="Удалить", command=lambda: delete_clicked(info_txt))  
    delete_button.grid(column=2, row=1)

    window.mainloop()

main_window()