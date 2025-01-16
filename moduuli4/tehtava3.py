lista = []

while True:
    luku = input("Anna luku: ")
    
    if luku == "":
        print(f"Saaduista luvuista suurin on {max(lista)} ja pienin on {min(lista)}")
        break

    if int(luku):
        lista.append(luku)