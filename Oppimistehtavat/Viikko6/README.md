> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla

# Viikko 6: Vuoden sähkönkulutuksen raportointi

Tehtävänäsi on laatia Python-ohjelma, joka:

1. **Lukee tiedot tiedostosta `2025.csv`**
2. Tarjoaa käyttäjälle **valikon input-komentojen avulla**, jossa käyttäjä voi valita erilaisia raportteja
3. **Laskee valitun raporttityypin** (esim. aikavälin päiväyhteenveto, kuukausiyhteenveto, koko vuoden yhteenveto)
4. **Tulostaa raportin konsoliin** selkeänä tekstinä
5. Raportin tulostuksen jälkeen kysyy käyttäjältä:

   * `1) Kirjoita raportti tiedostoon raportti.txt`
   * `2) Luo uusi raportti`
   * `3) Lopeta`
     ja toimii valinnan mukaan
6. Kirjoittaa raportin **tiedostoon `raportti.txt`**, jos käyttäjä valitsee kohdan 1. Tiedoston nimi on **aina sama** (`raportti.txt`) ja uusi raportti **korvaa** aiemman.

Tiedosto `2025.csv` sisältää vuoden 2025 tuntikohtaiset mittaukset:

* aika (päivämäärä ja kellonaika)
* kulutus (netotettu) kWh
* tuotanto (netotettu) kWh
* vuorokauden keskilämpötila

Tavoitteena on rakentaa **interaktiivinen raporttigeneraattori**, joka hyödyntää inputteja ja tekee ohjelmasta enemmän ”oikean työkalun” tuntuisen.

