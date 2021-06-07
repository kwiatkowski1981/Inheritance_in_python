from datetime import datetime


class Booking:
    def __init__(self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date

    def get_difference(self):
        difference = self.end_date - self.start_date

        return difference.days + 1  # liczy nie wliczajac ost dnia cos jak range(1, 7)
