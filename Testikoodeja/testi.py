def tulosta_lista():
    lista = ["omena", "banaani", "päärynä", "kiivi"]
    print("Hedelmät: ", end="")
    print("-".join(lista))


def main():
    #tulosta_lista()
    
    # Odottaa käyttäjän syötettä ennen sulkemista
    #input("\nPaina Enter sulkeaksesi...")

    ika = int(input("Anna ikä: "))
    jäsen = (input("Oletko jäsen - vastaa kyllä tai ei: ") == "kyllä")


    if ika >= 18:
        if jäsen:
            print("Pääsy sallittu")
        else:
            print("Jäsenyyttä vaaditaan")
    else:
        print("Alaikäinen")


if __name__ == "__main__":
    main()