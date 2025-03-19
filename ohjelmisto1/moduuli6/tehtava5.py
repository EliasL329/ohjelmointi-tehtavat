def karsi_parittomat(lista):
    for i in lista:
        if i // 2 != i / 2:
            lista.remove(i)

    return lista

def main():
    lista = [1, 2, 3 , 4, 5]

    print(karsi_parittomat(lista))

main()