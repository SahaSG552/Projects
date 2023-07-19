class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


p1 = Person("Vasya", 70)
p1.old = 60
p1.name = "Petya"
print(f"{p1.name} is getting {p1.old} this year")
