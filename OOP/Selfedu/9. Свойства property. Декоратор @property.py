class Param:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old


p = Param("semen", "sperm")
p.old = 35
print(p.old, p.__dict__)
