from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def get_total_price(self):
        pass


class Product(Item):

    def get_total_price(self):
        return self.price


# a = Item('ABC', 2.35)
