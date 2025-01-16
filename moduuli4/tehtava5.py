i = 0
while i < 5:
    tunnus = input("Käyttäjätunnus: ")
    ssana = input("Salasana: ")

    if tunnus == "python" and ssana == "rules":
        break
    
    i += 1

print(f"Tervetuloa" if i < 5 else "Pääsy evätty")