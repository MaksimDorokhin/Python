from csv_linereader import csv_linereader as csvl

def search_contact() -> None:
   
    search_results = list()
    contact_search = input('\nВведите значение для поиска в БД: ')
    phonebook = csvl(path = "phonebook", filename = "phonebook.csv")
   
    for contact_line in phonebook:
        if contact_search in contact_line:
            search_results.append(contact_line)

    if search_results == []:
        print('Ничего не найдено!')
    else:
        for result in search_results:
            result_list = result.split(';')
            print(f'\nФамилия: {result_list[0]} '
            f'Имя: {result_list[1]} '
            f'Отчество: {result_list[2]} '
            f'Телефон: {result_list[3]} '
            f'Описание: {result_list[4]}')
