from csv_writer import csv_writer as csv

def add_contact() -> None:
    surname = input('\nФамилия: ')
    csv(field = surname + ';', path = "phonebook", filename = "phonebook.csv")
    name = input('\nИмя: ')
    csv(field = name + ';', path = "phonebook", filename = "phonebook.csv")
    middlename = input('\nОтчество: ')
    csv(field = middlename + ';', path = "phonebook", filename = "phonebook.csv")
    phone = input('\nТелефон: ')
    csv(field = phone + ';', path = "phonebook", filename = "phonebook.csv")
    description = input('\nОписание: ')
    csv(field = description + ';', path = "phonebook", filename = "phonebook.csv")
    csv(field = '\n', path = "phonebook", filename = "phonebook.csv")
    
    