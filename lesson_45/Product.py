class Product:
    def __init__(self, price: float):
        self.price = price

    def calculate_netto(self):
        return self.price

    def calculate_brutto(self):
        return self.price * 1.23



