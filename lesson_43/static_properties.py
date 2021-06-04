class Student:
    NEXT_ID = 0

    def __init__(self, first_name: str, last_name: str):
        self.id = Student.NEXT_ID
        self.first_name = first_name
        self.last_name = last_name
        Student.NEXT_ID += 1

    def hello(self):
        return f'{self.id}. {self.first_name} {self.last_name}'


marek = Student('Marek', 'Duda')
karol = Student('Karol', 'Dupa')
print(marek)
print(marek.hello())
print(karol.hello())
print(marek.id)
