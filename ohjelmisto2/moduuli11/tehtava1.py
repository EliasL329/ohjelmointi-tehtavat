class Julkaisu():
    def __init__(self, nimi):
        self.nimi = nimi
        
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(self.nimi, self.kirjailija, self.sivumaara)

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(self.nimi, self.paatoimittaja)

def main():
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    kirja = Kirja("Hyttni n:o 6", "Rosa Liksom", 200)

    lehti.tulosta_tiedot()
    kirja.tulosta_tiedot()

main()