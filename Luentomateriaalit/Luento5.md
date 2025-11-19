> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla.

# 🐍 Silmukat Pythonissa

## 🔁 Mikä on silmukka?

Silmukka toistaa saman koodilohkon useita kertoja.

> [!NOTE]
> 💡 Ohjelma on itsessään jo silmukka. Pythonin `Main`-osasta käytetään nimeä pääsilmukka. `Main` voidaan suorittaa riviltä ja lopettaa suorittaminen viimeisen rivin jälkeen. Usein ohjelmat ovat kuitenkin sellaisia, että `Mainin` suorittaminen lopetetaan vasta erillisellä keskeytyksellä alla olevan esimerkin mukaisesti:

```py
import time

def main():
    print("Ohjelma käynnissä. Paina Ctrl+C lopettaaksesi.")
    try:
        while True:
            # Tee jotain tai odota
            print("Suoritetaan...")
            time.sleep(1)  # Odottaa 1 sekunnin
            pass  # Tyhjä silmukka
    except KeyboardInterrupt:
        print("\nKeskeytetty. Suljetaan ohjelma.")

if __name__ == "__main__":
    main()
```

---

Pythonissa tärkeimmät silmukat ovat:

* 🌀 **`for`** — käy läpi iteroitavan joukon (lista, merkkijono, range, tiedosto, jne.)  
* 🔂 **`while`** — toistaa niin kauan kuin ehto on tosi

---

## 🧩 `for`-silmukka käytännössä

**✅ Perusmuoto**

```py
for nimi in ["Anna", "Bashir", "Chen"]:
    print(f"Hei {nimi}!")
```

---

**🔢 `range()` → kokonaislukuvälit**

```py
for i in range(5):          # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2):   # 2,4,6,8
    print(i)
```

---

**🧮 `enumerate()` → sekä indeksi että arvo**

> [!NOTE]
> 💡 Opettele tämä! → Listojen kanssa mainio

```py
opiskelijat = ["Aino", "Ben", "Cai"]
for idx, nimi in enumerate(opiskelijat, start=1):
    print(idx, nimi)
```

---

**🔗 `zip()` → kulje rinnakkain useita jonoja**

```py
usernames = ["anna", "ben", "cai"]
roles = ["student", "admin", "student"]

for u, r in zip(usernames, roles):
    print(f"{u} → {r}")
```

---

**🗂 Iterointi sanakirjan yli**

```py
user = {"id": 17, "name": "Alex", "role": "student"}
for avain, arvo in user.items():
    print(avain, arvo)
```

---

## ⏳ `while`-silmukka → ehto-ohjattu toisto

> [!NOTE]
> 💡 Opettele tämä! **→ Ehdon täytyttyä suorittaminen lopetetaan.**

```py
saldo = 3
while saldo > 0:
    print("Käyttöoikeus voimassa.")
    saldo -= 1
print("Ei käyttöoikeutta.")
```

⚠️ **Varo:** jos ehto ei koskaan muutu epätodeksi → **loputon silmukka!** → CTRL-C monesti auttaa lopettamaan

---

## 🧭 `break`, `continue` ja silmukan `else`

* 🛑 **`break`** keskeyttää silmukan heti  
* ⏩ **`continue`** hyppää seuraavaan iteraatioon  
* 🧩 **`else`** suoritetaan vain, jos `break` ei tapahtunut  

```py
users = ["alice", "bob", "root", "carl"]
for u in users:
    if u == "root":
        print("Admin löytyi!")
        break
else:
    print("Adminia ei löytynyt.")
```
---

Jos jonkin alkion sisältö on tyhjä:

```py
rivit = ["Ville;08:00;huone101", "", "Anna;09:00;lab2"]
for r in rivit:
    if not r.strip():
        continue
    print("Käsitellään:", r)
```

---

## 🧱 Sisäkkäiset silmukat (nested loops)

```py
päivät = ["Ma", "Ti"]
ajat = ["08:00", "10:00"]
for p in päivät:
    for a in ajat:
        print(p, a)
```

> [!NOTE]
> 💡 Pidä silmukat lyhyinä ja tarvittaessa pilko loogisiin funktioihin.

---

## ⚡ Listan läpikäynti vs. list comprehension

**🧠 Perinteinen**

```py
numbers = [1, 2, 3, 4]
squared = []
for n in numbers:
    squared.append(n*n)
```

---

**✨ List comprehension (lyhyempi ja usein nopeampi)**

```py
numbers = [1, 2, 3, 4]
squared = [n*n for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
```

---

## 🧠 Hyvät käytännöt

✅ Älä muokkaa listaa samalla kun iteroit
✅ Käytä `enumerate()` selkeyden vuoksi
✅ Käytä `break` ja `continue` harkiten

---

## 🧱 Tyypillisiä käyttöskenaarioita

**🧮 Kertymä**

```py
total = 0
for price in [12.5, 8.0, 3.5]:
    total += price
```

---

**🔍 Haku**

