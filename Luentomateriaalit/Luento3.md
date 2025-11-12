> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla.

# 🧩 Pythonin funktiot ja metodit

Ohjelmoinnissa sekä **funktiot** että **metodit** suorittavat jonkin tehtävän — ne ottavat vastaan syötteitä ja tuottavat tuloksia.
Ne kuitenkin **eivät ole sama asia**. Katsotaan ero selkeästi.

---

## 🔹 Funktio

**Funktio** on *itsenäinen toiminto*, joka **ei kuulu millekään tietylle oliolle**.
Pythonissa monet funktiot ovat sisäänrakennettuja, kuten `print()`, `len()` ja `type()`.

---

**🧠 Perusidea**

* Funktiota **kutsutaan suoraan nimellä**.
* Se **saa argumentteja** sulkujen sisällä.
* Se **ei ole sidottu mihinkään tiettyyn tietotyyppiin**.

---

**💡 Esimerkki: `print()` funktio**

```python
# Funktio: print()
print("Tämä on funktioesimerkki")
```

🔍 Tässä `print()` on **funktio**, joka tulostaa annetun tekstin konsoliin.
Se toimii riippumatta siitä, minkä tyyppistä dataa sille annetaan (string, int, float, jne).

```python
print(123)
print(3.14)
print(["a", "b", "c"])
```

---

## 🔸 Metodi

**Metodi** on *funktio, joka kuuluu jollekin tietylle oliolle* — esimerkiksi merkkijonolle, listalle tai sanakirjalle.
Metodia **kutsutaan olion kautta pisteoperaattorilla (. )**.

---

**🧠 Perusidea**

* Metodi **toimii aina jonkin tietyn tietotyypin yhteydessä**.
* Se **muokkaa tai käsittelee kyseistä oliota**.
* Kutsutaan muodossa:
  `olio.metodi(argumentit)`

---

**💡 Esimerkki: `split()` metodi**

```python
# Metodi: split()
teksti = "Tämä on esimerkki"
sanat = teksti.split()

print(sanat)
```

🔍 Tässä `split()` on **metodi**, joka kuuluu **merkkijono-olioon (`str`)**.
Se jakaa merkkijonon osiin välilyönnin kohdalta ja palauttaa listan.

```python
teksti = "omena,päärynä,appelsiini"
hedelmät = teksti.split(",")
print(hedelmät)
# tulostaa: ['omena', 'päärynä', 'appelsiini']
```

---

## ⚖️ Vertailu: Funktio vs. Metodi

| Ominaisuus                | Funktio                       | Metodi                           |
| ------------------------- | ----------------------------- | -------------------------------- |
| Kuuluu jollekin oliolle   | ❌ Ei                          | ✅ Kyllä                          |
| Kutsutapa                 | `print("hei")`                | `"hei".split()`                  |
| Käyttötarkoitus           | Yleinen toiminto              | Toiminto tietylle tietotyypille  |
| Esimerkkejä               | `print()`, `len()`, `range()` | `split()`, `append()`, `lower()` |
| Vaikuttaa olioon itseensä | ❌ Ei yleensä                  | ✅ Usein kyllä                    |

---

## 🧭 Yhteenveto

* **Funktio**: Yleinen, irrallinen toiminto → esim. `print()`  
* **Metodi**: Olioon sidottu toiminto → esim. `"teksti".split()`

💬 Voit ajatella näin:

> Funktio on kuin työkalu työkalupakissa.  
> Metodi on kuin työkalu, joka on kiinteä osa jotakin konetta.

---

# 🐍 Johdatus Pythonin funktioihin

## 🎯 Mitä funktiot ovat?

**Funktio** on ohjelman osa, joka suorittaa tietyn tehtävän.
Funktioita käytetään, jotta koodi olisi **selkeämpää, uudelleenkäytettävää ja helpommin ylläpidettävää.**

> 💡 Ajattele funktiota kuin "pieniä koneita" ohjelmassasi — ne ottavat sisään syötteen, tekevät jotain, ja palauttavat tuloksen.

---

## 📦 Miksi funktioita käytetään?

Funktioiden avulla:

* vältetään koodin toistoa (DRY – *Don’t Repeat Yourself*)
* voidaan jakaa iso ohjelma pienempiin osiin
* saadaan koodista helpommin luettavaa ja testattavaa
* voidaan käyttää samoja toimintoja eri ohjelmissa

---

## 🧱 Funktion rakenne

Pythonissa funktio määritellään avainsanalla `def`.
Yleinen muoto:

```python
def funktion_nimi(parametrit):
    """Valinnainen dokumentaatiokommentti (docstring)."""
    # Toiminnallisuus
    return arvo  # valinnainen
```

