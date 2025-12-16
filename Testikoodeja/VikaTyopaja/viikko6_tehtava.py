# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date

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
        float(tietue[1].replace(",", ".")),
        float(tietue[2].replace(",", ".")),
        float(tietue[3].replace(",", ".")),
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


def raportti_tiedostoon(raportti: str):
    """
    Kirjoittaa annetun sisällön tiedostoon

    Parametrit:
     raportti (str): raporttiteksti
    """
    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write(raportti)


def raportti_aikavali(alkupaiva: str, loppupaiva: str, tietokanta: list) -> str:
    """
    Luo raportin aikaväliltä

    Parametrit:
     alkupaiva (str): aikavälin aloituspäivä
     loppupaiva (str): aikavälin lopetuspäivä
     tietokanta (list): sisältää kaikki tietueet

    Palautus:
     raportti (lst): palauttaa luodun raportin
    """
    alkupv = int(alkupaiva.split(".")[0])
    alkukk = int(alkupaiva.split(".")[1])
    alkuvv = int(alkupaiva.split(".")[2])
    alku = date(alkuvv, alkukk, alkupv)
    loppupv = int(loppupaiva.split(".")[0])
    loppukk = int(loppupaiva.split(".")[1])
    loppuvv = int(loppupaiva.split(".")[2])
    loppu = date(loppuvv, loppukk, loppupv)
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    tietue_lkm = 0
    for tietue in tietokanta:
        if alku <= tietue[0].date() <= loppu:
            kulutus += tietue[1]
            tuotanto += tietue[2]
            lampotila += tietue[3]
            tietue_lkm += 1

    raportti = "---------------------------------------------------------\n"
    raportti += f"Raportti aikaväliltä {alkupaiva}-{loppupaiva}\n"
    raportti += f"- kokonaiskulutus: {kulutus:.2f} kWh\n".replace(".", ",")
    raportti += f"- kokonaistuotanto: {tuotanto:.2f} kWh\n".replace(".", ",")
    raportti += f"- keskilämpötila: {lampotila/tietue_lkm:.2f} °C\n".replace(".", ",")
    raportti += "---------------------------------------------------------\n"
    return raportti


def raportti_kuukausi(kuukausi: str, tietokanta: list) -> str:
    """
    Luo kuukausiraportin

    Parametrit:
     kuukausi (str): pyydetty kuukausi
     tietokanta (list): sisältää kaikki tietueet

    Palautus:
     raportti (lst): palauttaa luodun raportin
    """
    kuukaudet = [
        "Tammikuu",
        "Helmikuu",
        "Maaliskuu",
        "Huhtikuu",
        "Toukokuu",
        "Kesäkuu",
        "Heinäkuu",
        "Elokuu",
        "Syyskuu",
        "Lokakuu",
        "Marraskuu",
        "Joulukuu",
    ]
    kk = int(kuukausi)
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    tietue_lkm = 0
    for tietue in tietokanta:
        if tietue[0].date().month == kk:
            kulutus += tietue[1]
            tuotanto += tietue[2]
            lampotila += tietue[3]
            tietue_lkm += 1

    raportti = "---------------------------------------------------------\n"
    raportti += f"Raportti kuukaudelta: {kuukaudet[kk-1]}\n"
    raportti += f"- kokonaiskulutus: {kulutus:.2f} kWh\n".replace(".", ",")
    raportti += f"- kokonaistuotanto: {tuotanto:.2f} kWh\n".replace(".", ",")
    raportti += f"- keskilämpötila: {lampotila/tietue_lkm:.2f} °C\n".replace(".", ",")
    raportti += "---------------------------------------------------------\n"
    return raportti

def raportti_vuosi(tietokanta: list) -> str:
    """
    Luo vuosiraportin

    Parametrit:
     tietokanta (list): sisältää kaikki tietueet

    Palautus:
     raportti (lst): palauttaa luodun raportin
    """
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    tietue_lkm = 0
    for tietue in tietokanta:
        kulutus += tietue[1]
        tuotanto += tietue[2]
        lampotila += tietue[3]
        tietue_lkm += 1

    raportti = "---------------------------------------------------------\n"
    raportti += f"Raportti vuodelta 2025\n"
    raportti += f"- kokonaiskulutus: {kulutus:.2f} kWh\n".replace(".", ",")
    raportti += f"- kokonaistuotanto: {tuotanto:.2f} kWh\n".replace(".", ",")
    raportti += f"- keskilämpötila: {lampotila/tietue_lkm:.2f} °C\n".replace(".", ",")
    raportti += "---------------------------------------------------------\n"
    return raportti

def main():
    """
    Ohjelman pääfunktio: kysyys käyttäjältä inputteja ja tulostaa/vie tiedostoon raportteja
    """
    # Luetaan data tiedostosta
    kulutusTuotanto2025 = lue_data("2025.csv")

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
            raportti = raportti_aikavali(alkupaiva, loppupaiva, kulutusTuotanto2025)
            print(raportti)
        elif ensimmainen_valinta == 2:
            kuukausi = input("Anna kuukauden numero (1–12): ")
            raportti = raportti_kuukausi(kuukausi, kulutusTuotanto2025)
            print(raportti)
        elif ensimmainen_valinta == 3:
            raportti = raportti_vuosi(kulutusTuotanto2025)
            print(raportti)
        elif ensimmainen_valinta == 4:
            print("Lopetaan ohjelma...")
            break
        else:
            continue

        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")
        toinen_valinta = int(input("Anna valinta (numero 1-3): "))
        if toinen_valinta == 1:
            raportti_tiedostoon(raportti)
            print("Raportti kirjoitettu tiedostoon.")
        elif toinen_valinta == 2:
            continue
        elif toinen_valinta == 3:
            print("Lopetaan ohjelma...")
            break
        else:
            continue

        print("---------------------------------------------------------")

if __name__ == "__main__":
    main()