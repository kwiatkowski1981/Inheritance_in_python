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
        return self._person

    def get_details(self):
        return f"{self.get_person().get_first_name()} {self.get_person().get_last_name()}," \
               f" {self.get_person().get_age()}yo. (pesel: {self.get_person().get_pesel()}) \n" \
               f"{self.get_person().get_adress().get_street()} {self.get_person().get_adress().get_home_number()}," \
               f" {self.get_person().get_adress().get_city()} (PLZ: {self.get_person().get_adress().get_postal_code()})"

    def get_account_balance(self):
        return self._account_balance

    def deposit(self, deposit_amount):
        self._account_balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self._account_balance:
            return
        elif withdraw_amount == self._account_balance:
            self._account_balance = 0
            return
        elif withdraw_amount < self._account_balance:
            self._account_balance -= withdraw_amount
            return withdraw_amount


class SavingsAccount(BankAccount):
    def __init__(self, person: Person, account_balance: float, annual_interest: float):
        super().__init__(person, account_balance)
        self.annual_interest = annual_interest

    def get_person(self):
        return super().get_person()

    def get_account_balance(self):
        return super().get_account_balance()

    def get_details(self):
        return super().get_details()

    def deposit(self, deposit_amount):
        super().deposit(deposit_amount)

    def withdraw(self, withdraw_amount):
        return super().withdraw(withdraw_amount)

    def accumulate(self):
        self._account_balance += (self.get_account_balance() * self.annual_interest) / 100


def test_deposit():
    # given
    adress_adam = Adress('43.a', 'Longstreet', 'Zurich', '8000')
    adam = Person('Adam', 'Nowak', 40, adress_adam, '01018132589')
    account1 = BankAccount(adam, 10_000.0)
    # when
    account1.deposit(20_000)
    # then
    assert account1.get_account_balance() == 30_000.0


def test_savings_account_deposit():
    # given
    adress_adam = Adress('43.a', 'Longstreet', 'Zurich', '8000')
    adam = Person('Adam', 'Nowak', 40, adress_adam, '01018132589')
    account2 = SavingsAccount(adam, 10_000.0, 3.5)
    # when
    account2.deposit(20_000)
    # then
    assert account2.get_account_balance() == 30_000.0


def test_withdraw():
    # given
    adress_adam = Adress('43.a', 'Longstreet', 'Zurich', '8000')
    adam = Person('Adam', 'Nowak', 40, adress_adam, '01018132589')
    account1 = BankAccount(adam, 10_000.0)
    # when
    account1.withdraw(5_000.5)
    # then
    assert account1.get_account_balance() == 4_999.5


def test_withdraw_all():
    # given
    adress_adam = Adress('43.a', 'Longstreet', 'Zurich', '8000')
    adam = Person('Adam', 'Nowak', 40, adress_adam, '01018132589')
    account1 = BankAccount(adam, 10_000.0)
    # when
    account1.withdraw(10_000)
    # then
    assert account1.get_account_balance() == 0


def test_savings_account_withdraw():
    # given
    adress_adam = Adress('43.a', 'Longstreet', 'Zurich', '8000')
    adam = Person('Adam', 'Nowak', 40, adress_adam, '01018132589')
    account2 = BankAccount(adam, 10_000.0)
    # when
    account2.withdraw(5_000.5)
    # then
    assert account2.get_account_balance() == 4_999.5


def test_savings_account_accumulate():
    # given
    adress_adam = Adress('43.a', 'Longstreet', 'Zurich', '8000')
    adam = Person('Adam', 'Nowak', 40, adress_adam, '01018132589')
    account2 = SavingsAccount(adam, 10_000.0, 3.5)
    # when
    account2.accumulate()
    # then
    assert account2.get_account_balance() == 10_350.0
