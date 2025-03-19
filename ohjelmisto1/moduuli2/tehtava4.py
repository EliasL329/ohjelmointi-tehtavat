summa = 0
tulo = 1

for i in range(3):
    luku = int(input("Anna luku: "))

    summa += luku
    tulo *= luku

print(f"Summa: {summa}, Tulo: {tulo}, Keskiarvo: {summa / 3}")