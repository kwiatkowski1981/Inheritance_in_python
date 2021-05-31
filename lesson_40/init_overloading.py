class Person:
    def __init__(self, first_name: str, last_name: str):
        self.details = f'{first_name} {last_name}'


class Student(Person):
    def __init__(self, first_name: str, last_name: str, semester: int):
        super().__init__(first_name, last_name)
        self.semester = semester


jan = Student('Jan', 'Kowalski', 2)
print(jan.details)
print(jan.semester)
