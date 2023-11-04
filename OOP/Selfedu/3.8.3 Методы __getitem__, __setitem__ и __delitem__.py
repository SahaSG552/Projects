class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__total_args = len(kwargs)
        self.__attrs = tuple(kwargs.keys())

    def __check__(self, item):
        if type(item) != int or not (-self.__total_args <= item < self.__total_args):
            raise IndexError("неверный индекс поля")

    def __getitem__(self, item):
        self.__check__(item)
        return getattr(self, self.__attrs[item])

    def __setitem__(self, key, value):
        self.__check__(key)
        setattr(self, self.__attrs[key], value)


r = Record(a="A", b="B", c="C")
print(r[0])
