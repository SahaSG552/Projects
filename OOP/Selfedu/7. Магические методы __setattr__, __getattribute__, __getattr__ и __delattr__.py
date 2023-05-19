class Point:
    MAX_COORD = 70
    MIN_COORD = 0

    def __init__(self, x, y,):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    def __getattribute__(self, attr):
        if attr == "x":
            raise ValueError("Доступ запрещен")
        else:
            return object.__getattribute__(self, attr)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError(f'"{key}" - Недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)
            # self.__dict__[key] = value

    def __getattr__(self, attr):
        # print("__getattr__" + attr)
        return False

    def __delattr__(self, attr):
        print(f'{attr} deleted')
        object.__delattr__(self, attr)


pt1 = Point(0, 50)
del pt1.x
print(pt1.__dict__)
