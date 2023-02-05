class Wizard:
    def __init__(self, name, surname):
        if not name:
            raise ValueError("Missing name")
        if not surname:
            raise ValueError("Missing surname")
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"


class Student(Wizard):
    def __init__(self, name, surname, house):
        super().__init__(name, surname)
        self.house = house


class Teacher(Wizard):
    def __init__(self, name, surname, subject):
        super().__init__(name, surname)
        self.subject = subject


wizard = Wizard("Albus", "Dumbledor")
student = Student("Harry", "Potter", "Gryffindor")
teacher = Teacher("Severus", "Snape", "Defence against the dark art")
teacher = Teacher("Minerva", "McGonagall", "Transfiguration")

print(
    f"{student.name} {student.surname} is student of {student.house}.\n"
    f"His teacher on subject {teacher.subject} is {teacher.name} {teacher.surname}.\n"
    f"His master is {wizard.name} {wizard.surname}."
)
