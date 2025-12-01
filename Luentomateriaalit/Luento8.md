> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla.

# 📥 Inputit osana ohjelmointia

## 🧠 Miksi ohjelmissa tarvitaan inputteja?

Kaikki ohjelmat ratkaisevat jonkin ongelman. Jotta ohjelma voi ratkaista ongelman, sen on saatava **tietoa käyttäjältä**, ympäristöstä tai toisesta järjestelmästä. Tätä tietoa kutsutaan **syötteeksi (input)**.

Input mahdollistaa esimerkiksi:

* nimen, iän, osoitteen tai muun tekstin antamisen
* valintojen tekemisen (k/e, kyllä/ei)
* numeroiden syöttämisen laskentaa varten
* tiedostojen valitsemisen
* lomakkeen lähettämisen verkkosivulla
* toiminnon käynnistämisen (esim. “Aloita varaus”, “Lähetä tilaus”)
* päätöksenteon (mitä ohjelma tekee seuraavaksi)

Ilman inputteja ohjelma olisi aina **täysin staattinen** → Se suorittaisi täsmälleen saman asian joka kerta muuttumattomalla datalla.

---

## 📦 Inputin erilaiset muodot

Syöte voi tulla monesta eri lähteestä:

**✔️ Käyttäjän syötteet (ihminen → ohjelma)**

Esimerkkejä:

* tekstikenttään kirjoitettu syöte
* numeron antaminen
* radionappien tai valintalistojen valinta
* hiirellä painettu nappi

---

**✔️ Tiedostot (tiedosto → ohjelma)**

Esim:

* CSV- tai JSON-tiedoston luku
* kuva- tai videotiedoston käsittely
* lokitiedoston analysointi

---

**✔️ Verkkopyynnöt (selain → palvelin)**

Esim:

* HTTP POST -lomake data web-palveluun
* API-kutsu (esim. JSON-data)

---

**✔️ Sensorit ja laitteet (fyysinen maailma → ohjelma)**

Esim:

* lämpötila-anturit
* IoT-laitteet
* näppäimistö / kosketusnäyttö

---

**✔️ Ympäristömuuttujat**

Esim. palvelimen ympäristömuuttujat:

```bash
DATABASE_URL=postgres://...
```

Ohjelma **lukee inputin**, käsittelee sen ja tuottaa **ulostulon (output)**.

---

## ✍️ Inputit eri käyttöliittymissä

Käyttöliittymä määrittää **miten**, **milloin** ja **missä muodossa** input saadaan.

---

**🖥️ Komentorivisovellus (CLI), esim. meidän Python-skriptit**

* Input kirjoitetaan näppäimistöltä.
* Käytetään `input()`-funktiota.
* Sopii oppimiseen: yksinkertainen, suora, keskittyy logiikkaan.
* Syötteen validointi ja kontrolli ovat ohjelmoijan vastuulla.

**Esim. Python CLI-syötteen käsittely:**

```py
nimi = input("Anna nimesi: ")
print("Hei", nimi)
```

---

**🌐 Graafinen käyttöliittymä (GUI)**

* Input tulee tekstikentistä, napeista, valikoista.
* Teknologioita: Tkinter, PyQt, React, Flutter, Electron…
* Koodi reagoi tapahtumiin: “painoin nappia”, “teksti muuttui”.

---

**🌍 Web-käyttöliittymä**

* Inputit ovat HTML-elementtejä:

  ```html
  <input type="text" name="email">
  <input type="number" name="age">
  <button type="submit">Send</button>
  ```
* Data lähetetään palvelimelle:

  * **GET**-parametreina
  * **POST**-lomakkeen datana
  * JSON:ina API-kutsussa

---

**🤖 Taustajärjestelmän inputit**

* API-kutsut
* Cron-tehtävät
* Tietokantakyselyt
* Webhookit

---

## ✅ Miten input käsitellään web-sivulla?

Katsotaan lyhyt käytännön polku.

**1️⃣ HTML-syöte**

```html
<form action="/submit" method="POST">
    <input type="text" name="username" placeholder="Your name">
    <input type="number" name="age">
    <button type="submit">Send</button>
</form>
```

---

**2️⃣ Selain lähettää datan palvelimelle**

Esimerkiksi POST-muodossa:

```
username=Ville&age=38
```

---

**3️⃣ Palvelin käsittelee datan (esim. Python/Flask)**

