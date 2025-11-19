def tulosta_lista():
    lista = ["omena", "banaani", "päärynä", "kiivi"]
    print("Hedelmät: ", end="")
    for i in range(len(lista)):
        if i < len(lista) - 1:
            print(lista[i], end="-")
        else:
            print(lista[i])  # Viimeinen alkio ilman '-'

def main():
    tulosta_lista()

if __name__ == "__main__":
    main()