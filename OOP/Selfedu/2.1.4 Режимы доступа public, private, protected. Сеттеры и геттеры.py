class Clock:
    __time = 0

    def set_time(self, tm):
        if self.check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @staticmethod
    def check_time(tm):
        return type(tm) is int and 0 <= tm < 100_000


clock = Clock()
clock.set_time(4530)
print(clock.get_time())
