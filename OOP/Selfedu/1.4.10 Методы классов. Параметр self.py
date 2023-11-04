lst_in = ["1 Mathew 35 2500", "2 Semen 25 3500", "3 Vasily 45 1500"]


class DataBase:
    lst_data = []
    FIELDS = ("id", "name", "old", "salary")

    # здесь добавлять методы
    def insert(self, data):
        for d in data:
            self.lst_data.append(dict(zip(self.FIELDS, d.split())))

    def select(self, a, b):
        return self.lst_data[a: b + 1]


db = DataBase()
db.insert(lst_in)
print(db.lst_data)
print(db.select(0, 5))
