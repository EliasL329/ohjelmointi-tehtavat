from random import randint
kuutio_maara = int(input("Arpakuutioiden määrä: "))
summa = 0

for i in range(kuutio_maara):
    summa += randint(1, 6)

print("Arpakuutioiden summa:", + summa)