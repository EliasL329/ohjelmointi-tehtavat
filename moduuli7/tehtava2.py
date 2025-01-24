nimilista = set()

while True:
    nimi = input("Syötä nimi: ")

    if nimi == "":
        break

    if nimi not in nimilista:
        nimilista.add(nimi)
        print("Uusi nimi")

    else:
        print("Aiemmin syötetty nimi")

for i in nimilista:
    print(i)