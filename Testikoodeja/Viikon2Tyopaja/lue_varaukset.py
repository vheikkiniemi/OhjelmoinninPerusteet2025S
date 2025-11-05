# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime
"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    # Tulostetaan varaus konsoliin
    varausnumero = int(varaus.split('|')[0])
    print("Varausnumero:", varausnumero)
    varaajannimi = varaus.split('|')[1]
    print("Varaaja:", varaajannimi)
    paivamaara = datetime.strptime(varaus.split('|')[2], "%Y-%m-%d").date()
    print("Päivämäärä:", paivamaara.strftime("%d.%m.%Y"))
    aloitusaika = datetime.strptime(varaus.split('|')[3], "%H:%M").time()
    print("Aloitusaika:", aloitusaika.strftime("%H.%M"))
    tuntimaara = int(varaus.split('|')[4])
    print("Tuntimäärä:", tuntimaara)
    tuntihinta = float(varaus.split('|')[5])
    print("Tuntihinta:", tuntihinta, "€")
    kokonaishinta = tuntihinta*tuntimaara
    print("Kokonaishinta:", kokonaishinta, "€")
    maksettu = varaus.split('|')[6]
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")
    varauskohde = varaus.split('|')[7]
    print("Kohde:", varauskohde)
    puhelinnumero = varaus.split('|')[8]
    print("Puhelin:", puhelinnumero)
    sahkoposti = varaus.split('|')[9]
    print("Sähköposti:", sahkoposti)

if __name__ == "__main__":
    main()