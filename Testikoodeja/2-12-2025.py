import time
import sys


def main():
    # try:
    #    ika_str = int(input("Anna ikäsi (vuosia): "))
    # except ValueError:
    #    print("Tyyppimuunnos ei onnistunut")
    #    sys.exit("Ohjelma lopetettiin virheen vuoksi.")

    # print(type(ika_str))
    # ika = int(ika_str)  # tyyppimuunnos str -> int
    # print(type(ika))
    # print("Ensi vuonna olet", ika_str + 1)
    #pituus_str = input("Anna pituutesi metreinä (esim. 1,75): ")
    #pituus = float(pituus_str.replace(",", "."))  # muutetaan pilkku pisteeksi
    #print("Pituus metreinä:", f"{pituus}".replace(".", ","))
    #jatka = True
    
    while True:
        syote1 = input("Anna ensimmäinen kokonaisluku: ")
        syote2 = input("Anna toinen kokonaisluku: ")

        try:
            luku1 = int(syote1)
            luku2 = int(syote2)
        except ValueError:
            print("Virhe: Eivät olleet kokonaislukuja. Yritä uudestaan.")
            continue

        syote3 = input("Lasketaan yhteen -> Anna +, vähennetään -> Anna - :")
        if syote3 == "+":
            print("Lasketaan yhteen ", luku1+luku2)
            break
        elif syote3 == "-":
            print("Vähennetään ", luku1-luku2)
            break
        else:
            print("Tuntematon merkki")




if __name__ == "__main__":
    main()
