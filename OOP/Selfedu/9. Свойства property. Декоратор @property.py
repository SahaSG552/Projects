class Param:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old


p = Param("semen", "sperm")
p.old = 35
print(p.old, p.__dict__)


class Car:
    "This class is for car properties such as wheel diameter and capacity"

    def __init__(self, wheel_diameter: int = 0, capacity: int = 0):
        self.__wheel_diameter = wheel_diameter
        self.__capacity = capacity

    @property
    def capacity_getter(self):
        return self.__capacity

    def capacity_setter(self, capacity):
        self.__capacity = capacity

    def __setattr__(self, __name: str, __value) -> None:
        if __name == "__wheel_diameter":
            raise AttributeError(
                f"This property name is restricted! ({__name})"
            )
        else:
            object.__setattr__(self, __name, __value)


car_1 = Car(15, 25)
# car_1.__wheel_diameter = 35
car_1.capacity_setter(55)
print(car_1.capacity_getter, car_1.__dict__, Car.__dict__, sep="\n")
