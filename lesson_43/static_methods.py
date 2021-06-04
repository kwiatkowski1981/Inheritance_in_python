class Phone:
    def __init__(self, country, number):
        self.country = country
        self.number = number

    @staticmethod
    def get_code(code: str):
        codes = {
            'pl': 48,
            'de': 49,
            'ru': 7
        }
        return codes[code]

    def get_full_number(self):
        return self.get_code(self.country) + self.number


print(Phone.get_code('pl'))
