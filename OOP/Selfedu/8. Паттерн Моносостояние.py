class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    # инициализируем объект, атрибуты берём из атрибута класса __shared_attrs
    def __init__(self) -> None:
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()
# у th1 и th2 будут одинаковые атрибуты, даже если мы поменем в одном
# экземпляре значение, то в другом оно тоже поменяется
th2.name = "thread_2"
th1.attr_new = 'new attr'
print(th1.__dict__, th2.__dict__, sep='\n')
del th1.attr_new
print(th1.__dict__, th2.__dict__, sep='\n')
