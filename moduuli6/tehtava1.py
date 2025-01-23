from random import randint

def noppa():
    return randint(1, 6)

def main():
    while True:
        i = noppa()

        print(i)

        if i == 6:
            break

main()