class NewList:
    def __init__(self, *args):
        self.list = list(*args)

    @staticmethod
    def item_type(lst):
        # проверяем является переданные данные списком или объектом класса
        lst = lst.list if isinstance(lst, NewList) else lst
        # и конвертируем в список
        return list(zip(lst, map(type, lst)))
        # конвертируем список в кортеж типа значение/тип данных

    def result(self, left, right):
        left = self.item_type(left)
        right = self.item_type(right)
        for el in right:
            if el in left:
                # тут ищем, есть ли в левом списке значение из правого
                left.remove(el)
                # и если находим, то удаляем из левого
        left = [x[0] for x in left]
        # возвращаем список значений левого списка
        return left

    def __sub__(self, other):
        return NewList(self.result(self, other))

    def __rsub__(self, other):
        return NewList(self.result(other, self))

    def __isub__(self, other):
        self.list = self.result(self, other)
        return self

    def get_list(self):
        return self.list


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst1 - [0, True]  # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print(res_1.get_list())
print(res_2.get_list())
print(res_3.get_list())
print(res_4.get_list())
