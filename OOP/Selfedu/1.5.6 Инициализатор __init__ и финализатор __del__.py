# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = (a, b, c)

    def is_triangle(self):
        for side in self.sides:
            if type(side) not in (float, int) or side <= 0:
                return 1
            elif sum(self.sides) - side <= side:
                return 2
        return 3


a, b, c = map(int, input().split())  # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker
# и вызовите метод is_triangle() с выводом информации на экран
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
