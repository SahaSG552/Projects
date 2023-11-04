class Car:
    __model = ""

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) == str and 1 < len(model) < 100:
            self.__model = model


car = Car()
car2 = Car()
car.model = "Toyota"
car2.model = "VAZ"

print(car.model, car2.model)
