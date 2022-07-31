from add_contact import add_contact
from search_contact import search_contact
from delete_contact import delete_contact

def run_phonebook() -> None:

    print('\nДобро пожаловать в телефонную книгу!')
    while True:
        good_action = False
        while not good_action:
            action = input('\nВыберите нужное действие:'
            '\n1 - Добавить контакт в книгу'
            '\n2 - Найти и показать контакт по заданному значению'
            '\n3 - Удалить контакт из книги'
            '\n4 - Выход\n\n')
            if action.isdigit():
                action = int(action)
                if (1 <= action <= 4):
                    good_action = True
                else:
                    print('Для выбора действия ввведите число от 1 до 3-х!')
            else:
                print('Для выбора действия ввведите число от 1 до 3-х!')

        match action:
            case 1: add_contact()
            case 2: search_contact()
            case 3: delete_contact()
            case 4: exit()