**💡Esimerkki:**

```python
def tervehdi():
    print("Hei, maailma!")

tervehdi()
```

🔍 Tässä `tervehdi()` on funktio, joka ei ota parametreja eikä palauta mitään — se vain **tulostaa** tekstin.

---

## 🧮 Parametrit ja argumentit

Funktio voi vastaanottaa **parametreja**, eli arvoja, joita se käyttää sisäisesti.

```python
def tervehdi(nimi):
    print(f"Hei, {nimi}!")
```

**🔍 Kun kutsumme:**

```python
tervehdi("Ville")
```

**📤 Tulostus:**

```
Hei, Ville!
```

🧩 *Parametri* on muuttuja funktion määrittelyssä.  
🧩 *Argumentti* on arvo, joka annetaan funktiolle kutsussa.

---

## 🔁 Paluuarvot (return)

Funktio voi **palauttaa arvon** avainsanalla `return`.

```python
def summa(a, b):
    return a + b

tulos = summa(3, 5)
print(tulos)  # 8
```

Jos funktio ei sisällä `return`-lausetta, se palauttaa oletuksena `None`.

---

## 💬 Dokumentointikommentit (Docstring)

Voit lisätä funktion alkuun **docstringin**, joka kertoo sen tarkoituksen:

```python
def nelio(x):
    """Laskee annetun luvun neliön."""
    return x * x

print(nelio(4))      # 16
print(nelio.__doc__) # Tulostaa docstringin
```

---

## ⚙️ Oletusarvot parametreille

Funktion parametreille voi määrittää oletusarvot:

```python
def tervehdys(nimi="vieras"):
    print(f"Hei, {nimi}!")

tervehdys()         # Hei, vieras!
tervehdys("Aino")   # Hei, Aino!
```

---

## ✳️ Palautetaan useampi arvo

Pythonissa funktio voi palauttaa useita arvoja kerralla:

```python
def luvut():
    return 10, 20, 30

a, b, c = luvut()
print(a, b, c)  # 10 20 30
```

Tämä palauttaa arvot **tuplena (tuple)**.

---

## 🔍 Funktiot käytännössä – esimerkki

Tässä pieni ohjelma, joka hyödyntää useita funktioita:

```python
def kysy_nimi():
    return input("Anna nimesi: ")

def muodosta_tervehdys(nimi):
    return f"Hei, {nimi}! Tervetuloa ohjelmointiin."

def main():
    nimi = kysy_nimi()
    tervehdys = muodosta_tervehdys(nimi)
    print(tervehdys)

if __name__ == "__main__":
    main()
```

**🔎 Mitä tapahtuu?**

1. Käyttäjältä kysytään nimi
2. Funktio rakentaa tervehdyksen
3. Pääohjelma tulostaa sen

---

## 🧩 Yhteenveto

| Käsite     | Selitys                         | Esimerkki          |
| ---------- | ------------------------------- | ------------------ |
| `def`      | Määrittelee funktion            | `def laske():`     |
| Parametri  | Muuttuja funktion määrittelyssä | `def f(x):`        |
| Argumentti | Arvo, joka annetaan funktiolle  | `f(10)`            |
| `return`   | Palauttaa arvon                 | `return tulos`     |
| `__doc__`  | Dokumentointikommentti          | `print(f.__doc__)` |

---

# 🖨️ Pythonin `print()`-funktio – tulostuksen ydin

`print()` on yksi Pythonin **yleisimmin käytetyistä sisäänrakennetuista funktioista**.
Sen avulla ohjelma voi **näyttää tietoa käyttäjälle** — olipa kyseessä teksti, numero, laskutoimitus tai muuttujan arvo.

---

## 🧩 Peruskäyttö

```python
print("Hei maailma!")
```

**📤 Tulostus:**

```
Hei maailma!
```

➡️ Teksti tulostuu ohjelman suoritusympäristöön (yleensä terminaaliin tai konsoliin).
`print()` **ei palauta arvoa** — se vain **näyttää tietoa käyttäjälle**.

---

## 🔢 Usean arvon tulostaminen

`print()` voi ottaa **useita argumentteja**, jotka erotetaan pilkulla.

```python
nimi = "Ville"
ikä = 47
print("Hei", nimi, "sinä olet", ikä, "vuotias.")
```

**📤 Tulostus:**

```
Hei Ville sinä olet 47 vuotias.
```

💡 Huomaa: `print()` lisää **automaattisesti välilyönnin** argumenttien väliin.

---

## 🔧 Rivinvaihto ja `end`-parametri

Oletuksena `print()` lisää **rivinvaihdon (`\n`)** jokaisen tulostuksen loppuun.
Tämä tarkoittaa, että jokainen `print()` alkaa uudelta riviltä.