```py
from flask import request

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["username"]
    age = int(request.form["age"])
    return f"Hello {name}, you are {age} years old."
```

---

**🔧 Mitä tapahtui?**

1. Käyttäjä kirjoitti tiedot lomakkeeseen.
2. Selain pakkasi ne `application/x-www-form-urlencoded` -muotoon.
3. Palvelin purki datan.
4. Koodi validoi ja käytti syötettä.

---

## ✨ Miten tämä eroaa Python-skripteistämme?

**🧪 Python-skripti → inputit käsitellään samassa ohjelmassa**

* Syöte annetaan komentorivillä.
* Ei ole erillistä selainkerrosta.
* Validaatio ja virheenkäsittely tehdään suoraan koodissa.
* Input-ketjut ja flow ovat täysin ohjelmoijan kontrolloitavissa.

**Esimerkiksi skriptissä:**

```py
name = input("Your name: ")
age = int(input("Your age: "))
print(name, age)
```

---

**🌍 Webissä → syöte kulkee kerrosten läpi**

| Kerros          | Tehtävä                     |
| --------------- | --------------------------- |
| HTML            | Syöttökentät                |
| Selain          | Lähettää datan palvelimelle |
| HTTP-protokolla | Kuljettaa datan             |
| Backend-koodi   | Ottaa vastaan ja validoi    |
| Tietokanta      | Tallentaa tiedot            |

**🔍 Web-syötteellä on enemmän uhkia:**

* SQL-injektiot
* XSS
* CSRF
* Väärennetyt lomakkeet
* Roskaposti-injektiot

**Siksi webissä tarvitaan:**

* backend-validointi
* frontend-validointi
* tietoturvatoimet

---

**☝️Python-komentorivissä suurin ongelma on:**

* väärä tietotyyppi (esim. käyttäjä kirjoittaa “kissa” kun odotetaan numeroa)

---

## 🗂️ Inputien rooli ohjelmoinnin ajattelussa

Inputit liittyvät laajemmin ohjelmointiprosessiin:

**🎯 Input → prosessointi → output**

Ohjelmoinnin peruskaava:

```
Syöte → Logiikka → Tulos
```

---

**🎛️ Syöte ohjaa ohjelman kulkua**

* ehtoihin perustuvat valinnat
* funktiot, jotka saavat argumentteja
* toistorakenteet, jotka riippuvat käyttäjän syötteestä

---

**🔁 Input mahdollistaa ohjelman “interaktiivisuuden”**

Ilman inputteja ohjelma on vain passiivinen kone.

---

## 🛕 Kytkentä opintojaksoon

Tällä opintojaksolla

* Aloitamme **komentorivi-inputeilla**, koska:

  * ne ovat yksinkertaisia
  * ne paljastavat ohjelmoinnin perusrakenteet
  * ne vahvistavat ajattelutaitoja: ehto, silmukka, virheenkäsittely, validointi
* Myöhemmin opinnnoissa:

  * web-lomakkeet
  * API-endpointien inputit
  * tietokantoihin syötettävät arvot

**Kun osaat hallita `input()`-syötteitä:**

* ymmärrät hyvin miten data virtaa ohjelmaan
* siirtyminen esim. web-ohjelmointiin on helpompaa
* validointi ja tietotyyppiajattelu ovat jo tuttuja

---

## 💡 Esimerkki: sama idea Python-skriptissä ja webissä

**🐍 Python (CLI)**

```py
nimi = input("Anna nimesi: ")
print("Hei", nimi)
```

---

**🌐 Web (HTML + backend)**

```html
<form action="/hello" method="POST">
    <input type="text" name="nimi">
    <button>Send</button>
</form>
```

**Backend:**

```py
nimi = request.form["nimi"]
return f"Hei {nimi}"
```

---

🟩 Ajatus on sama → Vain **käyttöliittymä ja datan kulkureitti muuttuvat**.

---


# 🧲 Pythonin `input`-syötteiden käyttö

## 💻 Mitä `input()` tekee?

```py
nimi = input("Anna nimesi: ")
print("Hei", nimi)
```

* `input("...")` **näyttää tekstin** käyttäjälle.
* Ohjelma **jää odottamaan syötettä**.
* Käyttäjän kirjoittama rivi **palautuu aina merkkijonona (`str`)**.

> Tärkeää: `input()` ei koskaan palauta suoraan `int`- tai `float`-tyyppiä – muunnos pitää tehdä itse.

---

