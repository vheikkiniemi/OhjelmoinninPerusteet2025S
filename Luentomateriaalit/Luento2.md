> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla.

# 🧩 Miksi ohjelmissa tarvitaan erilaisia tietotyyppejä?

## 1. Mitä tietotyyppi tarkoittaa?

Tietotyyppi (engl. *data type*) määrittelee, **millaisia arvoja muuttuja voi sisältää** ja **mitä operaatioita** arvoilla voidaan suorittaa.
Tietotyypit ovat ohjelmoinnin perusperiaatteita – ne kertovat tietokoneelle, miten dataa käsitellään.

> Esimerkiksi numeroilla voidaan laskea, mutta tekstillä ei voi suoraan laskea yhteen.

---

## 2. Miksi tietotyyppejä tarvitaan?

Tietokone käsittelee kaikkea lopulta bitteinä (0 ja 1).
Ohjelmoijan tehtävä on kertoa, **millä tavalla näitä bittejä tulisi tulkita**.

### 💡 Esimerkki:

```
01000001
```

* Jos tulkitaan **merkkinä (char)** → se on kirjain `A`
* Jos tulkitaan **lukuna (int)** → se on arvo `65`

Eli sama bittijono voi tarkoittaa eri asioita riippuen tietotyypistä.
Tietotyyppi siis **antaa merkityksen datalle.**

---

## 3. Tietotyypit auttavat ohjelmaa toimimaan oikein

Ilman tietotyyppejä ohjelma ei tietäisi:

* kuinka paljon muistia varata
* millaisia laskutoimituksia on sallittua tehdä
* miten tieto näytetään ruudulla tai tallennetaan

### 🔍 Esimerkki Pythonissa:

```python
a = 5        # kokonaisluku (int)
b = 2.5      # desimaaliluku (float)
c = "5"      # teksti (str)

print(a + b)     # toimii → tulos 7.5
print(a + c)     # virhe → ei voi laskea int + str
```

---

## 4. Eri tietotyypit palvelevat eri tarkoituksia

| Tietotyyppi | Esimerkki                    | Käyttötarkoitus              |
| ----------- | ---------------------------- | ---------------------------- |
| `int`       | 10                           | laskutoimitukset, laskurit   |
| `float`     | 3.14                         | desimaalit, mittaukset       |
| `str`       | "Hei maailma"                | tekstit, nimet, viestit      |
| `bool`      | True / False                 | ehtojen tarkistus, päätökset |
| `list`      | [1, 2, 3]                    | useiden arvojen tallennus    |
| `dict`      | {"nimi": "Ville", "ikä": 35} | avain–arvo-parit             |

---

## 5. Tietotyyppien avulla ohjelma on luotettavampi

Kun käytetään oikeita tietotyyppejä:  
✅ Virheiden määrä pienenee  
✅ Koodi on helpompi lukea ja ylläpitää  
✅ Ohjelman suoritus on tehokkaampaa  
✅ Tietoturva paranee (ei voi käsitellä vääränlaista tietoa)

---

## 6. Käytännön analogia 🧠

Ajattele tietotyyppejä **astioina keittiössä**:

| Astia         | Vastaa tietotyyppiä | Mitä siihen voi laittaa   |
| ------------- | ------------------- | ------------------------- |
| Vesilasi      | `float`             | vettä, mehua (nestettä)   |
| Leipälautanen | `str`               | leipää, juustoa (tekstiä) |
| Mittakuppi    | `int`               | kokonaisia mittoja        |

Jos yrität kaataa mehua lautaselle, se ei toimi — aivan kuten yrittäisit laskea yhteen tekstin ja numeron ohjelmassa!

---

## 7. Yhteenveto ✨

**Erilaisia tietotyyppejä tarvitaan, jotta:**

* tietokone tietää, mitä tietoa käsitellään
* ohjelma osaa käyttää muistia ja laskutoimituksia oikein
* virheet voidaan havaita aikaisessa vaiheessa
* koodi pysyy selkeänä ja luotettavana

> ➕ Tietotyypit ovat ohjelmoinnin rakennuspalikoita — ilman niitä ohjelmat olisivat vain sekava kokoelma bittejä!

---

# 🧩 Tietotyypit käytännössä – esimerkkinä varausjärjestelmä

Kuvitellaan, että rakennamme pienen **varausjärjestelmän**, jossa käyttäjät voivat varata esimerkiksi **kokoustiloja** tai **muita resursseja**.

Ohjelma tarvitsee monenlaista tietoa:

