> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla

# 💡 Viikko 5 - Tehtävä A: Viikon sähkönkulutus ja -tuotanto (kWh) konsolissa

Tehtävänäsi on laatia Python-ohjelma, joka:

1. **Lukee tiedot tiedostosta `viikko42.csv`**
2. **Laskee jokaiselle viikonpäivälle** (ma–su):

   * vaiheittaisen **sähkönkulutuksen** (vaihe 1–3) **kWh-yksikössä**
   * vaiheittaisen **sähköntuotannon** (vaihe 1–3) **kWh-yksikössä**
3. **Tulostaa tulokset konsoliin selkeänä, käyttäjäystävällisenä taulukkona.**

Tiedosto sisältää viikon 42 (ma–su) tuntikohtaiset mittaukset:

* aika (päivämäärä ja kellonaika)
* kulutus kolmeen vaiheeseen jaettuna (Wh)
* tuotanto kolmeen vaiheeseen jaettuna (Wh)

Sinun tehtäväsi on **muuntaa Wh → kWh** ja esittää tulokset **kahden desimaalin tarkkuudella**.

> [!NOTE]
> Halutessa työn voi tehdä **`pareittain (max. kaksi)`**. Tällöin kohdassa [Palautusohje Itslearningiin](#-palautusohje-itslearningiin) pari tekee vain yhden palautuksen, johon on yhdistetty molemmat.

---

## ⚖️ Yksikkö: Wh → kWh

Tiedostossa arvot ovat **Wh**. Tulosteessa kaikki energia-arvot tulee esittää **kWh**-yksikössä.

---

## 1️⃣ Ohjelman toiminnallisuus

**Tulostaa tiedot tiedostosta `viikko42.csv` selkeänä taulukkona**, jossa näkyy:

   * viikonpäivä suomeksi (maanantai, tiistai, …)
   * päivän päivämäärä muodossa **pv.kk.vuosi** (esim. `13.10.2025`)
   * kulutus vaihe 1–3 (kWh, kahden desimaalin tarkkuudella, pilkku desimaalina)
   * tuotanto vaihe 1–3 (kWh, kahden desimaalin tarkkuudella, pilkku desimaalina)

Tulosteen esimerkkirakenne (muotoilua saa muuttaa, mutta tulosteen pitää olla käyttäjäystävällinen):

```text
Viikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)

Päivä         Pvm         Kulutus [kWh]                 Tuotanto [kWh]
             (pv.kk.vvvv)  v1      v2      v3            v1     v2     v3
---------------------------------------------------------------------------
maanantai     13.10.2025   12,35   1,56    2,78          0,01   0,39   0,52
tiistai       14.10.2025   ...     ...     ...           ...    ...    ...
...
sunnuntai     19.10.2025   ...     ...     ...           ...    ...    ...
```

---

## 2️⃣ Funktioiden käyttö (pakollinen vaatimus)

Ohjelma pitää rakentaa **funktioiden varaan**, ei ”kaikki koodi suoraan tiedoston juureen”.

* Käytä **funktiota**, esim.:

  ```py
  def lue_data(tiedoston_nimi: str) -> list:
      """Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa."""
      ...

* Tee myös **pääfunktio**, esimerkiksi:

  ```py
  def main() -> None:
      """Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin."""
      ...
  ```

* Lopussa:

  ```py
  if __name__ == "__main__":
      main()
  ```

### 📚 Docstring-vaatimus

Jokaisella funktiolla tulee olla **docstring**, joka kertoo **mitä funktio tekee** lyhyesti ja selkeästi.

* Käytä kolmella lainausmerkillä tehtävää docstringiä:

  ```py
  def esimerkki(arvo: int) -> float:
      """Muuntaa kokonaisluvun liukuluvuksi ja palauttaa arvon kerrottuna kymmenellä."""
      ...
  ```

### 🔤 Tietotyyppivihjeet (type hints)

Kaikissa funktioissa tulee käyttää **tietotyyppivihjeitä**:

* parametrien tyypit
* palautusarvon tyyppi

Esimerkiksi:

```py
from datetime import datetime
from typing import List, Dict

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
Jos käytät **ehtolauseita** (`if`) tai vertailuja päivämäärien / aikojen kanssa, **älä vertaile raakatekstiä**, vaan käytä **oikeita tietotyyppejä** (`datetime`, `date`).

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

# esim. vertaillaan toiseen date-olioon
if paiva == date(2025, 10, 13):
    ...
```

---

## 5️⃣ Suomalaisten esitystapojen korostus 🇫🇮

Tulosteessa:

1. **Päivämäärä**:

   * Muoto: **pv.kk.vuosi**
   * Esim. `13.10.2025`
   * Voit muodostaa sen esimerkiksi:

     ```py
     pvm_str = f"{paiva.day}.{paiva.month}.{paiva.year}"
     ```

2. **Desimaaliluvut** (kWh-arvot):

   * Esitetään **pilkulla**, ei pisteellä
   * Pyöristetään **kahteen desimaaliin**
   * Esimerkki:

     ```py
     arvo_kwh = 1.2345
     arvo_str = f"{arvo_kwh:.2f}"      # "1.23"
     arvo_str = arvo_str.replace(".", ",")  # "1,23"
     ```

---

## 6️⃣ Ohjelmoinnin perusrakenteet (pakolliset)

Ohjelmassa tulee käyttää ainakin:

* **Muuttujia** (esim. päiväkohtaiset summat)
* **Listoja tai muita tietorakenteita**
* **Toistorakennetta** (`for`) rivien ja päivien läpikäyntiin
* **Ehtolauseita** (`if`) – erityisesti:

  * päivien ryhmittelyyn / valintaan
  * mahdollisesti ”erityispäivän” korostamiseen (esim. pienin nettokulutus)
* **Funktioita**, joissa on:

  * docstring
  * tietotyyppivihjeet

---

## 7️⃣ Bonus-ideat (vapaaehtoiset ⭐)

Halutessasi voit lisäksi:

1. **Laskea nettokulutuksen** (kulutus − tuotanto) joka päivälle.
2. **Korostaa parhaan päivän** (esim. pienin nettokulutus) tähdellä tai lisätekstillä.
3. **Tulostaa viikon yhteenvedon** (kokonaiskulutus ja -tuotanto vaiheittain).
4. **Lisätä yksinkertaisen valikon** (näytä vain kulutus / tuotanto / molemmat).

---

## 📤 Palautusohje Itslearningiin

Palauta **linkki GitHub-repoon** ja **kuvankaappaus konsolista**, jossa näkyy ohjelman suoritus ja tulostus.

> [!NOTE]
> Ota kuvakaappaus ilman bonustehtäviä.