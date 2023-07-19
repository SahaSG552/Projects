class WindowDlg:
    __title = ""
    __width = 0
    __height = 0

    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width != self.__width and self.check_value(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height != self.__height and self.check_value(height):
            self.__height = height
            self.show()

    @staticmethod
    def check_value(value):
        return type(value) is int and value in list(range(10000))


wnd = WindowDlg("заголовок окна", 600, 500)
wnd.show()
wnd.height = 300
wnd.width = 300
