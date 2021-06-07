from lesson_45.Booking import Booking
from lesson_45.Product import Product
from datetime import datetime


class Reservation(Booking, Product):
    def __init__(self, price: float, start_date: datetime, end_date: datetime):
        Product.__init__(self, price)
        Booking.__init__(self, start_date, end_date)

    def calculate_total(self):
        return self.calculate_brutto() * self.get_difference()


stay = Reservation(100, datetime(2021, 6, 1), datetime(2021, 6, 7))
print(stay.calculate_total())