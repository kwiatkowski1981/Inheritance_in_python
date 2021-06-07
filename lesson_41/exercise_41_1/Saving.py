from datetime import datetime


class Saving:
    def __init__(self, amount: float, date: datetime = datetime.now()):
        self._date = date
        self._amount = amount

    @property
    def date(self):
        return self._date.strftime('%d.%m.%Y %H:%M:%S')

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        if new_amount > 0:
            self._amount = new_amount

    @amount.deleter
    def amount(self):
        self._amount = 0

    def get_saving(self):
        return {self._date: self._amount}