* Kuka varaa
* Mitä varataan
* Milloin varataan
* Onko varaus vahvistettu

Näitä kaikkia kuvataan **erilaisilla tietotyypeillä**.

---

## 🧍 1. Käyttäjätiedot → *merkkijono (`str`)* ja *kokonaisluku (`int`)*

Käyttäjän nimi, sähköposti ja tunnus tallennetaan tekstinä (merkkijonona).
Jos käyttäjällä on ikä tai tunnistenumero, ne ovat kokonaislukuja.

```python
user_name = "Mika Virtanen"        # str
user_email = "mika@virtanen.com"   # str
user_age = 22                 # int
```

➡️ Näitä käytetään tunnistamaan varaaja ja mahdollisesti tarkistamaan, että hän on esimerkiksi yli 15-vuotias.

---

## 🕒 2. Varausaika → *päivämäärä ja kellonaika (`datetime`)*

Jokaisella varauksella on **alku- ja loppuaika**.
Pythonissa niitä voidaan käsitellä `datetime`-tyypillä, joka mahdollistaa vertailun ja laskutoimitukset.

```python
from datetime import datetime

start_time = datetime(2025, 10, 30, 14, 0)
end_time = datetime(2025, 10, 30, 16, 0)
```

➡️ Näillä voidaan tarkistaa, menevätkö varaukset päällekkäin.

---

## 🏠 3. Varattava resurssi → *merkkijono (`str`)*

Varattavan resurssin nimi tai tunniste on yleensä teksti:

```python
resource_name = "Kokoushuone A"  # str
```

Jos resursseilla on **kapasiteetti** (esim. 10 henkilöä), se voidaan tallentaa kokonaislukuna:

```python
capacity = 10  # int
```

---

## ✅ 4. Varaus vahvistettu tai ei → *totuusarvo (`bool`)*

Onko varaus hyväksytty, peruttu tai vielä odottamassa vahvistusta?
Tätä varten käytetään `bool`-tyyppiä.

```python
confirmed = True    # varaus on vahvistettu
canceled = False    # varaus ei ole peruttu
```

➡️ Tällaiset tiedot auttavat näyttämään käyttöliittymässä vain voimassa olevat varaukset.

---

## 📋 5. Varauslistat → *lista (`list`)*

Järjestelmässä on yleensä useita varauksia.
Ne voidaan tallentaa listaan, jolloin voidaan helposti käydä läpi kaikki varaukset:

```python
reservations = ["Varaus 1", "Varaus 2", "Varaus 3"]
```

Tai listana olioita / sanakirjoja, jos halutaan säilyttää enemmän tietoa:

```python
reservations = [
    {"user": "Mika", "resource": "Kokoushuone A", "time": "14:00-16:00"},
    {"user": "Satu", "resource": "Kokoushuone B", "time": "12:00-13:00"}
]
```

---

## 🧠 6. Yksi varaus → *sanakirja (`dict`)*

Yksittäisen varauksen kaikki tiedot voidaan koota yhteen sanakirjaan:

```python
reservation = {
    "user_name": "Mika Virtanen",   # str
    "resource": "Kokoushuone A",       # str
    "start": datetime(2025, 10, 30, 14, 0),  # datetime
    "end": datetime(2025, 10, 30, 16, 0),
    "confirmed": True,                 # bool
    "participants": 4                  # int
}
```

➡️ Tämä on kätevä, koska kaikki varauksen osat ovat yhdessä rakenteessa.

---

## 🧱 7. Yhteenvetona käytetyt tietotyypit

| Tietotyyppi | Käyttötarkoitus                      | Esimerkki                               |
| ----------- | ------------------------------------ | --------------------------------------- |
| `str`       | Nimet, sähköpostit, resurssien nimet | `"Mika Virtanen"`, `"Kokoushuone A"` |
| `int`       | Ikä, kapasiteetti, tunnisteet        | `22`, `10`, `12345`                     |
| `float`     | Hinta tai tuntimäärä                 | `2.5` tuntia                            |
| `bool`      | Onko varaus vahvistettu, peruttu     | `True`, `False`                         |
| `datetime`  | Varausaika                           | `datetime(2025, 10, 30, 14, 0)`         |
| `list`      | Useat varaukset tai käyttäjät        | `[varaus1, varaus2, ...]`               |
| `dict`      | Yhden varauksen tiedot yhdessä       | `{"user": ..., "resource": ...}`        |

---

## 💬 8. Miksi tämä on tärkeää?

