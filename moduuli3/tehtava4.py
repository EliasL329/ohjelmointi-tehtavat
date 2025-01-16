vuosi = int(input("Anna vuosi: "))
k_vuosi = True

if vuosi % 4 != 0:
    k_vuosi = False
if vuosi % 100 == 0:
    k_vuosi = True if vuosi % 400 == 0 else False

if k_vuosi:
    print("On karkausvuosi")
else:
    print("Ei ole karkausvuosi")