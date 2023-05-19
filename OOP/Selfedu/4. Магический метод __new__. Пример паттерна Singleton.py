class Employee:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        print(f"New class named: {cls.__name__}")
        return cls.__instance

    def __del__(self):
        Employee.__instance = None

    def __init__(self, first: str, last: str, pay: int):
        print(f"New instance named: {str(self)}")
        self.first = first
        self.last = last
        self.pay = pay


emp_1 = Employee("Vasiliy", "Ignatenko", 50000)
emp_2 = Employee("Valeriy", "Legasov", 80000)
print(Employee)
print(emp_1.pay)
