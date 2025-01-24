lentokentat = {}

def tallenna():
    nimi = input("Syötä lentokentän nimi: ")
    koodi = input("Syötä lentokentän ICAO koodi: ")
    
    if koodi not in lentokentat:
        lentokentat[koodi] = nimi

def haku():
    koodi = input("Syötä lentokentän ICAO koodi: ")
    
    if koodi in lentokentat:
        print(lentokentat[koodi])
    
    else:
        print("Lentokenttää ei löytynyt")

def main():
    print("Valitse komento syöttämällä numeron:\n 1: Tallenna lentokenttä\n 2: Hae lentokenttää\n 3: Lopeta ohjelma\n")

    while True:
        komento = int(input("Komento: "))

        if komento == 1:
            tallenna()
        elif komento == 2:
            haku()
        elif komento == 3:
            break

main()