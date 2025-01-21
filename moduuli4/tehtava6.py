from random import randint

pistemaara = int(input("Arvottavien pisteiden määrä: "))

ympyran_sisalla = 0

for i in range(pistemaara):
    x = randint(-1000, 1000) / 1000
    y = randint(-1000, 1000) / 1000

    if (x**2) + (y**2) < 1:
        ympyran_sisalla += 1

likiarvo = 4*  ympyran_sisalla / pistemaara

print(likiarvo)