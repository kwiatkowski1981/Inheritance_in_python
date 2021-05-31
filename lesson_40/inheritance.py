class User:
    def login(self):
        return 'Jestem zalogowany!'


class Teacher(User):
    def run(self):
        return 'Nauczam..'


class Student(User):
    def run(self):
        return 'Studiuję.........'


johny = Student()
print('Johny said: ')
print(johny.login())
print(johny.run())
aghata = Teacher()
print('Aghata said: ')
print(aghata.login())
print(aghata.run())
