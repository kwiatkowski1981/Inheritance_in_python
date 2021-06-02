try:
    number1 = int(input('number 1: '))
    number2 = int(input('number 2: '))
    result = number2 / number1
    print(result)
except ValueError:
    print('podano nieprawidlowa wartosc')
except ZeroDivisionError:
    print('nie dzielimy przez zero')

