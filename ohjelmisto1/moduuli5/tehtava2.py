luvut = []

while True:
    syote = input("Anna luku: ")

    if syote == "":
        break
    luvut.append(int(syote))

luvut.sort(reverse=True)

for i in luvut[0:5]:
    print(i)