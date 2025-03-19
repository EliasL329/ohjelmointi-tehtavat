from random import randint

def noppa(tahko):
    return randint(1, tahko)

def main():
    tahko = int(input("Nopan tahkojen määrä: "))

    while True:
        i = noppa(tahko)

        print(i)

        if i == tahko:
            break

main()