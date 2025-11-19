def tulosta_lista():
    lista = ["omena", "banaani", "päärynä", "kiivi"]
    print("Hedelmät: ", end="")
    print("-".join(lista))


def main():
    tulosta_lista()
    
    # Odottaa käyttäjän syötettä ennen sulkemista
    input("\nPaina Enter sulkeaksesi...")

if __name__ == "__main__":
    main()