Kun varausjärjestelmä käyttää **oikeita tietotyyppejä**, ohjelma toimii oikein ja luotettavasti:

 * Päällekkäiset varaukset voidaan estää ajallisesti (`datetime`)   
 * Käyttäjän tunnistaminen onnistuu tekstin perusteella (`str`)   
 * Kapasiteettia voidaan verrata numeroina (`int`)   
 * Varauslogiikka toimii selkeästi (`bool`)   

---

## 🧩 Esimerkin kokonaisuus

```python
from datetime import datetime

reservation = {
    "user_name": "Mika Virtanen",
    "resource": "Kokoushuone A",
    "start": datetime(2025, 10, 30, 14, 0),
    "end": datetime(2025, 10, 30, 16, 0),
    "confirmed": True,
    "participants": 4
}

print(f"Varaus: {reservation['resource']} klo {reservation['start'].strftime('%H:%M')}–{reservation['end'].strftime('%H:%M')}")
```

📤 Tulostus:

```
Varaus: Kokoushuone A klo 14:00–16:00
```

---

# 🧩 Pythonin tietotyypit esimerkeillä

Pythonissa kaikki on olioita — myös tietotyypit.
Tietotyyppi kertoo, **millaista tietoa muuttuja sisältää** ja **miten sitä voidaan käsitellä**.

---

## 🔢 1. Kokonaisluvut – `int`

Kokonaisluvut ovat numeroita ilman desimaaleja.

```python
age = 25
students = 32
year = 2025

print(age + 5)      # 30
print(year - 2000)  # 25
print(students * 2) # 64
```

💡 **Käyttö:** laskurit, iät, määrät, tunnisteet  
📏 **Esimerkki:** käyttäjän ikä, varattujen paikkojen määrä

---

## 💧 2. Desimaaliluvut – `float`

Desimaaliluvut sisältävät murto-osia.
Ne soveltuvat mittauksiin ja rahamäärien laskentaan.

```python
temperature = 21.5
price = 9.99
duration = 2.5  # tuntia

print(temperature + 2.0)  # 23.5
print(price * 2)          # 19.98
```

💡 **Käyttö:** hinnat, mittaukset, prosentit  
📏 **Esimerkki:** varauksen kesto tunneissa

---

## ⚙️ 3. Kompleksiluvut – `complex`

`complex`-tyyppiä käytetään matemaattisiin laskuihin, joissa on **reaali- ja imaginaariosa**.
Harvemmin käytössä perusohjelmoinnissa, mutta tärkeä tieteellisessä laskennassa.

```python
z = 3 + 4j
print(z.real)  # 3.0
print(z.imag)  # 4.0
print(z * 2)   # (6+8j)
```

💡 **Käyttö:** sähkötekniikka, fysiikka, signaalinkäsittely  
📏 **Esimerkki:** jännitteen ja virran kompleksimuodot

---

## 🧵 4. Merkkijonot – `str`

Merkkijonot tallentavat tekstiä.
Voidaan yhdistää, muotoilla ja hakea osia.

```python
name = "Mika Virtanen"
room = 'Kokoushuone A'

print("Tervetuloa, " + name + "!")
print(f"Varaus tehty tilaan {room}.")
```

💡 **Käyttö:** nimet, sähköpostit, tekstitiedot  
📏 **Esimerkki:** resurssin nimi, käyttäjän sähköposti

---

## ✅ 5. Totuusarvot – `bool`

`bool` kertoo onko jokin ehto **tosi (True)** tai **epätosi (False)**.

```python
confirmed = True
over_15 = False

if confirmed:
    print("Varaus vahvistettu ✅")
else:
    print("Varaus odottaa hyväksyntää ❌")
```

💡 **Käyttö:** päätökset, ehdot, loogiset tarkistukset  
📏 **Esimerkki:** onko käyttäjä yli 15-vuotias

---

## 📋 6. Listat – `list`

Lista on **järjestetty ja muokattava** kokoelma arvoja.

```python
reservations = ["A", "B", "C"]

print(reservations[0])  # A
reservations.append("D")
print(reservations)     # ["A", "B", "C", "D"]
```

💡 **Käyttö:** useiden arvojen tallennus, toistuvat rakenteet  
📏 **Esimerkki:** lista kaikista varauksista

---

## 🗂️ 7. Sanakirjat – `dict`

Sanakirjassa on **avain–arvo-parit**, kuten JSON:issa.

