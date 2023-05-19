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
        self.pay = int(int(self.pay) * self.raise_amount)

    def __add__(self, other):
        return self.pay + other.pay

    def __repr__(self) -> str:
        return f'{self.get_classname()} {self.fullname()} {self.pay}'

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        args = emp_str.split("-")
        return cls(*args)

    @classmethod
    def get_classname(cls):
        return cls.__name__

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay,)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay,)
        self.employees = [] if employees is None else employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"---> {emp.fullname()}")


emp_1 = Employee("Creed", "Bratton", 50000)
emp_2 = Employee("Andrew", "Bernard", 50000)
emp_3 = Employee.from_string("Stanley-Huddson-1000")
dev_1 = Developer.from_string("Meredith-Palmer-70000-Python")
man_1 = Manager('Angela', 'Martin', 40000, [emp_1])
man_1.add_emp(emp_2)
man_1.add_emp(dev_1)
man_1.remove_emp(emp_2)
print(*list(man_1.__dict__.items()), sep="\n")
man_1.print_emps()

print(man_1)