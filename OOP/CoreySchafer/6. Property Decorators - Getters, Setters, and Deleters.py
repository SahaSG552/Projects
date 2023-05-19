class Employee:
    def __new__(cls, *args, **kwargs):
        print(f"New class named: {cls.__name__}")
        return super().__new__(cls)
    
    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay


print(Employee)