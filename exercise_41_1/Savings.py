from datetime import datetime
from exercise_41_1.Saving import Saving


class Savings:
    def __init__(self):
        self.savings = []

    def add_saving(self, saving: Saving):
        self.savings.append({
            'date': saving.date,
            'amount': saving.amount
        })

    def print_savings(self):
        for self.saving in self.savings:
            print(f"{self.saving['date']}: {self.saving['amount']}")

    def print_savings_as_dict_list(self):
        print(self.savings)

    def get_sum_of_all_savings(self):   # total
        # sum_of_all_savings = 0
        # for saving in self.savings:
        #     sum_of_all_savings += saving['amount']
        # return sum_of_all_savings
        return sum([saving['amount'] for saving in self.savings])


# today = datetime.now()
now1 = datetime(2021, 5, 21, 12, 50, 00)
saving1 = Saving(55.0, now1)
savings2 = Savings()
savings2.add_saving(saving1)
# savings2.print_savings()
saving2 = Saving(35.0)
savings2.add_saving(saving2)
# savings2.print_savings()
# savings2.print_savings_as_dict_list()

saving3 = Saving(3500.0)
savings2.add_saving(saving3)
savings2.print_savings()
savings2.print_savings_as_dict_list()
print(f"oszczednosci razem to: {savings2.get_sum_of_all_savings()}")
