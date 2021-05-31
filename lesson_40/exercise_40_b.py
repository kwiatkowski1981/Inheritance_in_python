class Employee:
    def __init__(self, first_name: str, last_name: str, rate_per_hour: float):
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self._time_spent = 0

    def add_time(self, time: float):
        self._time_spent += time

    def pay(self):
        return self._time_spent * self.rate_per_hour


class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, rate_per_hour: float):
        super().__init__(first_name, last_name, rate_per_hour)
        self.bonus = 0

    def add_bonus(self, bonus):
        self.bonus += bonus

    def pay(self):
        return super().pay() * 2 + self.bonus


manager = Manager('Fred', 'Flinston', 100)
manager.add_time(3)
manager.add_bonus(500)
print(manager.pay())

employee = Employee('Marek', 'Niedzwiedzki', 15)
employee.add_time(168)
print(employee.pay())
