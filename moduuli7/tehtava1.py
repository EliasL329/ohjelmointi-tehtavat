sanakirja = {"kevät": (1, 2, 3), "kesä": (4, 5, 6), "syksy": (7, 8, 9), "talvi": (10, 11, 12)}

kuukausi = int(input("Syötä kuukauden numero: "))

for avain in sanakirja:
    for i in sanakirja[avain]:
        if i == kuukausi:
            print(avain)