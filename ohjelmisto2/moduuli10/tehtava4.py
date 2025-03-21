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

class Kilpailu():
    def __init__(self, nimi: str, pituus: int, autot: list):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tuntiKuluu(self):
        for auto in self.autot:
            auto.kiihdyta(randint(-10, 15))
            auto.kulje(1)

    def tulostaTilanne(self):
        def key(auto):
            return auto.kuljettu_matka
        self.autot.sort(reverse=True, key=key)
        
        for auto in self.autot:
            print(f"Tunnus: {auto.tunnus:6} | Huippunopeus: {auto.huippunopeus:3}km/h | Nopeus: {auto.nopeus:3}km/h | Kuljettu matka: {auto.kuljettu_matka}km")
        print()

    def kilpailuOhi(self):
        i = True
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                i = False
        return i

        

def main():
    kilpailu = Kilpailu("Suuri romuralli", 8000, [Auto(f"ABC-{i}", randint(100, 200)) for i in range(1, 11)])
    
    i = True
    tunti = 0
    while i:
        kilpailu.tuntiKuluu()
        tunti += 1

        i = kilpailu.kilpailuOhi()

        if tunti % 10 == 0:
            kilpailu.tulostaTilanne()
    kilpailu.tulostaTilanne()

main()