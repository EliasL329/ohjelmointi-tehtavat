def muunna(gallona):
    return print(f"{gallona} gallonaa litroina on {gallona * 3.785}")

def main():
    while True:
        gallona_maara = int(input("Syötä gallonamäärä: "))

        if gallona_maara < 0:
            break
        
        muunna(gallona_maara)

main()