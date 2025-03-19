class Auto():
    def __init__(self, tunnus, huippunopeus):
        self.tunnus = tunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

def main():
    uusiAuto = Auto("ABC-123", 142)
    print(uusiAuto.tunnus, uusiAuto.huippunopeus, "km/h", uusiAuto.nopeus, "km/h", uusiAuto.kuljettu_matka)

main()