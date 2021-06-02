capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin'
}
try:
    country = input('Podaj nazwę państwa żeby dowiedzieć się jaką ma stolicę: ')
    print(f'{country}: {capitals[country]}')
except KeyError:
    print(f'nie wiem jaka jest stolica panstwa {country}')

