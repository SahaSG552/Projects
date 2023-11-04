class Book:
    __title = ""
    __author = ""
    __price = 0

    def __init__(self, author: str, title: str, price: int):
        self.set_title(title)
        self.set_author(author)
        self.set_price(price)

    def set_author(self, author):
        self.__author = author

    def set_title(self, title):
        self.__title = title

    def set_price(self, price):
        self.__price = price

    def get_author(self):
        return self.__author

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price


book = Book("автор", "название", 25)
print(book.get_title())
