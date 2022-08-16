class Book():
    def __init__(self, age: int = 0, author: str = 'Author', name: str = 'Book'):
        self.age = age
        self.author = author
        self.name = name

    def open_book(self, mes: str = 'Hello'):
        print(mes)


my_book1 = Book(author='New', name='OOP')

print(my_book1.age)