## 🔎 Syötteen muuttaminen eri tietotyypeiksi

**Kokonaisluku (`int`)**

```py
ikä_str = input("Anna ikäsi (vuosia): ")
ikä = int(ikä_str)  # tyyppimuunnos str -> int
print("Ensi vuonna olet", ikä + 1)
```

👉 Jos käyttäjä kirjoittaa jotain, mitä ei voi muuttaa kokonaisluvuksi (esim. "kissa"), ohjelma kaatuu `ValueError`-virheeseen. Siksi tarvitsemme validointia (katso alla).

---

**Liuku(Desimaali)luku (`float`)**

```py
pituus_str = input("Anna pituutesi metreinä (esim. 1.75): ")
pituus = float(pituus_str.replace(",", "."))  # muutetaan pilkku pisteeksi
print("Pituus metreinä:", pituus)
```

* Suomalaiset kirjoittavat usein **desimaalipilkun** – sen voi korjata `replace(",", ".")`-muunnoksella.

---

**Totuusarvo (`bool`)**

Usein kätevämpää on tulkita kyllä/ei-syöte itse:

```py
vastaus = input("Haluatko jatkaa? (k/e): ").strip().lower()

if vastaus == "k":
    jatka = True
elif vastaus == "e":
    jatka = False
else:
    print("Tuntematon vastaus, oletetaan ettei jatketa.")
    jatka = False
```

---

**Tietotyypin merkitys käytännössä**

* `str` – nimet, osoitteet, viestit
* `int` – lukumäärät, määrät, iät, pisteet
* `float` – hinnat, mitat, lämpötilat
* `bool` – kyllä/ei-valinnat, tilat (on/off)

---

## ✅❌ Syötteen validointi → Perusperiaatteet 

Peruskysymys: **"Onko syöte kelvollinen?"**

Tyypilliset validoinnin askeleet:

1. Onko syöte **tyhjä**?
2. Onko syötteen tyyppi oikea (kokonaisluku, liukuluku…)?
3. Onko arvo **sallitussa välillä** (esim. 0–120)?
4. Onko syöte jokin **sallituista vaihtoehdoista** (esim. "k", "e")?

---

**1️⃣ Esimerkki: ikä välillä 0–120**

```py
ikä_str = input("Anna ikäsi (0–120): ")

if not ikä_str.isdigit():
    print("Virhe: ikä pitää olla kokonaisluku.")
else:
    ikä = int(ikä_str)
    if 0 <= ikä <= 120:
        print("Kiitos, ikäsi on", ikä)
    else:
        print("Virhe: ikä pitää olla välillä 0–120.")
```

---

**2️⃣ Toistuva kysyminen, kunnes syöte on kelvollinen**

Usein halutaan **kysyä uudestaan**, kunnes käyttäjä antaa oikean syötteen.

```py
while True:
    ikä_str = input("Anna ikäsi (0–120): ")

    if not ikä_str.isdigit():
        print("Virhe: anna kokonaisluku.")
        continue  # palaa while-silmukan alkuun

    ikä = int(ikä_str)

    if 0 <= ikä <= 120:
        print("Kiitos, ikäsi on", ikä)
        break  # poistutaan silmukasta
    else:
        print("Virhe: ikä pitää olla välillä 0–120.")
```

---

**3️⃣ `try` / `except` – virheiden käsittely syötteessä**

`isdigit()` ei toimi kaikenlaisille luvuillle (esim. -5, 3.14). Silloin `try/except` on hyvä työkalu.

```py
while True:
    syote = input("Anna kokonaisluku: ")

    try:
        luku = int(syote)
        print("Annoit luvun:", luku)
        break
    except ValueError:
        print("Virhe: tämä ei ollut kokonaisluku. Yritä uudestaan.")
```

**Sama liukuluvuille:**

```py
while True:
    syote = input("Anna lämpötila (°C): ")

    try:
        lampotila = float(syote.replace(",", "."))
        print("Lämpötila on", lampotila, "°C")
        break
    except ValueError:
        print("Virhe: anna numero, esim. 21.5")
```

---

## 🔗 Input-ketjut → Useita syötteitä peräkkäin 

**Input-ketju** = ohjelma kysyy useita asioita peräkkäin, ja myöhemmät kysymykset voivat riippua aiemmista vastauksista.

**Esimerkki: yksinkertainen varauskysely**

