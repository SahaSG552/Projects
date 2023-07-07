from random import choice, randrange


class Elem:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Line(Elem):
    pass


class Rect(Elem):
    pass


class Ellipse(Elem):
    pass


objects = (Line, Rect, Ellipse)
elements = []

elements.extend(
    choice(objects)(*[randrange(10) for _ in range(4)])
    for _ in range(217)
)


for el in elements:
    if isinstance(el, Line):
        el.sp = el.ep = (0, 0)

# print(*[el.__dict__ for el in elements], sep="\n")
[print(type(el).__name__, el.__dict__) for el in elements]
