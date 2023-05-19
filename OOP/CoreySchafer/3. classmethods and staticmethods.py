import datetime


class Employee:
    # Class Attributes
    num_of_employees = 0  # number of employees
    raise_amount = 1.04  # payment increment in %

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}{last}@company.com"
        type(self).num_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)   

    @staticmethod
    def is_workday(day) -> bool:
        return day.weekday() < 5


emp_1 = Employee("Creed", "Bratton", 50000)
emp_2 = Employee("Andrew", "Bernard", 50000)
emp_3 = Employee.from_string("Stanley-Huddson-1000")
print(emp_3.__dict__)
# emp_1.raise_amount = 1.05
emp_1.raise_amount = 1.06
Employee.set_raise_amount(1.07)
emp_1.apply_raise()
emp_2.apply_raise()

print(Employee.num_of_employees)
print(emp_1.fullname(), emp_1.raise_amount, emp_1.pay)
print(emp_2.fullname(), emp_2.raise_amount, emp_2.pay)

my_date = datetime.date(2023, 5, 12)
print(Employee.is_workday(my_date))