```py
target = "ben"
for name in ["anna", "ben", "cai"]:
    if name == target:
        print("Löytyi!")
        break
```

---

**🎯 Suodatus**

```py
emails = ["a@x.com", "virhe", "b@y.com"]
valid = [e for e in emails if "@" in e]
```

---

**🧩 Rinnakkaiset listat**

```py
starts = ["08:00", "09:00", "10:00"]
rooms  = ["101", "202", "303"]
for s, r in zip(starts, rooms):
    print(f"{s} → huone {r}")
```

---

## 🧾 Checklist

| Asia                                            | Osaaminen |
| ----------------------------------------------- | --------- |
| 🔁 Ero `for` ja `while`                         | ✔️        |
| 🧮 `range`, `enumerate`, `zip`                  | ✔️        |
| 🧱 `break`, `continue`, `else`                  | ✔️        |
| 🔍 Peruskuviot (kertymä, haku, suodatus)        | ✔️        |
| ⚠️ Sudenkuopat (loputon while, listan muokkaus) | ✔️        |

---

## 🧠 Tiivistelmä → **muista nämä**

* `for`: käy läpi jono tai kokoelma
* `while`: toista ehtoon asti
* `break` ja `continue`: ohjaavat toistoa
* `else`: suoritetaan vain jos ei keskeytetty
* `List comprehensions`: tehokas ja selkeä

---

# 🚦 Ehtolauseet Pythonissa

## 📍 Miksi ehtolauseita käytetään?

Ohjelmoinnissa tehdään jatkuvasti päätöksiä:

* Mitä tapahtuu, jos käyttäjä kirjautuu sisään väärällä salasanalla?
* Mitä jos tiedoston rivi on tyhjä?
* Mitä jos varauspäivä on menneisyydessä?

👉 **Ehtolauseiden avulla ohjelma valitsee toteutettavan polun.**

---

Pythonissa avainrakenteet ovat:

* `if`
* `elif`
* `else`

---

## 🧩 Perusrakenne

```py
if ehto:
    # suoritetaan jos ehto on tosi
elif toinen_ehto:
    # suoritetaan jos edellinen ei ollut tosi, mutta tämä on
else:
    # suoritetaan jos mikään yllä olevista ehdoista ei ollut tosi
```

Esimerkki:

```py
ika = 17

if ika >= 18:
    print("Täysi-ikäinen")
else:
    print("Alaikäinen")
```

---

## 🔢 Yleisimmät vertailuoperaattorit

| Operaattori | Tarkoitus              | Esimerkki      |
| ----------- | ---------------------- | -------------- |
| `==`        | yhtäsuuri              | `a == 10`      |
| `!=`        | eri suuri              | `a != 5`       |
| `<`         | pienempi               | `ika < 15`     |
| `<=`        | pienempi tai yhtäsuuri | `hinta <= 100` |
| `>`         | suurempi               | `pisteet > 80` |
| `>=`        | suurempi tai yhtäsuuri | `ika >= 18`    |

---

## ⚙️ Loogiset operaattorit

Niillä yhdistetään ehtoja:

| Operaattori | Selite                      | Esimerkki                        |
| ----------- | --------------------------- | -------------------------------- |
| `and`       | molempien oltava tosi       | `ika >= 18 and rooli == "admin"` |
| `or`        | vähintään yhden oltava tosi | `pisteet > 90 or bonus == True`  |
| `not`       | kääntää arvon               | `not aktiivinen`                 |

Esimerkki:

```py
ika = 20
rooli = "student"

if ika >= 18 and rooli == "student":
    print("Täysi-ikäinen opiskelija")
```

---

## 📁 Ehtolauseet tiedoston käsittelyssä

Tämä tapa esiintyy varausjärjestelmissä, datan puhdistuksessa ja lokien lukemisessa **→ Kopioi koodi ja kysy AI-työkaluilta tarkennusta rivien ja komentojen toiminnasta**

```py
with open("varaukset.txt", "r", encoding="utf-8") as f:
    for rivi in f:
        rivi = rivi.strip()
        
        if not rivi:  # tyhjä rivi
            continue
        
        osat = rivi.split("|")
        if len(osat) != 4:
            print("⚠️ Virheellinen rivi:", rivi)
            continue
        
        nimi, pvm, aika, tila = osat
        
        if not tila.startswith("huone"):
            print("❌ Tila ei kelpaa:", tila)
            continue
        
        print(f"OK: {nimi} → {tila}")
```

---

**Ehtolauseilla voidaan (esim):**

* suodattaa virheelliset rivit
* varmistaa arvojen rakenne
* estää ohjelmaa kaatumasta

---

## 🧠 Ehtojen kirjoittaminen siististi (best practices)

**✔️ Hyvä**

```py
if käyttäjä and käyttäjä.is_admin:
    ...
```

---

**👉 Mitä tekee?**

