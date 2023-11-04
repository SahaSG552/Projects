class StreamData:

    def create(self, fields, lst_values):

        if len(fields) == len(lst_values):
            for i in range(len(fields)):
                setattr(self, fields[i], lst_values[i])
        return bool(self.__dict__)


s = StreamData()
print(s.create(("Hello", "World", "Z"), (1, 2, 3)))
print(s.__dict__)