```python
reservation = {
    "user": "Mika Virtanen",
    "room": "Kokoushuone A",
    "confirmed": True
}

print(reservation["user"])  # Mika Virtanen
```

💡 **Käyttö:** tietorakenteet, API-data, tietokantaobjektit  
📏 **Esimerkki:** yksittäinen varaus

---

## 📦 8. Tuplet – `tuple`

Tuple muistuttaa listaa, mutta on **muuttumaton**.

```python
time_slot = ("14:00", "16:00")

print(time_slot[0])  # 14:00
# time_slot[0] = "13:00"  # ❌ Virhe
```

💡 **Käyttö:** pysyvät arvot, koordinaatit, aikavälit  
📏 **Esimerkki:** varauksen alku- ja loppuaika

---

## 🧮 9. Joukot – `set`

`set` sisältää **vain uniikkeja arvoja**, eikä säilytä järjestystä.

```python
resources = {"A", "B", "A"}
print(resources)  # {"A", "B"}

resources.add("C")
print(resources)  # {"A", "B", "C"}
```

💡 **Käyttö:** duplikaattien poistaminen, joukko-operaatiot  
📏 **Esimerkki:** uniikit resurssit

---

## 🧩 10. Joukkojen sanakirja – `frozenset`

`frozenset` on kuten `set`, mutta **muuttumaton**.

```python
permissions = frozenset({"view", "edit"})
# permissions.add("delete")  # ❌ Virhe
```

💡 **Käyttö:** pysyvät joukkoarvot, esim. käyttöoikeudet

---

## 🕹️ 11. Range – `range`

`range` tuottaa sarjan kokonaislukuja, usein silmukoissa.

```python
for i in range(3):
    print(i)
# 0, 1, 2
```

💡 **Käyttö:** toistolauseet, laskurit  
📏 **Esimerkki:** tuntien läpikäynti varauspäivänä

---

## 🧱 12. Bytes ja Bytearray – `bytes`, `bytearray`

Käytetään binääridatan tallentamiseen, kuten tiedostoihin ja verkon yli lähetettävään dataan.

```python
data = b"Hello"
print(data[0])  # 72 (ASCII-koodi)

mutable_data = bytearray(b"Hi")
mutable_data[0] = 65  # 'A'
print(mutable_data)   # bytearray(b'Ai')
```

💡 **Käyttö:** tiedonsiirto, tiedostojen käsittely, kryptografia

---

## 🚫 13. NoneType – `None`

`None` tarkoittaa **ei arvoa**.
Se on Pythonin tapa kuvata tyhjyyttä tai määrittelemättömyyttä.

```python
result = None

if result is None:
    print("Ei tulosta vielä saatavilla.")
```

💡 **Käyttö:** palautusarvot, alustamattomat muuttujat  
📏 **Esimerkki:** varaus ei ole vielä vahvistettu → `confirmed = None`

---

## 🧠 14. Yhteenvetotaulukko

| Tietotyyppi | Kuvaus                 | Muokattavissa | Esimerkki            | Tyypillinen käyttö       |
| ----------- | ---------------------- | ------------- | -------------------- | ------------------------ |
| `int`       | Kokonaisluku           | ✅             | `42`                 | laskurit, määrät         |
| `float`     | Desimaaliluku          | ✅             | `3.14`               | hinnat, mittaukset       |
| `complex`   | Kompleksiluku          | ✅             | `3+4j`               | tekninen laskenta        |
| `str`       | Teksti                 | ✅             | `"Hei"`              | nimet, viestit           |
| `bool`      | Totuusarvo             | ✅             | `True`               | ehdot, tarkistukset      |
| `list`      | Järjestetty kokoelma   | ✅             | `[1, 2, 3]`          | moniarvoinen data        |
| `tuple`     | Muuttumaton lista      | ❌             | `(1, 2)`             | pysyvät arvot            |
| `set`       | Uniikit arvot          | ✅             | `{1, 2, 3}`          | joukko-operaatiot        |
| `frozenset` | Muuttumaton joukko     | ❌             | `frozenset({1, 2})`  | pysyvät oikeudet         |
| `dict`      | Avain–arvo-parit       | ✅             | `{"nimi": "Eemeli"}` | tietorakenne             |
| `range`     | Sarja kokonaislukuja   | ✅             | `range(0, 5)`        | silmukat                 |
| `bytes`     | Binaaridata            | ❌             | `b"Hello"`           | tiedonsiirto             |
| `bytearray` | Muokattava binaaridata | ✅             | `bytearray(b"Hi")`   | muokattava data          |
| `NoneType`  | Ei arvoa               | —             | `None`               | alustamattomat muuttujat |

