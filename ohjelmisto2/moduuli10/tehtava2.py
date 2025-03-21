from random import randint

class Hissi():
    def __init__(self, alinKerros, ylinKerros):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.kerros = alinKerros
    
    def kerrosYlos(self):
        self.kerros += 1
    
    def kerrosAlas(self):
        self.kerros -= 1

    def siirryKerrokseen(self, kerros):
        while self.kerros != kerros:
            self.kerrosAlas() if self.kerros > kerros else self.kerrosYlos()

class Talo():
    def __init__(self, hissiMaara: int, alinKerros: int, ylinKerros: int):
        self.hissiMaara = hissiMaara
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.hissit = [Hissi(0, randint(1, ylinKerros)) for i in range(hissiMaara)]

    def ajaHissia(self, hissiNro: int, kohdeKerros: int):
        self.hissit[hissiNro].siirryKerrokseen(kohdeKerros)
    
def main():
    talo = Talo(10, 0, 10)
    print(talo.hissit[0].kerros)

    talo.ajaHissia(0, 9)
    print(talo.hissit[0].kerros)

main()