Voit muuttaa tätä käytöstä käyttämällä **`end`-parametria**.

```python
print("Hei", end=" ")
print("maailma!")
```

**📤 Tulostus:**

```
Hei maailma!
```

🧠 Tässä `end=" "` tarkoittaa, että rivinvaihdon sijaan tulostuksen loppuun lisätään välilyönti.

---

## 🔁 Erottimen muuttaminen – `sep`-parametri

`sep` määrittää **mitä merkkiä käytetään** argumenttien välissä.
Oletuksena `sep=" "` (välilyönti), mutta sen voi muuttaa:

```python
print("omena", "banaani", "appelsiini", sep=", ")
```

**📤 Tulostus:**

```
omena, banaani, appelsiini
```

---

## 🧮 Laskutoimitusten tulostaminen

`print()` voi tulostaa myös laskujen tuloksia.

```python
print("5 + 3 =", 5 + 3)
```

**📤 Tulostus:**

```
5 + 3 = 8
```

---

## 🪄 F-merkkijonot – tyylikäs tapa yhdistää tekstiä ja muuttujia

`print()` toimii erinomaisesti yhdessä **f-stringien** kanssa.

```python
nimi = "Ville"
ikä = 47
print(f"Hei {nimi}, olet {ikä} vuotta vanha.")
```

**📤 Tulostus:**

```
Hei Ville, olet 47 vuotta vanha.
```

💡 F-merkkijonot ovat erittäin hyödyllisiä, koska ne tekevät tulosteesta luettavamman ja selkeämmän.

---

## 🧠 Tulostaminen ilman rivinvaihtoa useissa kohdissa

Jos haluat tulostaa **samalle riville useassa vaiheessa**, voit käyttää `end=""`.

```python
for i in range(3):
    print(i, end=" ")
```

**📤 Tulostus:**

```
0 1 2
```

---

## 🧱 Erikoismerkit `\n`, `\t`, jne.

Tulostuksessa voit käyttää **escape-merkkejä** erikoisrakenteiden lisäämiseen:

| Merkki | Selitys     | Esimerkki                 | Tulostus       |
| ------ | ----------- | ------------------------- | -------------- |
| `\n`   | Rivinvaihto | `print("Hei\nmaailma")`   | Hei<br>maailma |
| `\t`   | Sarkain     | `print("Omena\tBanaani")` | Omena Banaani  |
| `\\`   | Takakeno    | `print("C:\\tiedosto")`   | C:\tiedosto    |

---

## 📚 `print()` teknisesti

Funktio `print()` on määritelty seuraavasti:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

**Selitykset:**

| Parametri  | Selitys                                              |
| ---------- | ---------------------------------------------------- |
| `*objects` | Tulostettavat kohteet (yksi tai useampi)             |
| `sep`      | Erottaa useat arvot (oletus on välilyönti)           |
| `end`      | Mitä lisätään tulosteen loppuun (oletus rivinvaihto) |
| `file`     | Mihin tulostetaan (oletus on konsoli)                |
| `flush`    | Tyhjennetäänkö puskurit heti (harvoin tarvitaan)     |

---

## 🧭 Esimerkki kaikilla parametreilla

```python
import sys

print("A", "B", "C", sep="-", end="!", file=sys.stdout, flush=True)
```

**📤 Tulostus:**

```
A-B-C!
```

---

## ✨ Yhteenveto

| Ominaisuus          | Selitys                   | Esimerkki                  |
| ------------------- | ------------------------- | -------------------------- |
| Perustulostus       | Tulostaa tekstiä          | `print("Hei")`             |
| Useat arvot         | Tulostaa useita objekteja | `print("A", "B")`          |
| Erottimen vaihto    | Muuttaa väliä             | `print("A", "B", sep=",")` |
| Rivinvaihdon poisto | Tulostaa samalle riville  | `print("A", end="")`       |
| F-merkkijono        | Lisää muuttujat tekstiin  | `print(f"Nimi: {nimi}")`   |

---

# ✂️ Pythonin `split()`-metodi

`split()` on **merkkijono-olioiden (`str`) metodi**, joka **jakaa merkkijonon osiin** tietyn **erottimen (delimiter)** perusteella.
Tuloksena saadaan **lista**, jossa on merkkijonon osat erillisinä alkioina.

---

## 🔹 Peruskäyttö

```python
teksti = "omena päärynä banaani"
hedelmät = teksti.split()

print(hedelmät)
```

**📤 Tulostus:**

```
['omena', 'päärynä', 'banaani']
```