```py
print("Tervetuloa varausjärjestelmään!")

nimi = input("Anna nimesi: ").strip()
paiva = input("Anna varauspäivä (pp.kk.vvvv): ").strip()
kesto_str = input("Varauksen kesto tunteina: ").strip()

try:
    kesto = int(kesto_str)
except ValueError:
    print("Virhe: keston pitää olla kokonaisluku. Käytetään oletusta 1 h.")
    kesto = 1

print("\nYhteenveto:")
print(f"Nimi: {nimi}")
print(f"Päivä: {paiva}")
print(f"Kesto: {kesto} h")
```

**Lisämausteita input-ketjuihin:**

* Siivoa syöte: `.strip()`, `.lower()`, `.upper()`
* Tarkista valinnat listasta:

```py
tyypit = ["auto", "vene", "mökki"]
tyyppi = input("Mitä haluat varata (auto/vene/mökki)? ").strip().lower()

if tyyppi not in tyypit:
    print("Tuntematon tyyppi, käytetään oletuksena 'auto'.")
    tyyppi = "auto"
```

---

## 🔁 Ohjelman lopettaminen ja uudelleen aloitus inputien avulla 

Yleinen malli: ohjelmassa on **pääsilmukka**, joka toistuu, kunnes käyttäjä haluaa lopettaa.

**➡️ Yksinkertainen "jatketaanko?"-rakenne**

```py
while True:
    luku_str = input("Anna luku, lasken sen kaksinkertaisena: ")
    try:
        luku = float(luku_str.replace(",", "."))
        print("Kaksinkertainen arvo:", luku * 2)
    except ValueError:
        print("Virhe: tämä ei ollut luku.")
    
    jatko = input("Haluatko laskea toisen luvun? (k/e): ").strip().lower()
    if jatko != "k":
        print("Ohjelma päättyy. Hei hei!")
        break
```

* `while True:` pyörii loputtomasti, kunnes `break`-komento suoritetaan.
* Käyttäjä **päättää**, milloin ohjelma loppuu.

---

**👉🏻 Pieni valikkopohjainen ohjelma**

Tässä käyttäjä voi valita toiminnon tai lopettaa ohjelman kokonaan:

```py
def laske_summa():
    a = float(input("Anna ensimmäinen luku: ").replace(",", "."))
    b = float(input("Anna toinen luku: ").replace(",", "."))
    print("Summa on:", a + b)

def laske_keskiarvo():
    maara_str = input("Kuinka monta lukua? ")
    try:
        maara = int(maara_str)
    except ValueError:
        print("Virhe: määrä pitää olla kokonaisluku.")
        return

    luvut = []
    for i in range(maara):
        luku = float(input(f"Anna luku {i+1}: ").replace(",", "."))
        luvut.append(luku)

    ka = sum(luvut) / len(luvut)
    print("Keskiarvo on:", ka)

while True:
    print("\nVALIKKO")
    print("1) Laske kahden luvun summa")
    print("2) Laske usean luvun keskiarvo")
    print("3) Lopeta ohjelma")

    valinta = input("Valitse (1-3): ").strip()

    if valinta == "1":
        laske_summa()
    elif valinta == "2":
        laske_keskiarvo()
    elif valinta == "3":
        print("Kiitos käytöstä, ohjelma päättyy.")
        break  # ohjelma loppuu
    else:
        print("Tuntematon valinta, yritä uudelleen.")
```

**Tässä:**

* **Ohjelman uudelleen aloitus** = paluu valikkoon.
* **Ohjelman lopetus** = valinta "3" ja `break`.

> ☝️ Voisi myös käyttää `sys.exit()`, mutta `break` ja silmukat ovat usein alussa selkeämpiä.

---

## 🎯 Yhteenveto

* `input()` **palauttaa aina merkkijonon** → tee tarvittavat tyyppimuunnokset (`int`, `float`, `bool`).
* **Validointi** on tärkeää: älä luota sokeasti käyttäjään.

  * Tarkista, onko syöte oikeaa muotoa.
  * Tarvittaessa käytä `while` + `try/except`.
* **Input-ketjut** muodostavat pieniä "lomakkeita" komentoriville – monta syötettä peräkkäin.
* Ohjelman voi **lopettaa** ja **aloittaa toiminnon uudelleen** käyttämällä:

  * pääsilmukkaa (`while True`)
  * valikoita (1, 2, 3, …)
  * `break`-komentoa, kun käyttäjä valitsee lopetuksen.

---