> [!NOTE]
> Halutessa työn voi tehdä **pareittain (max. kaksi)**. Tällöin kohdassa [Palautusohje Itslearningiin](#-palautusohje-itslearningiin) pari tekee vain yhden palautuksen, johon on yhdistetty molemmat.

---

## ⚖️ Yksikkö ja esitystavat

Tiedostossa arvot ovat jo **kWh-yksikössä**. Raportissa sinun tulee huolehtia:

* **Desimaaliluvut** esitetään **kahden desimaalin tarkkuudella**, käyttäen **pilkkua desimaalierottimena**.
* Päivämäärät esitetään muodossa **pv.kk.vuosi** (esim. `13.10.2025`).
* Raportissa käytetään **selkeitä otsikoita ja taulukkomaisuutta**, jotta lukija ymmärtää sisällön helposti.

---

## 1️⃣ Ohjelman toiminnallisuus

Ohjelman tulee:

1. **Lukea CSV-tiedosto** `2025.csv`.

2. Muuntaa rivit sellaiseen rakenteeseen, että niistä voidaan laskea helposti päivä-, kuukausi- ja vuositasoisia yhteenvetoja (esim. listat, sanakirjat, tms.).

3. Näyttää käyttäjälle **valikko**, esim.:

   ```text
   Valitse raporttityyppi:
   1) Päiväkohtainen yhteenveto aikaväliltä
   2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle
   3) Vuoden 2025 kokonaisyhteenveto
   4) Lopeta ohjelma
   ```

4. Kysyy valinnan perusteella tarvittavat lisäinputit (ks. alla).

5. Laskee ja tulostaa **raportin konsoliin**.

6. Raportin jälkeen näyttää **toisen valikon**:

   ```text
   Mitä haluat tehdä seuraavaksi?
   1) Kirjoita raportti tiedostoon raportti.txt
   2) Luo uusi raportti
   3) Lopeta
   ```

   * Jos käyttäjä valitsee **1**, ohjelma kirjoittaa **juuri luodun raportin** tiedostoon `raportti.txt`.
   * Jos käyttäjä valitsee **2**, ohjelma palaa raporttivalikkoon ja käyttäjä voi luoda uuden raportin.
   * Jos käyttäjä valitsee **3**, ohjelma lopettaa.

Ohjelma toimii siis **silmukassa**, kunnes käyttäjä haluaa lopettaa. 🔁

---

### 📅 Raportti 1: Päiväkohtainen yhteenveto aikaväliltä

Kysy käyttäjältä:

* **Alkupäivä**: `Anna alkupäivä (pv.kk.vvvv):`
* **Loppupäivä**: `Anna loppupäivä (pv.kk.vvvv):`

Raporttiin tulostetaan aikaväliltä:

* Alku- ja loppupäivä (pv.kk.vvvv-pv.kk.vvvv)
* Aikavälin kokonaiskulutus (kWh, 2 desimaalia, pilkku desimaalina)
* Aikavälin kokonaistuotanto (kWh, 2 desimaalia, pilkku desimaalina)
* Aikavälin keskilämpötila (esim. kaikkien tuntien lämpötilojen keskiarvo)

**Bonus-ideoita (vapaaehtoiset ⭐)**
* Lisää myös **nettokuorman** (kulutus − tuotanto)
* Lisää päivä, jolla kulutus oli suurin (+ lämpötila)
* Lisää päivä, jolla kulutus oli pienin (+ lämpötila)

---

### 📆 Raportti 2: Kuukausikohtainen yhteenveto

Kysy käyttäjältä:

* **Kuukauden numero** (1–12), esim. `Anna kuukauden numero (1–12):`

Raportissa tulostetaan:

* Kuukausi
* Kuukauden kokonaiskulutus (kWh)
* Kuukauden kokonaistuotanto (kWh)
* Kuukauden keskimääräinen vuorokauden lämpötila

**Bonus-ideoita (vapaaehtoiset ⭐)**
* Lisää myös **nettokuorman** (kulutus − tuotanto)
* Lisää päivä, jolla kulutus oli suurin (+ lämpötila)
* Lisää päivä, jolla kulutus oli pienin (+ lämpötila)

---

### 📊 Raportti 3: Vuoden 2025 kokonaisyhteenveto

Raportissa tulostetaan:

* Vuoden 2025 kokonaiskulutus (kWh)
* Vuoden 2025 kokonaistuotanto (kWh)
* Vuoden keskimääräinen lämpötila

**Bonus-ideoita (vapaaehtoiset ⭐)**
* Lisää myös **nettokuorman** (kulutus − tuotanto)
* Lisää päivä, jolla kulutus oli suurin (+ lämpötila)
* Lisää päivä, jolla kulutus oli pienin (+ lämpötila)

---

## 2️⃣ Funktioiden käyttö (pakollinen vaatimus)

Ohjelma pitää rakentaa **funktioiden varaan**, ei ”kaikki koodi suoraan tiedoston juureen”.

Käytä esimerkiksi:

```py
def lue_data(tiedoston_nimi: str) -> list:
    """Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa."""
    ...

def nayta_paavalikko() -> str:
    """Tulostaa päävalikon ja palauttaa käyttäjän valinnan merkkijonona."""
    ...

def luo_paivaraportti(data: list) -> list[str]:
    """Muodostaa päiväkohtaisen raportin valitulle aikavälille."""
    ...

def luo_kuukausiraportti(data: list) -> list[str]:
    """Muodostaa kuukausikohtaisen yhteenvedon valitulle kuukaudelle."""
    ...

def luo_vuosiraportti(data: list) -> list[str]:
    """Muodostaa koko vuoden yhteenvedon."""
    ...

def tulosta_raportti_konsoliin(rivit: list[str]) -> None:
    """Tulostaa raportin rivit konsoliin."""
    ...

def kirjoita_raportti_tiedostoon(rivit: list[str]) -> None:
    """Kirjoittaa raportin rivit tiedostoon raportti.txt."""
    ...
```

Lisäksi tee **pääfunktio**, esimerkiksi:

```py
def main() -> None:
    """Ohjelman pääfunktio: lukee datan, näyttää valikot ja ohjaa raporttien luomista."""
    ...
```

Lopussa:

```py
if __name__ == "__main__":
    main()
```

### 📚 Docstring-vaatimus

Jokaisella funktiolla tulee olla **docstring**, joka kertoo **mitä funktio tekee** lyhyesti ja selkeästi.

### 🧾 Tietotyyppivihjeet (type hints)

Kaikissa funktioissa tulee käyttää **tietotyyppivihjeitä**:

* parametrien tyypit
* palautusarvon tyyppi

Esimerkiksi:

```py
from datetime import datetime, date
from typing import List

def muunna_aika(aika_str: str) -> datetime:
    """Muuntaa ISO-muotoisen aikaleiman datetime-olioksi."""
    ...
```

---

## 3️⃣ MIT Copyright -merkintä

Kooditiedoston alkuun tulee laittaa **copyright- ja lisenssimerkintä**, esimerkiksi:

```py
# Copyright (c) 2025 Oma Nimi
# License: MIT
```

---

## 4️⃣ Päivämäärä & aika – käsittele **tietotyyppeinä**, älä tekstinä

**Tärkeä periaate:**

Käyttäessä **ehtolauseita** (`if`) tai vertailuja päivämäärien / aikojen kanssa, **älä vertaile raakatekstiä**, vaan käytä **oikeita tietotyyppejä** (`datetime`, `date`).

❌ Huono tapa (merkkijonovertailu):

```py
if aika_str[:10] == "2025-10-13":
    ...
```

✅ Parempi tapa:

```py
from datetime import datetime, date

aika = datetime.fromisoformat(aika_str)  # esim. "2025-10-13T00:00:00"
paiva = aika.date()

if paiva == date(2025, 10, 13):
    ...
```

---

## 5️⃣ Suomalaisten esitystapojen korostus

Raportissa (`raportti.txt` ja konsolissa):

1. **Päivämäärä**

   * Muoto: **pv.kk.vuosi**
   * Esim. `13.10.2025`
   * Voit muodostaa sen esimerkiksi:

     ```py
     pvm_str = f"{paiva.day}.{paiva.month}.{paiva.year}"
     ```

2. **Desimaaliluvut** (kWh-arvot):

   * Esitetään **pilkulla**, ei pisteellä
   * Pyöristetään **kahteen desimaaliin**

   Esimerkki:

   ```py
   arvo_kwh = 1.2345
   arvo_str = f"{arvo_kwh:.2f}"   # "1.23"
   arvo_str = arvo_str.replace(".", ",")  # "1,23"
   ```

---

## 6️⃣ Ohjelmoinnin perusrakenteet (pakolliset)

Ohjelmassa tulee käyttää ainakin:

* **Muuttujia** (esim. päiväkohtaiset summat, kuukausikohtaiset summat)
* **Listoja tai muita tietorakenteita** (esim. lista kaikista mittauksista, lista raporttiriveistä)
* **Toistorakenteita** (`for`, tarvittaessa `while`) rivien, päivien ja kuukausien läpikäyntiin
* **Ehtolauseita** (`if`) – erityisesti:

  * valikko- ja input-valintojen käsittelyyn
  * päivien ja kuukausien valintaan
* **Funktioita**, joissa on:

  * docstring
  * tietotyyppivihjeet

Lisäksi tarvitaan:

* **Tiedoston kirjoittamista** (`open("raportti.txt", "w", encoding="utf-8")`) käyttäen `with`-rakennetta, jotta tiedosto **sulkeutuu varmasti oikein**
* **Inputteja**, joilla käyttäjä ohjaa ohjelmaa (valikot, päivämäärät, kuukaudet)

---

## 7️⃣ Bonus-ideat (vapaaehtoiset ⭐)

Halutessasi voit lisäksi (katso myös raporttien yhteydessä olevat):

1. **Lisätä suodattimen**, jolla käyttäjä voi etsiä vain ”poikkeuspäiviä” (esim. kulutus yli X kWh ja lämpötila alle Y °C).
2. **Lisätä yhteenvedon** ohjelman lopuksi, montako raporttia istunnon aikana luotiin.
3. **Lisätä yksinkertaisen tarkistuksen**, joka varoittaa, jos käyttäjän antama aikaväli tai kuukausi ei löydy datasta.

---

## 📤 Palautusohje Itslearningiin

Palauta:

1. **Linkki GitHub-repoon**, jossa on:

   * Python-kooditiedosto (esim. `viikko5_tehtava_c.py`) kansiossa `viikko5`
   * viimeisin ohjelman generoima `raportti.txt`

2. **Kuvankaappaus** VS Coden terminaalista tai hakemistorakenteesta, josta näkyy:

   * että ohjelma on ajettu
   * että `raportti.txt` on luotu
   * että raportteja on voitu luoda useampi peräkkäin (valikkorakenne näkyvissä)

> [!NOTE]
> Jos työ on tehty **pareittain**, tehkää yksi yhteinen repo ja yksi yhteinen palautus, johon lisätään **molempien nimet**.