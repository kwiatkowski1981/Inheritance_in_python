class Product:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


class DiscountedPrice(Product):
    def get_price(self):
        price = super().get_price()
        return price - 0.1 * price


product = DiscountedPrice(100)
print(product.get_price())
