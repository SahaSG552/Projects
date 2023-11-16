class Point:
    MAX_COORD = 70
    MIN_COORD = 0

    def __init__(self, x, y,):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    # для того, чтобы изменить аттрибуты класса нужно написать
    # декоратор @classmethod и ссылаться не на self (экземпляр объекта),
    # а на сам класс cls
    # если сослаться на self, то будем менять аттрибут
    # в конкретном экземпляре объекта
    def set_bound(cls, left):
        cls.MIN_COORD = left

    def __getattribute__(self, attr):  
        # автоматически вызывается при получении свойства класса с именем attr
        if attr == "x":
            raise ValueError("Доступ запрещен")
        else:
            return object.__getattribute__(self, attr)

    def __setattr__(self, key, value):
        # автоматически вызывается при изменении свойства класса key
        if key == "z":  # запрещаем создавать аргумент с именем Z
            raise AttributeError(f'"{key}" - Недопустимое имя атрибута')
            # выводим ошибку
        else:
            object.__setattr__(self, key, value)  # создание аргумента
            # self.__dict__[key] = value

    def __getattr__(self, attr):
        # автоматически вызывается при получении
        # несуществующего свойства класса с именем attr
        # print("__getattr__" + attr)
        return False
        # если идёт обращение к несуществующему аргументу, то получим False

    def __delattr__(self, attr):
        # автоматически вызывается при удалении свойства
        # класса с именем attr (не важно существует оно или нет)
        print(f'{attr} deleted')  # когда удаляем аргумент - выводим сообщение
        object.__delattr__(self, attr)  # непосредственное удаление


pt1 = Point(0, 50)
del pt1.x
pt1.__setattr__('x', 20)

print(pt1.yy)
print(pt1.__getattribute__("y"))
print(pt1.__dict__)
print(Point.__dict__)
