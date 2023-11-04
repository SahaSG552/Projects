class FRange:
    def __init__(self, strt=0.0, nd=0.0, stp=1.0):
        self.strt = strt
        self.nd = nd
        self.stp = stp
        self.vl = self.strt - self.stp

    def __next__(self):
        if self.vl + self.stp == self.nd:
            raise StopIteration
        self.vl += self.stp
        return self.vl

    def __iter__(self):
        self.vl = self.strt - self.stp
        return self


f = FRange(0, 2, 0.5)
for i in f:
    print(i)
