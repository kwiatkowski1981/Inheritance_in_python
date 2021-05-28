class Adress:
    def __init__(self, home_number: str, street: str, city: str, postal_code: str):
        self.home_number = home_number
        self._street = street
        self._city = city
        self._postal_code = postal_code

    def get_home_number(self):
        return self.home_number

    def get_street(self):
        return self._street

    def get_city(self):
        return self._city

    def get_postal_code(self):
        return self._postal_code


class Person:
    def __init__(self, first_name: str, last_name: str, age: int, adress: Adress, pesel: str):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._adress = adress
        self._pesel = pesel

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_age(self):
        return self._age

    def get_adress(self):
        return self._adress

    def get_pesel(self):
        return self._pesel


class BankAccount:
    def __init__(self, person: Person, account_balance: float):
        self._person = person
        self._account_balance = account_balance

    def get_person(self):
        return f"pesel: {self._person.get_pesel()} - {self._person.get_first_name()} {self._person.get_last_name()}," \
               f" {self._person.get_age()}yo. \n" \
               f"{self._person.get_adress().get_street()} {self._person.get_adress().get_home_number()}, " \
               f"{self._person.get_adress().get_city()} (PLZ: {self._person.get_adress().get_postal_code()})"

    def get_account_balance(self):
        return f"{self._account_balance} Pln."

    def deposit(self):
        deposit_amount = float(input('Proszę podać ilość środków do wpłaty: '))
        self._account_balance += deposit_amount
        return self._account_balance

    def withdraw(self):
        withdraw_amount = float(input('Proszę podać ilość środków do wypłaty: '))
        if withdraw_amount > self._account_balance:
            print('Zamało środków na koncie żeby dokonać wypłaty.')
        elif withdraw_amount == self._account_balance:
            print('Twoje konto zostanie wyzerowane. Po dokonaniu wypłaty konto będzie puste.')
            print('Jeśli konto będzie puste między ostatnim tygodniem roku, pierwszym dniem nowego roku,'
                  ' konto zostanie zamknięte.')
        elif withdraw_amount < self._account_balance:
            self._account_balance -= withdraw_amount
            print(f"Wypłacam: {withdraw_amount}")
            print(f"Obecny stan konta po wypłacie: {self.get_account_balance()}")
            return self._account_balance


class SavingsAccount(BankAccount):
    def __init__(self, person: Person, account_balance: float, annual_interest: float):
        super().__init__(person, account_balance)
        self.annual_interest = annual_interest

    def get_person(self):
        return super().get_person()

    def get_account_balance(self):
        return super().get_account_balance()

    def deposit(self):
        return super().deposit()

    def withdraw(self):
        return super().withdraw()


adress_adam = Adress('43.a', 'Longstreet', 'Zurich', '8000')
adam = Person('Adam', 'Nowak', 40, adress_adam, '01018132589')

account1 = BankAccount(adam, 10_000.0)

print(account1.get_person())
print(account1.get_account_balance())

savings_account = SavingsAccount(adam, 500_000.0, 3.5)
print(savings_account.get_person())
print(savings_account.get_account_balance())
print('\n')

# account1.deposit()
# account1.get_account_balance()

print(account1.get_person())
print(account1.get_account_balance())

account1.withdraw()
