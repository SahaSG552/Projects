class StackObj:
    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, StackObj) or value is None:
            self.__next = value


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj

        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        temp = self.top
        if temp is None:
            return
        while temp and temp.next != self.last:
            temp = temp.next
        if temp:
            temp.next = None
        last = self.last
        self.last = temp
        if self.last is None:
            self.top = None
        return last

    def get_data(self):
        data_list = []
        temp = self.top
        while temp:
            data_list.append(temp.data)
            temp = temp.next
        return data_list


obj = StackObj(1)
obj2 = StackObj(2)
obj3 = StackObj(3)
obj2.next = obj3
obj3.next = obj
st = Stack()
st.get_data()
