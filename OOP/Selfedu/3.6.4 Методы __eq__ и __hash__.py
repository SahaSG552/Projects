class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __eq__(self, other):
        return self.w == other.w and self.h == other.h

    def __hash__(self):
        return hash((self.w, self.h))


r1 = Rect(0, 5, 200, 300)
r2 = Rect(0, 5, 200, 300)
print(r1 == r2)
print(hash(r1) == hash(r2))
