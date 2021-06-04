class ValueToSmall(Exception):
    pass


class ValueToBig(Exception):
    pass


try:
    value = int(input('Podaj liczbę: '))
    if value < 10:
        raise ValueToSmall()
    if value > 20:
        raise ValueToBig()
    print(value)
except (ValueToSmall, ValueToBig) as error:
    print(error)

