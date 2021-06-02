names = [
    "niunia",
    "dziunia",
    "sunia",
    "misio",
    "zdzisio",
    "kszysio",
    "dysio"
]

# print(names)
for id, name in enumerate(names):
    print(f"{id}. {name}")
try:
    number = int(input('Ktore imie wybierasz: '))
    print(names[number])
except IndexError:
    print('nie mam takiego imienia')
except (ValueError, TypeError) as error:
    print('do wyboru imienia podac cyfre calkowitą!')
    print(error)