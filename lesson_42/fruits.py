fruits = []
try:
    for _ in range(0, 10):
        fruit = input('Podaj nazwe owoca: ')
        if fruit in fruits:
            raise ValueError('Ten owoc juz zostal dodany.')
        fruits.append(fruit)

except ValueError as e:
    print(e)
print(fruits)
