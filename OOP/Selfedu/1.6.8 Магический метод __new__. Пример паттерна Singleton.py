class SingletonFive:
    __counter = 0
    __fifth_class = None

    def __new__(cls, *args, **kwargs):
        cls.__counter += 1
        if cls.__counter < 6:
            cls.__fifth_class = super().__new__(cls)
        return cls.__fifth_class

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
print(*[(id(o), hasattr(o, "name")) for o in objs], sep="\n")
