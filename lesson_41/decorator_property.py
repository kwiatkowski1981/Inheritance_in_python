class Product:
    def __init__(self, price):
        self.price = price
        self._discount = 0.1

    @property
    def discounted_price(self):
        return self.price - self.price * self._discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, new_discount):
        if 0 < new_discount < 1:
            self._discount = new_discount

    @discount.deleter
    def discount(self):
        self._discount = 0


car = Product(1_000)
print(car.discounted_price)
car.discount = 0.2
print(car.discounted_price)
car.discount = 0.05
print(car.discounted_price)
del car.discount
print(car.discounted_price)