🧠 `split()` jakaa merkkijonon osiin (`Listatyyppiseksi` 👉 Voidaan käyttää alkioita) **välilyönnin** kohdalta, jos erottinta ei erikseen määritellä.

---

## 🔸 Määritä oma erotin

Voit määrittää haluamasi merkin tai merkkijonon, jonka kohdalta jako tapahtuu.

```python
teksti = "omena,päärynä,banaani"
hedelmät = teksti.split(",")
print(hedelmät)
```

**📤 Tulostus:**

```
['omena', 'päärynä', 'banaani']
```

💡 Nyt jako tapahtuu pilkun (`,`) kohdalta eikä välilyönnistä.

---

## ⚙️ Erotin voi olla mikä tahansa merkki

```python
teksti = "opiskelija;ohjelmoija;kehittäjä"
sanat = teksti.split(";")
print(sanat)
```

**📤 Tulostus:**

```
['opiskelija', 'ohjelmoija', 'kehittäjä']
```

---

## 🔢 Rajoita jakokertojen määrä (`maxsplit`)

`split()` voi ottaa toisen valinnaisen argumentin: 👉 `maxsplit`, joka määrittää **kuinka monta kertaa jako tehdään**.

```python
teksti = "a b c d e"
osat = teksti.split(" ", 2)
print(osat)
```

**📤 Tulostus:**

```
['a', 'b', 'c d e']
```

🧠 Tässä jako tehdään vain **kahdesti**, joten viimeinen osa jää kokonaiseksi.

---

## 🧹 Välilyöntien käsittely

Jos merkkijonossa on useita välilyöntejä peräkkäin, `split()` käsittelee ne automaattisesti yhtenä erottimena, **jos et määritä erottajaa**.

```python
teksti = "Python   on    hauskaa"
sanat = teksti.split()
print(sanat)
```

**📤 Tulostus:**

```
['Python', 'on', 'hauskaa']
```

💡 Tämä tekee `split()`-metodista kätevän esimerkiksi, kun käsitellään tekstirivejä, joissa on vaihtelevasti välilyöntejä.

---

## 📄 Käytännön esimerkki – tiedoston käsittely

Kuvitellaan, että luet tiedostosta varausjärjestelmän rivin:

```python
rivi = "Huone101|2025-11-05|Ville Heikkiniemi|0401234567|ville@example.com"
tiedot = rivi.split("|")

print(tiedot)
```

**📤 Tulostus:**

```
['Huone101', '2025-11-05', 'Ville Heikkiniemi', '0401234567', 'ville@example.com']
```

Tämän jälkeen voit käsitellä tietoja yksittäin:

```python
huone = tiedot[0]
päivä = tiedot[1]
nimi = tiedot[2]

print(f"Varaus: {nimi} varasi {huone} päivälle {päivä}")
```

**📤 Tulostus:**

```
Varaus: Ville Heikkiniemi varasi Huone101 päivälle 2025-11-05
```

---

## 🧭 `split()` vs. `rsplit()`

`rsplit()` toimii samoin kuin `split()`, mutta se **alkaa jakamisen oikeasta reunasta** (”reverse split”).

```python
teksti = "a,b,c,d,e"
print(teksti.split(",", 2))   # jakaa vasemmalta
print(teksti.rsplit(",", 2))  # jakaa oikealta
```

**📤 Tulostus:**

```
['a', 'b', 'c,d,e']
['a,b,c', 'd', 'e']
```

---

## ⚠️ Tyhjä merkkijono

Jos `split()` saa tyhjän merkkijonon ilman erottimia, tulos on tyhjä lista.

```python
print("".split())
```

**📤 Tulostus:**

```
[]
```

---

## 🧩 Yhteenveto

| Ominaisuus          | Selitys             | Esimerkki                 | Tulostus            |
| ------------------- | ------------------- | ------------------------- | ------------------- |
| Oletuserotin        | Välilyönti          | `"a b c".split()`         | `['a', 'b', 'c']`   |
| Oma erotin          | Itse valittu merkki | `"a,b,c".split(",")`      | `['a', 'b', 'c']`   |
| Jakomäärän rajoitus | `maxsplit`          | `"a b c d".split(" ", 2)` | `['a', 'b', 'c d']` |
| Useat välilyönnit   | Käsitellään yhtenä  | `"a   b".split()`         | `['a', 'b']`        |
| Tyhjä merkkijono    | Tyhjä lista         | `"".split()`              | `[]`                |

---

**🧠 `split()`:**

* on **merkkijono-olioiden metodi**
* **jakaa tekstin osiin** annetun erottimen perusteella
* **palauttaa listan**
* toimii tehokkaasti tiedostojen, lokien ja tekstisyötteiden käsittelyssä