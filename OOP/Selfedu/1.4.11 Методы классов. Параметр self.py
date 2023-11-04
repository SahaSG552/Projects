class Translator:
    """
    перевод с английского на русский
    метод add добавляет слово-перевод в словарь
    если слово есть в словаре, а перевод другой,
    то дополняем список переводов
    метод remove удаляет слово-перевод
    метод translate возвращает список русских
    значений
    """

    def add(self, eng, rus):
        if "tr" not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        self.tr.pop(eng, None)

    def translate(self, eng):
        return self.tr.get(eng, [])


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(*tr.translate("go"))
