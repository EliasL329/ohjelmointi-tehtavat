from math import pi

def pizzan_arvo(halkaisija, hinta):
    
    pinta_ala = (halkaisija / 2)**2 * pi
    return (hinta / pinta_ala)

def main():
    pizzat = {}

    for i in range(1, 3):
        halkaisija = int(input(f"Pizza {i}:n halkaisija: "))
        hinta = int(input(f"Pizza {i}:n hinta: "))

        pizzat[pizzan_arvo(halkaisija, hinta)] = i

    return print(f"Pizza {pizzat[min(pizzat)]} antaa paremman vastineen rahalle ")

main()