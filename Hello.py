class It:
    def __init__(self):
        self.l = list(range(1, 11))
        self.current_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_index > len(self.l) - 1:
            raise StopIteration
        value = self.l[self.current_index]
        self.current_index += 1
        return value

g = It()
print(g.__next__())
for x in g:
    print(x, end=' ')
