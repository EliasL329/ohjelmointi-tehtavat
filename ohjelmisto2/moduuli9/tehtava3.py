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
    uusiAuto = Auto("ABC-123", 142)
    print(uusiAuto.tunnus, uusiAuto.huippunopeus, "km/h", uusiAuto.nopeus, "km/h", uusiAuto.kuljettu_matka)

    uusiAuto.kiihdyta(+30)
    uusiAuto.kiihdyta(+70)
    uusiAuto.kiihdyta(+50)
    print(uusiAuto.nopeus)

    uusiAuto.kulje(3)
    print(uusiAuto.kuljettu_matka)

main()