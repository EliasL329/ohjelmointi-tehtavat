from random import randint

luku = randint(1, 10)
print("Anna luku väliltä 1 - 10")

while True:
    arvaus = int(input())

    if arvaus < luku:
        print("Liian pieni arvaus")
    elif arvaus > luku:
        print("Liian suuri arvaus")
    else:
        print("Oikein!")
        break