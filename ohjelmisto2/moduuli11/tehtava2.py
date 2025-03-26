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

class SahkoAuto(Auto):
    def __init__(self, tunnus, huippunopeus, akkuKapasiteetti):
        super().__init__(tunnus, huippunopeus)
        self.akkuKapasiteetti = akkuKapasiteetti

class PolttomoottoriAuto(Auto):
    def __init__(self, tunnus, huippunopeus, bensaKapasiteetti):
        super().__init__(tunnus, huippunopeus)
        self.bensaKapasiteetti = bensaKapasiteetti

def main():
    auto1 = SahkoAuto("ABC-15", 180, 52.5)
    auto2 = PolttomoottoriAuto("ACD-123", 165, 32.3)

    auto1.kiihdyta(100)
    auto2.kiihdyta(110)

    auto1.kulje(3)
    auto2.kulje(3)

    print(auto1.kuljettu_matka, auto2.kuljettu_matka)

main()