---

## 🧩 15. Esimerkkiohjelma: tietotyypit varausjärjestelmässä

```python
from datetime import datetime

reservation = {
    "user": "Mika Virtanen",   # str
    "age": 22,                    # int
    "room": "Kokoushuone A",      # str
    "start": datetime(2025, 10, 30, 14, 0),
    "end": datetime(2025, 10, 30, 16, 0),
    "confirmed": None,            # NoneType (ei vielä hyväksytty)
    "price": 25.50,               # float
    "participants": ["Satu", "Antti", "Joonas"], # list
    "time_slot": ("14:00", "16:00"),  # tuple
    "permissions": frozenset({"view"}), # frozenset
}

print(f"{reservation['user']} varasi huoneen {reservation['room']} klo {reservation['time_slot'][0]}–{reservation['time_slot'][1]}")
if reservation["confirmed"] is None:
    print("Varaus odottaa vahvistusta ⏳")
```

📤 **Tulostus:**

```
Mika Virtanen varasi huoneen Kokoushuone A klo 14:00–16:00
Varaus odottaa vahvistusta ⏳
```

---

## ✨ Yhteenveto

Pythonin tietotyypit kattavat kaiken:  

🔹 Numerot (`int`, `float`, `complex`)  
🔹 Teksti ja logiikka (`str`, `bool`)  
🔹 Kokoelmat (`list`, `tuple`, `set`, `dict`)  
🔹 Erikoistapaukset (`range`, `bytes`, `NoneType`, `frozenset`)

> 🎯 Kun osaat valita oikean tietotyypin, ohjelmasi on nopeampi, virheettömämpi ja helpompi ymmärtää.

---

# 🔄 Pythonin tietotyyppimuunnokset (Type conversions)

Python on **dynaamisesti tyypitetty kieli**, mikä tarkoittaa, että muuttujan tietotyyppi määräytyy automaattisesti sen arvon perusteella.
Kuitenkin ohjelmoijan täytyy usein **muuttaa tietotyyppi toiseen**, jotta dataa voidaan käsitellä oikein.

---

## 🧠 1. Miksi tietotyyppimuunnoksia tarvitaan?

Usein ohjelmassa joudutaan käsittelemään tietoa eri muodoissa:

* 🧾 **Käyttäjän syöte** tulee aina tekstinä (`str`)
* ➕ **Laskutoimitukset** onnistuvat vain numeroilla (`int` tai `float`)
* ✅ **Totuusarvot** (`bool`) tarvitaan ehtoihin
* 🔢 **Tulosteet** yhdistävät tekstiä ja numeroita

> 👉 Tällöin täytyy muuntaa tyyppi toiseen ennen käyttöä.

---

## 🧩 2. Kaksi tapaa muuntaa tyyppiä

### 1️⃣ Epäsuora muunnos (*implicit conversion*)

Python tekee sen automaattisesti, kun se on turvallista.

```python
num_int = 5
num_float = 2.5
result = num_int + num_float  # int → float

print(result)      # 7.5
print(type(result))  # <class 'float'>
```

💡 Tässä Python muutti `int`-arvon automaattisesti `float`-arvoksi, jotta lasku onnistuisi ilman tietohäviötä.

---

### 2️⃣ Suora muunnos (*explicit conversion*)

Ohjelmoija tekee muutoksen itse käyttäen muunnosfunktioita kuten:

```python
int()   float()   str()   bool()   list()   tuple()   set()
```

---

## 🔢 3. Muunnos numeroiksi (`int`, `float`)

### 🔸 Teksti → kokonaisluku (`int`)

```python
text = "42"
num = int(text)
print(num + 1)   # 43
```

### 🔸 Teksti → desimaaliluku (`float`)

```python
price_text = "19.99"
price = float(price_text)
print(price * 2)  # 39.98
```

💡 **Muista:** Tekstin on oltava *oikeassa muodossa*, muuten tulee virhe:

```python
int("42a")  # ❌ ValueError
```

---

## 🧮 4. Muunnos tekstiksi (`str`)

Kaikki arvot voidaan muuttaa merkkijonoksi:

```python
age = 25
print("Ikä on " + str(age) + " vuotta.")
```

tai **f-merkkijonolla (suositeltu tapa)**:

```python
print(f"Ikä on {age} vuotta.")
```

