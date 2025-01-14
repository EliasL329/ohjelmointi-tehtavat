leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

naula += leiviska * 20
luoti += naula * 32
luoti *= 13.3
kilogramma = luoti // 1000
gramma = luoti - kilogramma * 1000

print("Massa nykymittojen mukaan:")
print(f"{kilogramma:.0f} kilogrammaa ja {gramma:.2f} grammaa")