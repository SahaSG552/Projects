class Book:
    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if (
            key in ["title", "author"] and type(value) is not str
            or key in ["pages", "year"] and type(value) is not int
        ):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)


book = Book("0", "1", 2, 2023)
book.author = "Васёчек"
print(*[f"{k}: {str(v)}" for k, v in book.__dict__.items()], sep="\n")