💡 F-merkkijonot ovat nykyaikainen ja selkeä tapa yhdistää tekstiä ja eri tietotyyppejä.

---

## ✅ 5. Muunnos totuusarvoksi (`bool`)

Pythonissa lähes kaikki arvot voidaan tulkita todeksi tai epätodeksi.

| Arvo                                 | Tulkitsee |
| ------------------------------------ | --------- |
| `0`, `0.0`, `""`, `[]`, `{}`, `None` | `False`   |
| Kaikki muut                          | `True`    |

```python
print(bool(1))        # True
print(bool(0))        # False
print(bool(""))       # False
print(bool("Hello"))  # True
```

💡 Tätä käytetään usein ehtolauseissa:

```python
username = "Ville"
if username:
    print("Käyttäjänimi annettu")
```

---

## 📋 6. Muunnos kokoelmaksi (`list`, `tuple`, `set`)

Python mahdollistaa muunnokset eri kokoelmatyyppien välillä.

### 🔸 Tuple → List

```python
t = ("A", "B", "C")
lst = list(t)
print(lst)  # ['A', 'B', 'C']
```

### 🔸 List → Tuple

```python
lst = ["A", "B", "C"]
t = tuple(lst)
print(t)  # ('A', 'B', 'C')
```

### 🔸 List → Set (poistaa duplikaatit)

```python
lst = ["A", "A", "B"]
unique = set(lst)
print(unique)  # {'A', 'B'}
```

---

## 🧱 7. Muunnos binäärimuotoon (`bytes` ja `bytearray`)

```python
text = "Hello"
binary = bytes(text, "utf-8")
print(binary)  # b'Hello'

# takaisin tekstiksi
decoded = binary.decode("utf-8")
print(decoded)  # Hello
```

💡 **Käyttö:** tiedonsiirrossa, tiedostojen käsittelyssä, verkkosovelluksissa

---

## 🚫 8. Muunnos tyhjyyteen (`NoneType`)

Jos muuttujaan ei haluta vielä arvoa, käytetään `None`:

```python
result = None

if result is None:
    print("Ei tulosta vielä.")
```

---

## 🧠 9. Käytännön esimerkki – varausjärjestelmä

Käyttäjän syöte tulee tekstinä.
Ohjelma muuntaa sen oikeisiin tietotyyppeihin ennen käsittelyä.

```python
# Käyttäjän syötteet
participants_input = "5"
price_input = "12.50"
confirmed_input = "True"

# Muutetaan tietotyypit
participants = int(participants_input)
price = float(price_input)
confirmed = confirmed_input == "True"  # str → bool

total = participants * price

print(f"Osallistujia: {participants}, Yhteishinta: {total} €, Vahvistettu: {confirmed}")
```

📤 **Tulostus:**

```
Osallistujia: 5, Yhteishinta: 62.5 €, Vahvistettu: True
```

---

## 🧩 10. Yhteenvetotaulukko

| Muunnos                | Funktio                | Esimerkki        | Tulos     |
| ---------------------- | ---------------------- | ---------------- | --------- |
| Teksti → Kokonaisluku  | `int()`                | `int("5")`       | `5`       |
| Teksti → Desimaaliluku | `float()`              | `float("3.14")`  | `3.14`    |
| Numero → Teksti        | `str()`                | `str(42)`        | `"42"`    |
| Lista → Tuple          | `tuple()`              | `tuple([1,2,3])` | `(1,2,3)` |
| Tuple → Lista          | `list()`               | `list((1,2,3))`  | `[1,2,3]` |
| Lista → Set            | `set()`                | `set([1,1,2])`   | `{1,2}`   |
| Arvo → Totuusarvo      | `bool()`               | `bool("")`       | `False`   |
| Teksti → Binaariksi    | `bytes(text, "utf-8")` | `"A"`            | `b"A"`    |
| Binaari → Tekstiksi    | `decode()`             | `b"A".decode()`  | `"A"`     |

---

## ✨ 11. Yhteenveto

* 🧩 Python osaa joskus muuntaa tietotyypin automaattisesti (*implicit conversion*)
* 👨‍💻 Useimmiten ohjelmoijan täytyy tehdä se itse (*explicit conversion*)
* 💡 Muunnoksia tarvitaan, jotta eri tietotyyppejä voidaan yhdistää turvallisesti ja järkevästi

> 🎯 Oikea tietotyyppimuunnos on kuin tulkkaus — se varmistaa, että kaikki ohjelman osat "puhuvat samaa kieltä".

---