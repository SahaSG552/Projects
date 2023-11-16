class Rectangle:
    def __init__(self, x=0, y=0):
        self.x = self.y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    # @protected
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


rect_1 = Rectangle(50, 500)
print(rect_1.get_coord())
rect_1.set_coord(1, 15)
print(rect_1.get_coord())
