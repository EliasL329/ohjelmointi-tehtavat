from random import randint

class Auto():
    def __init__(self, tunnus: str, huippunopeus: int):
        self.tunnus = tunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, maara: int):
        self.nopeus += maara

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit: float):
        self.kuljettu_matka += self.nopeus * tunnit

def main():
    autot = [Auto(f"ABC-{i}", randint(100, 200)) for i in range(1, 11)]

    i = True
    while i:
        for auto in autot:
            auto.kiihdyta(randint(-10, 15))
            auto.kulje(1)

            if auto.kuljettu_matka >= 10000:
                i = False
                
    def key(auto):
        return auto.kuljettu_matka
    autot.sort(reverse=True, key=key)

    for auto in autot:
        print(f"Tunnus: {auto.tunnus:6} | Huippunopeus: {auto.huippunopeus:3}km/h | Nopeus: {auto.nopeus:3}km/h | Kuljettu matka: {auto.kuljettu_matka}km")

main()