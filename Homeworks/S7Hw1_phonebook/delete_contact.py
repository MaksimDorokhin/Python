from csv_linereader import csv_linereader as csvl
from pathlib import Path

def delete_contact() -> None:

    search_results = list()
    contact_search = input('\nВведите значение для поиска контактов для удаления из БД: ')
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

    confirm_delete = bool(input('\nВы действиьнльно хотите удалить найденные выше контакты?'
                                '\nДля отмены нажмите Enter'
                                '\nДля подтверждения введите любое значение и Enter\n'))
    if confirm_delete:

        new_phonebook = list()

        for contact in phonebook:

            contact_match = False

            for contact_to_delete in search_results:

                if contact == contact_to_delete:
                    contact_match = True

            if not contact_match:
                new_phonebook.append(contact)

        filepath = Path('phonebook', 'phonebook.csv')
        with open (filepath, 'w') as file:
            file.writelines(new_phonebook)