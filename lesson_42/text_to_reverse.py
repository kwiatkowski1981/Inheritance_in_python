content = input('Podaj tekst do odwrucenia: ')
try:
    if content == '':
        raise ValueError('Tekst nie zostal podany.')
    print(content[::-1])
except ValueError as error:
    print(error)
