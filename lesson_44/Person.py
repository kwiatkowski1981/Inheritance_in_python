from csv import reader


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_row(cls, row: str):
        # strip(usuwa biale znaki), split(rozdziela po tym co ustawie)
        first_name, last_name = row.strip().split(";")
        return cls(first_name, last_name)


person = Person.from_row(' Jakub;Kwiatkowski       ')  # dodalem biale znaki, zostana usuniete w funkcji
print(f'{person.first_name} {person.last_name}')
