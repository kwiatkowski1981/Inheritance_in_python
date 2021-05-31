class Employee:
    def __init__(self, first_name: str, last_name: str, rate_per_hour: float):
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour


class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, rate_per_hour: float, bonus: float):
        super().__init__(first_name, last_name, rate_per_hour)
        self.bonus = bonus
