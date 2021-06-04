from json import loads
from urllib.request import urlopen

country = input('Podaj kraj: ')

with urlopen(f'https://restcountries.eu/rest/v2/name/{country}') as response:
    data = loads(response.read().decode('utf-8'))
    print(data)
    country_data = data[0]
    print('Stolica', country_data['capital'])

# todo <------------------------------->    its not working yet
