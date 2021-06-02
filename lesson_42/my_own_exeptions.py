while True:
    value = int(input('Podaj liczbę: '))
    if not value % 5 == 0:
        raise Exception('Liczba nie jest podzielna prze 5.')
    print(value)

