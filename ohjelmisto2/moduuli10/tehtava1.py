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
    
h = Hissi(0, 10)
print(h.kerros)

h.siirryKerrokseen(5)
print(h.kerros)

h.siirryKerrokseen(h.alinKerros)
print(h.kerros)