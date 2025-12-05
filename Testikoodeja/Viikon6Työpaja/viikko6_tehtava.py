# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date, timedelta

def muunna_tiedot(tietue: list) -> list:
    """
    Muuttaa jokaisen annetun tietorivin tietotyypit oikeiksi

    Parametrit:
     tietue: Sisältää 7 kenttää, joista ensimmäinen date -> loput int

    Palautus:
     Listan, jossa muutetut tietotyypit
    """
    return [
        datetime.fromisoformat(tietue[0]),
        int(tietue[1]),
        int(tietue[2]),
        int(tietue[3]),
        int(tietue[4]),
        int(tietue[5]),
        int(tietue[6]),
    ]

def lue_data(tiedoston_nimi: str) -> list:
    """
    Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa ja tietotyypeissä.

    Kutsuu funktiota muunna_tiedot (lst):
     funktio palauttaa listan -> Tietotyypit muutettu

    Parametrit:
     tiedoston_nimi (str): ottaa vastaan tiedoston, jossa kentät jaettu merkillä ;

    Palautus:
     tietokanta (lst): palauttaa tietokannan, jossa tietotyypit on muutettu
    """
    tietokanta = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # Otetaan kenttien esittelytiedot pois
        for tietue in f:
            tietue = tietue.split(";")
            tietokanta.append(muunna_tiedot(tietue))

    return tietokanta

def main():
    """
    Ohjelman pääfunktio: kysyys käyttäjältä inputteja ja tulostaa/vie tiedostoon raportteja
    """
    while True:
        print("Valitse raporttityyppi:")
        print("1) Päiväkohtainen yhteenveto aikaväliltä")
        print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
        print("3) Vuoden 2025 kokonaisyhteenveto")
        print("4) Lopeta ohjelma")
        ensimmainen_valinta = int(input("Anna valinta (numero 1-4): "))
        if ensimmainen_valinta == 1:
            alkupaiva = input("Anna alkupäivä (pv.kk.vvvv): ")
            loppupaiva = input("Anna loppupäivä (pv.kk.vvvv): ")
            print("raportti aikaväliltä tulostuu...")
        elif ensimmainen_valinta == 2:
            kuukausi = input("Anna kuukauden numero (1–12): ")
            print("kuukausiraportti tulostuu...")
        elif ensimmainen_valinta == 3:
            print("vuosiraportti tulostuu...")
        elif ensimmainen_valinta == 4:
            print("Lopetaan ohjelma...")
            break
        else:
            continue

        print("---------------------------------------------------------")
        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")
        toinen_valinta = int(input("Anna valinta (numero 1-3): "))
        if toinen_valinta == 1:
            print("raportti kirjoitetaan tiedostoon...")
        elif toinen_valinta == 2:
            continue
        elif toinen_valinta == 3:
            print("Lopetaan ohjelma...")
            break
        else:
            continue

        print("---------------------------------------------------------")

    #print("Valitsit ", ensimmainen_valinta)


if __name__ == "__main__":
    main()