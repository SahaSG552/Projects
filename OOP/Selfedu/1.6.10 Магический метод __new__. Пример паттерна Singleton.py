class Point:

    def __init__(self, x=0, y=0,):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)


pt = Point(1, 5)
print(pt, pt.__dict__)
pt_clone = pt.clone()
print(pt_clone, pt_clone.__dict__)
pt_clone.x = 5
pt_clone.y = 1
print(pt_clone, pt_clone.__dict__)
