class FloatValue:
    """
    The FloatValue class is a descriptor that allows
    assigning and retrieving float values to attributes.
    It raises a TypeError if a non-float value is assigned.
    """
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) is float:
            setattr(instance, self.name, value)
        else:
            raise TypeError("Присваивать можно только вещественный тип данных.")


class Cell:
    """
    The Cell class represents a cell in a table and has a value attribute of type FloatValue.
    It initializes the value attribute with a default value of 0.0.
    """

    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    """
    The TableSheet class represents a table with a specified number of rows and columns.
    It initializes a 2D list of Cell objects as the cells attribute.
    """
    def __init__(self, rows, cols):
        self.cells = [[Cell() for _ in range(cols)] for _ in range(rows)]


# sourcery skip: use-itertools-product
table = TableSheet(5, 3)
start_value = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j].value = start_value
        start_value += 1

print(*table.cells, sep="\n")
print(table.cells[1][2].value)
