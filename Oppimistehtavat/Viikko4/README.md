> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla

# 🐍 Varaustietojen käsitty (Osa A & B)

## 🎯 Tavoite

Tehtävän tavoitteena on harjoitella:

* tietotyyppimuunnoksia Pythonissa
* `datetime`-kirjaston käyttöä (`datetime.date`, `datetime.time`, `datetime.datetime`)
* listojen käsittelyä ja varausdatan rakenteistamista
* koodin jakamista selkeään funktioon (`muunna_varaustiedot`)

> [!NOTE]
> Halutessa työn voi tehdä **`pareittain (max. kaksi)`**. Tällöin kohdassa [Palautusohje Itslearningiin](#-palautusohje-itslearningiin) pari tekee vain yhden palautuksen, johon on yhdistetty molemmat.
> Osa **A** tehdään ensin. **Palautus Itslearningiin tehdään yhdessä osan B kanssa.**

---

## 📄 Kuvaus

Sinulle on annettu:

* tekstitiedosto [**`varaukset.txt`**](https://github.com/vheikkiniemi/OhjelmoinninPerusteet2025S/blob/main/Oppimistehtavat/Viikko4/varaukset.txt), jossa jokainen rivi sisältää yhden varauksen tiedot.
* Python-skripti [**`lue_varaukset.py`**](https://github.com/vheikkiniemi/OhjelmoinninPerusteet2025S/blob/main/Oppimistehtavat/Viikko4/lue_varaukset.py), jossa on valmiiksi toteutettuja toiminnallisuuksia varauksien lukemiseen (mm. funktio `muunna_varaustiedot`)

**Esimerkkirivi `varaukset.txt` tiedostossa:**

```
201|Muumi Muumilaakso|muumi@valkoinenlaakso.org|0509876543|2025-11-12|09:00|2|18.50|True|Metsätila 1|2025-08-12 14:33:20
```

Rivillä on seuraavat tiedot:

| Sarake                 | Selite               | Tietotyyppi, jota tavoitellaan |
| ---------------------- | -------------------- | ------------------------------ |
| 1  `varausId`          | Varausnumero         | `int`                          |
| 2  `nimi`              | Varaajan nimi        | `str`                          |
| 3  `sähköposti`        | Varaajan sähköposti  | `str`                          |
| 4  `puhelin`           | Varaajan puhelin     | `str`                          |
| 5  `varauksenPvm`      | Varauspäivä          | `datetime.date`                |
| 6  `varauksenKlo`      | Aloitusaika          | `datetime.time`                |
| 7  `varauksenKesto`    | Tuntimäärä           | `int`                          |
| 8  `hinta`             | Tuntihinta (€)       | `float`                        |
| 9  `varausVahvistettu` | Vahvistettu          | `bool`                         |
| 10 `varattuTila`       | Varauskohde          | `str`                          |
| 11 `varausLuotu`       | Milloin varaus luotu | `datetime`            |

---

## 🧠 Osa A: `muunna_varaustiedot` kuntoon

Tässä osassa keskitytään yhden varausrivin muuntamiseen oikeisiin tietotyyppeihin..

> [!TIP]
> Aikaisemmista tehtävistä poiketen tässä funktio tekee heti lukemisen jälkeen muunnoksen ja ohjelma jatkaa muunnettujen tietojen kanssa.

---

### 1️⃣ Valmistelut

1. Kopioi tiedosto **`varaukset.txt`** omaan Git-repoosi ja kansioon `Viikko4`.
2. Kopioi Python-skripti **`lue_varaukset.py`** samaan `Viikko4`-kansioon.
3. Varmista, että ohjelma käynnistyy komennolla → `ohjelma tulostaa varaukset ja muuttamattomat tietotyypit`:

   ```bash
   python lue_varaukset.py
   ```
---

### 2️⃣ Funktio `muunna_varaustiedot`

Skriptissä on funktio nimeltä **`muunna_varaustiedot`**, joka saa parametrina **yhdestä rivistä splitatun listan**. Esim.:

```python
["201", "Muumi Muumilaakso", "muumi@valkoinenlaakso.org", "0509876543", "2025-11-12", "09:00", "2", "18.50", "True", "Metsätila 1", "2025-08-12 14:33:20"]
```

**Tehtäväsi on muuttaa funktiota `muunna_varaustiedot` niin, että se palauttaa listan, jossa sarakkeet ovat seuraavissa tietotyypeissä:**

```text
varausId | nimi | sähköposti | puhelin | varauksenPvm | varauksenKlo | varauksenKesto | hinta | varausVahvistettu | varattuTila | varausLuotu

int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
```

> [!TIP]
> Käytä apuna Pythonin `datetime`-kirjastoa:

```python
from datetime import datetime, date, time
```

> [!TIP]
> Esimerkkejä muunnoksista (voit sovittaa omaan koodiisi):

```python
# 1) varausId: str -> int
varaus_id = int(rivi[0])

# 5) varauksenPvm: "2025-11-12" -> datetime.date
varauksen_pvm = datetime.strptime(rivi[4], "%Y-%m-%d").date()

# 6) varauksenKlo: "09:00" -> datetime.time
varauksen_klo = datetime.strptime(rivi[5], "%H:%M").time()

# 8) hinta: "18.50" -> float
hinta = float(rivi[7])

# 9) varausVahvistettu: "True"/"False" -> bool
varaus_vahvistettu = (rivi[8] == "True")

# 11) varausLuotu: "2025-08-12 14:33:20" -> datetime.datetime
varaus_luotu = datetime.strptime(rivi[10], "%Y-%m-%d %H:%M:%S")
```

**Lopuksi** funktio palauttaa listan, jossa kentät ovat oikeassa järjestyksessä ja tietotyypeissä.

> [!TIP]
> Esim. (ei ole pakko käyttää juuri tätä muuttujanimitystä ja/tapaa, mutta idea on sama):

```python
return [
    varaus_id, nimi, sahkoposti, puhelin,
    varauksen_pvm, varauksen_klo,
    varauksen_kesto, hinta,
    varaus_vahvistettu, varattu_tila,
    varaus_luotu
]
```

### 3️⃣ Testaus

Varmista, että ohjelma käynnistyy komennolla → `ohjelma tulostaa varaukset ja muutetut tietotyypit`:

```bash
python lue_varaukset.py
```
---

### 🧩 Vihjeitä

* Tutustu edellisten tehtävien: [viikko2](../Viikko2/README.md) [viikko3](../Viikko3/README.md) vihjeisiin
* Viikon 2 työpajalla tehtyyn ohjelmaan, joka löytyy [tästä linkistä](https://github.com/vheikkiniemi/OhjelmoinninPerusteet2025S/blob/main/Testikoodeja/Viikon2Tyopaja/lue_varaukset.py)
* Viikon 3 työpajalla tehtyyn ohjelmaan, joka löytyy [tästä linkistä](https://github.com/vheikkiniemi/OhjelmoinninPerusteet2025S/blob/main/Testikoodeja/Viikon3Tyopaja/lue_varaukset.py)
* **Katso Panoptosta viikon 3 työpajan tallenne**
* Tee muunnokset **pienissä paloissa**:

  * ensin `int` ja `float`
  * sitten `bool`
  * lopuksi `datetime.date`, `datetime.time` ja `datetime`
* Jos `datetime.strptime` antaa virheen, tarkista tarkasti:

  * millainen merkkijono tulee tiedostosta
  * että formaattimerkkijono (`"%Y-%m-%d %H:%M:%S"`) vastaa tarkalleen merkkijonon muotoa
* Voit lisätä väliaikaisia `print`-komentoja debuggausta varten (esim. `print(rivi[4], type(varauksen_pvm))`).
* **Jos et pääse eteenpäin, tule työpajaan! 😉**

---

## 🧠 Osa B: jatko-osa (tulossa myöhemmin)

Osa B täydentää tämän viikon tehtävää:

* Osa A keskittyy tietotyyppien muuntamiseen.
* Osa B:ssa jatketaan tästä eteenpäin (esim. varauslistan käsittelyyn ja tulostukseen liittyvillä toiminnoilla).

> [!IMPORTANT]
> **Älä palauta tehtävää vielä Itslearningiin.**
> Osan A **palautus tapahtuu yhdessä osan B kanssa.**

---

## 📤 Palautusohje Itslearningiin

> [!WARNING]
> **Tätä vaihetta ei vielä tehdä.**
> Viikon 4 tehtävän **lopullinen palautus** (Osa A + Osa B) tehdään, kun Osa B on julkaistu.

Myöhemmin, kun Osa B on valmis, palautusohje on muodoltaan samantapainen kuin edellisellä viikolla:

* linkki GitHub-repoon
* kuvankaappaus ohjelman suorituksesta (konsoli)
* lyhyt teksti:

  > Mitä jäi päällimmäisenä tehtävästä mieleen?

---

## 💬 Hyvä fiilis tekemiseen!

**Muista:** kaikki ohjelmoijat aloittavat jostain. Tärkeintä ei ole täydellinen koodi, vaan **oppiminen, kokeilu ja oivallus**. Pidä hauskaa ja tutki, miten ihan oikeita asioita ihan oikeasti tehdään! 🚀💡😎

---

## 💡 Yleisimmät virheet ja ratkaisut

| Virhe | Syy | Ratkaisu |
|-------|-----|----------|
| “Tiedostoa ei löydy” | Skriptiä ajetaan väärässä kansiossa | Siirry kansioon jossa skripti on |
| “Tiedostoa ei löydy” | Tiedostoja ei ole kopioitu | Kopioi tiedostot kansioosi |
| “Tiedostoa ei löydy” | Tiedostot on nimetty väärin | Varmista tiedostojen nimien oikeellisuus |