1. `if käyttäjä`

   * Tarkistaa, että `käyttäjä`-muuttuja **ei ole tyhjä** (ei None, ei False, ei tyhjä merkkijono, ei tyhjä dict/list).
   * Pythonissa tämä on “pythonic” tapa tarkistaa olemassaolo.

2. `käyttäjä.is_admin`

   * Tarkistaa suoraan onko käyttäjä admin.
   * Ei tarvitse verrata arvoa `True`:aan, koska jos `is_admin` on boolean, se toimii suoraan ehtona.

---

**⭐ Miksi on hyvä?**

* Lyhyt ja selkeä
* Pythonissa hyväksytty ja idiomaattinen tapa
* Ehtolauseen lukeminen on helppoa:
  **“Jos käyttäjä on olemassa JA on admin…”**
* Välttää turhaa koodia
* Ei vertaa boolean-arvoa booleaniin

---

**❌ Huono**

```py
if käyttäjä != None and käyttäjä.is_admin == True:
    ...
```

---

**👉 Mikä on ongelmaa?**

1. **Turha vertailu `!= None`**

   * Pythonissa `if käyttäjä` riittää.
   * `!= None` on kömpelö ja ei-idiomaattinen.
   * Pitäisi käyttää `is not None` jos haluaa olla formaali.

2. **Turha vertailu `== True`**

   * Boolean-arvoja ei tarvitse verrata True/False-arvoihin.
   * Riittää `if käyttäjä.is_admin`.

3. **Koodi on pidempi ja vaikeampi lukea**

   * Lisäsanat eivät tarjoa lisäarvoa.
   * Tekee koodista raskaamman ja aloittelijamaisemman.

4. **Logiikka ei ole yhtä turvallinen**

   * Jos `käyttäjä` on `None`, Python evaluoi `käyttäjä != None` ensin → OK
   * Mutta jos ehtoja joskus muutetaan väärin, voi johtaa virheisiin kuten
     `"NoneType" object has no attribute "is_admin"`.

---

**🛑 Yhteenveto huonoista puolista**

* liikaa tekstiä
* vähemmän Python-tyylistä
* tekee boolean-vertailut väärällä tavalla
* ei lisää turvallisuutta
* vaikeampi lukea ja ylläpitää

---

**📝 Vinkkejä**

* Käytä **selkeitä ehtoja** (vältä liian pitkiä yhdistelmiä)
* Pilko ehtoja tarvittaessa apumuuttujiin

---

## 🎯 Sisäkkäiset ehtolauseet (nested if)

```py
ika = 20
jäsen = True

if ika >= 18:
    if jäsen:
        print("Pääsy sallittu")
    else:
        print("Jäsenyyttä vaaditaan")
else:
    print("Alaikäinen")
```

> [!NOTE]
> 💡  Jos sisäkkäisiä ehtoja alkaa olla liikaa, harkitse `elif`-rakenteen käyttöä tai logiikan pilkkomista funktioihin.

---

## 🚦 Ehtolauseet merkkijonojen käsittelyssä

```py
email = "test@example.com"

if "@" in email:
    print("Sähköposti kelpaa")
else:
    print("⚠️ Virheellinen sähköposti")
```

```py
nimi = ""

if not nimi:
    print("Nimi puuttuu")
```

---

## 🔀 Ternary-operaatio (lyhyt if)

Kompakti tapa valita arvo:

```py
ika = 20
status = "aikuinen" if ika >= 18 else "lapsi"
print(status)
```

---

## 📊 Ehtolauseet ja numerot

```py
pisteet = 85

if pisteet >= 90:
    print("Erinomainen")
elif pisteet >= 75:
    print("Hyvä")
elif pisteet >= 50:
    print("Kohtalainen")
else:
    print("Hylätty")
```

---

## 🏁 Yhteenveto

📌 Ehtolauseet ovat keskeinen osa ohjelman päätöksentekoa. Niillä voidaan:

* suodattaa syötteitä
* tarkistaa arvoja
* estää virheitä
* ohjata ohjelman kulku oikeille poluille

> [!NOTE]
> 💡 Kun yhdistät ehtolauseet silmukoihin ja tiedostonkäsittelyyn, pystyt rakentamaan vakaampia ja virheensietoisempia ohjelmia → Kuten varausjärjestelmiä

---

# 🧩 Käytännön esimerkkejä

**Listan tulostus ilman viimeistä viimeistä -merkkiä**

```py
def tulosta_lista():
    lista = ["omena", "banaani", "päärynä", "kiivi"]
    print("Hedelmät: ", end="")
    for i in range(len(lista)):
        if i < len(lista) - 1:
            print(lista[i], end="-")
        else:
            print(lista[i])  # Viimeinen alkio ilman '-'

def main():
    tulosta_lista()

if __name__ == "__main__":
    main()
```

**Sama kuin edellinen, mutta Join-metodilla**

```py
def tulosta_lista():
    lista = ["omena", "banaani", "päärynä", "kiivi"]
    print("Hedelmät: ", end="")
    print("-".join(lista))


def main():
    tulosta_lista()

if __name__ == "__main__":
    main()
```