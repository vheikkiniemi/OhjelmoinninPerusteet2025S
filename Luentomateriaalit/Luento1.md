> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla.

# 🕰️ **Ohjelmoinnin lähestymisen malleja**

---

## 💡 1. **IPO-malli (Input–Process–Output)**

**Ohjelma sisältää toimintoja, joilla käsitellään inputteja (syötteitä) ja tuotetaan outputteja (tulosteita)**

* **Idea:** Kaikki ohjelmat voidaan hahmottaa kolmena perusvaiheena:

  1. **Input** – tietojen vastaanottaminen (esim. käyttäjältä, tiedostosta, verkosta).
  2. **Process** – tietojen käsittely (laskenta, logiikka, vertailu).
  3. **Output** – tulosten esittäminen (näyttö, tiedosto, verkko).
* **Hyöty opetuksessa:** Selkeyttää aloittelijoille, mitä ohjelma “tekee”.
* **Esimerkki:**

  ```python
  name = input("Anna nimesi: ")   # Input
  message = f"Hei, {name}!"       # Process
  print(message)                   # Output
  ```

---

## 🧠 2. **Computational Thinking (Laskennallinen ajattelu)**

**Ohjelma on keino muuttaa syöte tulokseksi loogisen käsittelyn kautta.**

* Avainvaiheet: **dekompositio, abstraktio, algoritmointi ja arviointi.**
* Input ja output nähdään osana *abstraktioiden* määrittelyä: mikä tieto tulee sisään, mitä sille tehdään ja mitä sen jälkeen syntyy.
* **Lähde:** Jeannette Wing (2006) – “Computational Thinking”.

---

## 🧩 3. **Functional decomposition (toiminnallinen pilkkominen)**

**ohjelma käsittelee inputin ja tuottaa outputin, se koostuu *toiminnoista* (funktioista), joista kukin toteuttaa osan prosessia.**

* Esim.:

  ```python
  def get_input():
      return input("Anna luku: ")

  def process(n):
      return int(n)**2

  def output(result):
      print("Tulos:", result)

  output(process(get_input()))
  ```
* Tämä on sillanrakentaja *olio-ohjelmointiin* ja *modulaariseen suunnitteluun*.

---

## 🧮 4. **Structured Programming (rakenteinen ohjelmointi)**

**Perustuu selkeään syötteen ja tulosteen hallintaan ilman "goto"-tyyppistä sekavuutta.**

* Ohjelma on **deterministinen**: sama input → sama output.
* Klassisesti ensin *sekvenssi, valinta ja toisto*, jotka liittyvät “process”-vaiheeseen IPO:ssa.

---

## 🌐 5. **Data Flow -ajattelu**

* Näkee ohjelman *tietovirtojen* käsittelijänä: data kulkee sisään, muuttuu vaiheittain ja virtaa ulos.
* Tämä laajentaa IPO-mallin monivaiheiseksi ketjuksi.

  * Input → Transform 1 → Transform 2 → Output

---

## 📚 **Mahdollisia lähteitä**

* Wing, J. (2006). *Computational Thinking.* Communications of the ACM.
* Lister, R., & Leaney, J. (2003). *Introductory Programming, Cognitive Load and the IPO Model.*
* Wirth, N. (1971). *Program Development by Stepwise Refinement.* Communications of the ACM.
* Dale, N., & Lewis, J. (1997). *Computer Science Illuminated.* (IPO mallin käyttö opetuksessa)

---

# 🎓 **Ohjelmointi inputin, prosessin ja outputin kokonaisuutena**

## ♿ **Johdanto: miksi tämä näkökulma?**

Ohjelmointi voidaan ymmärtää monella tavalla: se voi olla ongelmanratkaisua, järjestelmien suunnittelua, tai pelkistetysti koneen ohjaamista. Aloittelevan ohjelmoijan kannalta yksinkertaisin ja samalla tehokkain lähtökohta on kuitenkin ajatella ohjelmaa **prosessina, joka ottaa vastaan syötteen (input), käsittelee sen (process) ja tuottaa tuloksen (output)**.

Tämä **Input–Process–Output (IPO)** -lähestymistapa auttaa ymmärtämään, että jokaisella ohjelmalla on tarkoitus ja rakenne, joka voidaan selittää loogisesti ilman monimutkaisia käsitteitä tai syntaksia.

---

## 💡 **Pedagoginen perusta**

**a) Rakenteinen ajattelu (Structured Thinking)**
IPO tarjoaa tavan jäsentää ajattelua ennen koodin kirjoittamista. Opitaan hahmottamaan, *mitä ohjelma tekee* ennen kuin miettii, *miten se tekee sen*. Tämä tukee **rakenteisen ohjelmoinnin** ja **stepwise refinementin** periaatteita (Wirth, 1971).

**b) Kognitiivisen kuormituksen hallinta (Cognitive Load Theory)**
Lister & Leaney (2003) osoittivat, että IPO-mallin käyttäminen vähentää kognitiivista kuormitusta ohjelmoinnin alkeissa. Kun ymmäretään kolmen vaiheen logiikan, syntaksin ja ohjelmointikielen yksityiskohdat eivät enää tunnu niin kuormittavilta.

**c) Abstraktion opettaminen**
IPO tarjoaa ensimmäisen kosketuksen **abstraktioon**: oppitaan erottamaan tietojen syötön, käsittelyn ja tulostuksen eri tasoiksi. Tämä ajattelutapa on keskeinen **laskennallisessa ajattelussa (Computational Thinking)** (Wing, 2006).

---

## 🧾 **Käytännöllinen merkitys**

| IPO-vaihe   | Opetuksellinen tavoite                                                                 | Esimerkki Pythonilla            |
| ----------- | -------------------------------------------------------------------------------------- | ------------------------------- |
| **Input**   | Opitaan vastaanottamaan tietoa käyttäjältä tai tiedostosta                    | `name = input("Anna nimesi: ")` |
| **Process** | Opitaan käsittelemään tietoa loogisesti (laskeminen, vertailu, ehtorakenteet) | `message = f"Hei, {name}!"`     |
| **Output**  | Opitaan esittämään tuloksen käyttäjälle tai tallentamaan sen tiedostoon       | `print(message)`                |

Tämä vaiheittainen lähestymistapa sopii erityisesti aloitusvaiheen opintojaksoille, joissa tavoitteena on oppia ohjelmoinnin perusrakenne ennen monimutkaisempia käsitteitä kuten olio-ohjelmointia tai tietorakenteita.

---

## 🧰 **Siirtymä kohti kehittyneempiä käsitteitä**

IPO ei ole pelkästään aloittelijan malli — se toimii **siltana monimutkaisempaan ajatteluun**:

* **Funktiot** → jokainen vaihe voidaan toteuttaa omana toimintona (*modularisointi*).
* **Olio-ohjelmointi** → input, prosessointi ja output voivat olla olion vastuita.
* **Tietovirrat ja API-ajattelu** → modernit ohjelmistotkin perustuvat syötteiden vastaanottamiseen ja muuntamiseen tuloksiksi (esim. REST, sensoridata, käyttäjän vuorovaikutus).

---

## ✅ **Yhteenveto**

> **Ohjelmointi on tiedon kuljettamista ja muokkaamista loogisen prosessin läpi.**
> Input–Process–Output-ajattelu tekee tästä näkyvää, jäsenneltyä ja opetettavaa.

| Hyöty                                    | Kuvaus                                                                                              |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Yksinkertainen malli aloittelijoille** | Kolme loogista vaihetta auttavat ymmärtämään ohjelman rakennetta ennen syntaksia.                   |
| **Tukee ongelmanratkaisua**              | Osataan eritellä tehtävän pienempiin osiin (input → käsittely → output).                    |
| **Selkeyttää ohjelmointiprosessia**      | Edistetään suunnittelua ennen toteutusta ja vähentää kokeiluluonteista “koodailua ilman suunnitelmaa”. |
| **Yhdistettävissä muihin paradigmoihin** | Toimii perustana funktioihin, olioihin ja jopa tietovirta-arkkitehtuureihin.                        |

---

# 🧠 **Ohjelmoinnin ja ohjelman keskeiset käsitteet**

## 1. 🧩 **Ohjelma**

Ohjelma on **sarja käskyjä**, jotka tietokone suorittaa tietyssä järjestyksessä halutun tuloksen saavuttamiseksi.

* Ohjelma on kuin **resepti**: se kertoo koneelle, mitä vaiheita pitää suorittaa ja missä järjestyksessä.
* Käskyt voivat sisältää laskutoimituksia, ehtoja, toistoja ja tiedon käsittelyä.

📘 *Esimerkki:*

```python
print("Hello, world!")
```

Tämä ohjelma antaa koneelle yhden käskyn: tulosta teksti ruudulle.

---

## 2. 💬 **Ohjelmointikieli**

Ohjelmointikieli on **ihmisen ja tietokoneen välinen kieli**.

* Se sisältää **säännöt (syntaksi)** ja **merkityksen (semantiikka)**.
* Ohjelmointikielen avulla ohjelmoija kertoo koneelle, mitä sen tulee tehdä.

Kielet voidaan jakaa karkeasti kahteen tasoon:

* **Korkean tason kielet** (esim. Python, JavaScript, C#) – helppo lukea ja ymmärtää.
* **Matalan tason kielet** (esim. Assembly, konekieli) – lähempänä suoraan prosessorin käskyjä.

📘 *Esimerkki:*
Python: `print("Hello")`
Assembly:

```
mov edx, len
mov ecx, msg
mov ebx, 1
mov eax, 4
int 0x80
```

---

## 3. 🔢 **Tietotyypit (Data Types)**

Tietokone käsittelee tietoa eri muodoissa.
Yleisimmät tietotyypit ovat:

* **int** – kokonaisluku (`10`)
* **float** – desimaaliluku (`3.14`)
* **str** – merkkijono (`"Hei"`)
* **bool** – totuusarvo (`True` / `False`)

Tietotyyppien ymmärtäminen on keskeistä, koska ohjelman logiikka ja virheettömyys riippuvat niistä.

📘 *Esimerkki:*

```python
age = 20
name = "Ville"
is_student = True
```

---

## 4. 🔁 **Ohjausrakenteet (Control Structures)**

Ohjausrakenteet määräävät, **mitä ohjelma tekee seuraavaksi**:

1. **Sekvenssi** – käskyt suoritetaan järjestyksessä
2. **Ehto (if)** – päätetään, suoritetaanko jokin osuus vai ei
3. **Toisto (loop)** – suoritetaan käskyjä useita kertoja

📘 *Esimerkki:*

```python
for i in range(3):        # Toisto
    if i == 1:            # Ehto
        print("Keskellä!")
    else:
        print(i)
```

---

## 5. ⚙️ **Muuttuja (Variable)**

Muuttuja on **nimetty paikka tietokoneen muistissa**, johon tallennetaan arvo.

* Muuttujan arvoa voidaan muuttaa ohjelman aikana.
* Muuttujat tekevät ohjelmasta dynaamisen: ohjelma ei ole pelkkä sarja tulosteita, vaan se reagoi dataan.

📘 *Esimerkki:*

```python
x = 5
y = x + 3
print(y)  # tulostaa 8
```

---

## 6. 🧮 **Funktio (Function)**

Funktio on **uudelleenkäytettävä koodilohko**, joka suorittaa tietyn tehtävän.

* Funktiot auttavat pilkkomaan ohjelman pienempiin, ymmärrettäviin osiin.
* Ne voivat ottaa **parametreja (input)** ja palauttaa **paluuarvon (output)**.

📘 *Esimerkki:*

```python
def square(n):
    return n * n

print(square(4))  # tulostaa 16
```

---

## 7. 🧩 **Parametri (Parameter)**

Parametri on **muuttuja, joka määritellään funktion tai metodin otsikossa** ja joka toimii **paikkamerkkinä** tulevalle arvolle.

* Se kertoo, *millaista tietoa funktio tarvitsee toimiakseen*.
* Parametri on siis **funktion sisäinen nimi arvolle**, joka annetaan myöhemmin.

📘 *Esimerkki:*

```python
def greet(name):
    print("Hei", name)
```

➡️ Tässä `name` on **parametri** — se kertoo, että `greet` tarvitsee yhden tiedon (nimen).

---

## 8. 📨 **Argumentti (Argument)**

Argumentti on **arvo**, joka **välitetään funktiolle**, kun sitä kutsutaan.

* Se on se **todellinen tieto**, joka korvaa funktion parametrin.
* Argumentti voidaan antaa suoraan, muuttujasta tai laskutoimituksen tuloksena.

📘 *Esimerkki jatkuu:*

```python
greet("Ville")
```

➡️ Tässä `"Ville"` on **argumentti** — se on konkreettinen arvo, joka välitetään parametrille `name`.

---

## 9. 🧱 **Algoritmi**

Algoritmi on **tarkka kuvaus** siitä, miten jokin ongelma ratkaistaan askel askeleelta.

* Algoritmi on ohjelman **logiikan ydin** – ohjelma on algoritmin toteutus tietokoneella.
* Esimerkiksi lajittelu, hakeminen ja laskeminen ovat tyypillisiä algoritmiongelmia.

📘 *Esimerkki (yksinkertainen):*

1. Ota kaksi lukua
2. Laske niiden summa
3. Tulosta tulos

---

## 10. 🧠 **Virhe ja virheenkäsittely (Error & Exception Handling)**

Virheitä tapahtuu aina – ohjelmoija ei voi niitä täysin välttää.
Virheitä on kahdenlaisia:

* **Syntaksivirheet** – koodi ei noudata kielen sääntöjä.
* **Ajonaikaiset virheet** – koodi on muodollisesti oikein, mutta epäonnistuu suorittaessaan.

📘 *Esimerkki:*

```python
try:
    num = int(input("Anna luku: "))
    print(10 / num)
except ZeroDivisionError:
    print("Nollalla ei voi jakaa!")
```

---

## 11. 🧩 **Moduuli ja kirjasto**

Moduuli on **valmiiksi kirjoitettu koodikokonaisuus**, jota voidaan käyttää ohjelmassa.

* Koodin uudelleenkäyttö säästää aikaa ja vähentää virheitä.
* Pythonin oma kirjasto sisältää satoja valmiita moduuleja (esim. `math`, `datetime`, `random`).

📘 *Esimerkki:*

```python
import math
print(math.sqrt(16))  # tulostaa 4.0
```

---

## 12. 🧭 **Ohjelman suoritus (Program Execution)**

Kun ohjelma ajetaan, tapahtuu seuraavat vaiheet:

1. Lähdekoodi luetaan ja tulkitaan (tai käännetään konekielelle).
2. Käskyt suoritetaan vaiheittain.
3. Muistiin tallennetaan muuttujat ja välitulokset.
4. Ohjelma tuottaa tuloksen (output) ja päättyy.

Tämä on käytännön ilmentymä IPO-mallista — **syöte → käsittely → tulos**.

---

## 📚 **Yhteenveto**

| Käsite           | Selitys                                       | Yhteys IPO-malliin |
| ---------------- | --------------------------------------------- | ------------------ |
| Ohjelma          | Käskyjen sarja, joka ratkaisee ongelman       | Koko prosessi      |
| Ohjelmointikieli | Viestintäväline ohjelmoijan ja koneen välillä | Koko prosessi      |
| Muuttuja         | Tiedon säilytyspaikka                         | Input & Process    |
| Ohjausrakenne    | Päätösten ja toistojen hallinta               | Process            |
| Funktio          | Toiminnallinen osakokonaisuus                 | Process & Output   |
| Parametri        | Nimeää tiedon, jota funktio tarvitsee         | Process            |
| Argumentti       | Antaa arvon funktiolle                        | Process            |
| Algoritmi        | Looginen toimintamalli ongelman ratkaisuun    | Process            |
| Tietotyyppi      | Kuvaa datan luonteen                          | Input & Process    |
| Moduuli          | Uudelleenkäytettävä koodikokonaisuus          | Process            |
| Output           | Tuloksen esittäminen käyttäjälle              | Output             |

---

# 🧱 **Olio-ohjelmoinnin (Object-Oriented Programming, OOP) käsitteitä**

## 1. 🧩 **Olio (Object)**

Olio on ohjelman **perusyksikkö**, joka mallintaa jotakin todellisen tai käsitteellisen maailman asiaa.

* Olio **sisältää tietoa (ominaisuuksia)** ja **toimintoja (metodeja)**.
* Se on kuin “miniohjelma” ohjelman sisällä: se tietää jotain ja osaa tehdä jotain.

📘 *Esimerkki:*

```python
# Olion luonti
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

my_car = Car("Toyota", 120)
```

Tässä `my_car` on olio, jolla on **ominaisuudet** (`brand`, `speed`) ja myöhemmin myös **metodeja**.

---

## 2. 🏗️ **Luokka (Class)**

Luokka on **malli tai suunnitelma** olioille.

* Jos olio on “talo”, luokka on “talon piirustus”.
* Luokasta voidaan luoda useita samanlaisia olioita, joilla on eri tiedot.

📘 *Esimerkki:*

```python
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

# Kaksi oliota samasta luokasta
car1 = Car("Tesla", 150)
car2 = Car("Volvo", 130)
```

---

## 3. ⚙️ **Metodi (Method)**

Metodi on **funktion kaltainen toiminto**, joka kuuluu olioon.

* Se määrittelee, **mitä olio osaa tehdä**.
* Jokaisella metodilla on automaattisesti pääsy olion omiin tietoihin (`self`).

📘 *Esimerkki:*

```python
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} nyt {self.speed} km/h")

my_car = Car("Audi", 100)
my_car.accelerate(20)  # kutsutaan metodia
```

➡️ Tässä `accelerate()` on **metodi**, ja `self.speed` on **ominaisuus** (property).

---

## 4. 📦 **Ominaisuus / Attribuutti (Attribute / Property)**

Ominaisuus on **tieto**, joka kuuluu olioon.

* Attribuutit tallennetaan olion sisään.
* Niihin päästään käsiksi `self`-viittauksen kautta luokan sisällä tai suoraan olion kautta.

📘 *Esimerkki:*

```python
print(my_car.brand)  # tulostaa "Audi"
```

---

## 5. 🧬 **Konstruktori (`__init__`-metodi)**

Konstruktori on **erikoismetodi**, joka ajetaan automaattisesti, kun olio luodaan.

* Sen avulla määritellään olion alkuarvot.
* Pythonissa konstruktori on nimeltään `__init__()`.

📘 *Esimerkki:*

```python
class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
```

---

## 6. 🧱 **Kapselointi (Encapsulation)**

Kapselointi tarkoittaa, että **olion sisäinen tila pidetään piilossa** ulkopuolelta ja sitä hallitaan metodien avulla.

* Tämä suojaa tietoja virheelliseltä käytöltä.
* Toteutetaan usein yksityisillä muuttujilla (Pythonissa `_` tai `__` -alkuiset nimet).

📘 *Esimerkki:*

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance  # yksityinen attribuutti

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

---

## 7. 🧬 **Perintä (Inheritance)**

Perintä tarkoittaa, että **uusi luokka voi periä ominaisuuksia ja metodeja toiselta luokalta**.

* Tämä vähentää koodin toistoa ja mahdollistaa luokkien laajentamisen.
* Aliluokka (subclass) voi myös **ylikirjoittaa (override)** vanhan metodin.

📘 *Esimerkki:*

```python
class Vehicle:
    def move(self):
        print("Liikkuu eteenpäin")

class Car(Vehicle):   # Car perii Vehicle-luokan
    def honk(self):
        print("Beep beep!")

my_car = Car()
my_car.move()
my_car.honk()
```

---

## 8. 🔄 **Polymorfismi**

Polymorfismi tarkoittaa, että **eri oliot voivat käyttää samaa metodia eri tavalla**.

* Esimerkiksi sekä `Dog` että `Cat` voivat toteuttaa oman `make_sound()`-metodinsa.

📘 *Esimerkki:*

```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

for a in [Dog(), Cat()]:
    a.make_sound()
```

---

## 9. 🧠 **Abstraktio (Abstraction)**

Abstraktio tarkoittaa, että **monimutkaiset yksityiskohdat piilotetaan**, ja käyttäjälle näytetään vain olennainen.

* Käyttäjä käyttää olion toimintoja (metodeja) tietämättä, miten ne on toteutettu.

📘 *Esimerkki:*
Kun kutsut `car.accelerate(10)`, sinun ei tarvitse tietää, mitä kaikkea auton sisällä tapahtuu — tiedät vain, että se kiihdyttää.

---

## 10. 🔗 **Olioiden välinen vuorovaikutus**

Oliot voivat **kutsua toistensa metodeja** ja **välittää tietoa**.

* Tämä mahdollistaa ohjelmien rakentamisen **yhteistyötä tekevien olioiden verkostoksi**.

📘 *Esimerkki:*

```python
class Engine:
    def start(self):
        print("Moottori käynnistyy")

class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.start()
        print("Auto liikkuu")

my_car = Car()
my_car.drive()
```

---

## 🧭 **OOP:n neljä peruspilaria yhteenvetona**

| Periaate                        | Selitys                                                                        | Esimerkki                                |
| ------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------- |
| **Kapselointi (Encapsulation)** | Tiedot ja toiminnot kootaan yhteen olioon ja suojataan ulkopuoliselta pääsyltä | Pankkitili-luokan `__balance`            |
| **Abstraktio (Abstraction)**    | Monimutkaisuus piilotetaan metodien taakse                                     | `car.accelerate()`                       |
| **Perintä (Inheritance)**       | Luokka perii toisen luokan ominaisuudet                                        | `Car(Vehicle)`                           |
| **Polymorfismi (Polymorphism)** | Sama toiminto toimii eri tavoin eri olioilla                                   | `Dog.make_sound()` ja `Cat.make_sound()` |

---

## 🧩 **Yhteys IPO-malliin**

Olio-ohjelmointi **laajentaa IPO-mallia**:

* Jokainen **olio** voi käsitellä omaa **inputtiaan**, suorittaa oman **processinsa** ja tuottaa oman **outputtinsa**.
* Tällöin koko ohjelma on **yhteistyössä toimivien IPO-yksiköiden verkosto**.

---

## 📚 **Yhteenveto**

| Käsite                     | Kuvaus                          | Esimerkki Pythonilla    |
| -------------------------- | ------------------------------- | ----------------------- |
| **Luokka (Class)**         | Määrittelee olion mallin        | `class Car:`            |
| **Olio (Object)**          | Luokan yksittäinen esiintymä    | `my_car = Car()`        |
| **Ominaisuus (Attribute)** | Olion sisältämä tieto           | `self.speed`            |
| **Metodi (Method)**        | Olion toiminto                  | `def accelerate(self):` |
| **Konstruktori**           | Luo ja alustaa olion            | `def __init__(...)`     |
| **Kapselointi**            | Suojaa olion tietoja            | `self.__balance`        |
| **Perintä**                | Luokka laajentaa toista luokkaa | `class Car(Vehicle)`    |
| **Polymorfismi**           | Sama toiminto eri toteutuksilla | `make_sound()`          |
| **Abstraktio**             | Näyttää vain olennaisen         | `car.drive()`           |

---

# 🧠 Ohjelmointikielten kategorioita ja lähestymistapoja

Ohjelmointikieliä voidaan jaotella monin eri perustein. Yleisimpiä ovat:

1. **Ohjelmointiparadigman mukaan**
2. **Käännöksen ja tulkinnan mukaan**
3. **Abstraktiotason mukaan**
4. **Käyttötarkoituksen mukaan**

---

## 🧩 1. **Ohjelmointiparadigman mukaan**

**Paradigma** tarkoittaa sitä, *millä tavalla ohjelma jäsennetään ja miten ohjelmoija ajattelee ongelmaa*.
Se on kuin “ajattelutapa” ohjelmoinnissa.

| Paradigma                             | Kuvaus                                                                      | Tyypillisiä kieliä                    | Esimerkki                              |
| ------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------- | -------------------------------------- |
| **Imperatiivinen**                    | Ohjelmoija käskee askel askeleelta, mitä koneen tulee tehdä.                | C, Python, JavaScript (osittain)      | `x = x + 1`                            |
| **Deklaratiivinen**                   | Ohjelmoija kertoo *mitä* haluaa, ei *miten*. Kone päättää toteutuksen.      | SQL, HTML, Prolog                     | `SELECT * FROM Students;`              |
| **Olio-ohjelmointi (OOP)**            | Maailma mallinnetaan olioina, joilla on ominaisuuksia ja toimintoja.        | Java, Python, C++, C#, Swift          | `car.accelerate()`                     |
| **Funktionaalinen**                   | Ohjelmat rakentuvat funktioista ilman sivuvaikutuksia.                      | Haskell, Lisp, F#, Scala, myös Python | `map(lambda x: x*2, lista)`            |
| **Proseduraalinen**                   | Ohjelma jaetaan aliohjelmiin ja toistuviin osiin (varhainen muoto OOP:sta). | C, Pascal, BASIC                      | `void printSum(int a, int b)`          |
| **Looginen**                          | Ohjelmoija määrittelee säännöt ja suhteet, kone päättää ratkaisut.          | Prolog                                | `father(X,Y) :- parent(X,Y), male(X).` |
| **Tapahtumapohjainen (Event-driven)** | Koodi reagoi käyttäjän tai järjestelmän tapahtumiin.                        | JavaScript, C#, Swift                 | `button.onclick = handler`             |

💡 **Opetuksellinen huomio:**
Paradigmat eivät ole toisiaan poissulkevia. Esimerkiksi **Python ja JavaScript** ovat *moniparadigmaisia* — niillä voi ohjelmoida sekä olio- että funktionaalisella tavalla.

---

## ⚙️ 2. **Käännöksen ja tulkinnan mukaan**

| Tyyppi                       | Kuvaus                                                                                     | Esimerkkejä             | Opetuksellinen näkökulma                 |
| ---------------------------- | ------------------------------------------------------------------------------------------ | ----------------------- | ---------------------------------------- |
| **Käännettävä (compiled)**   | Koodi muunnetaan ensin konekieleksi (binaariksi), jota kone suorittaa. Nopeampi suoritus.  | C, C++, Rust, Go        | Koodista tulee *exe* tai *bin* tiedosto. |
| **Tulkattava (interpreted)** | Koodi suoritetaan riviltä riville tulkin (interpreter) avulla. Hitaampi mutta joustavampi. | Python, JavaScript, PHP | Helppo testata ja muuttaa lennossa.      |
| **Hybridikieli**             | Käännetään ensin välikielelle (bytecode), jota virtuaalikone suorittaa.                    | Java (JVM), C# (.NET)   | Yhdistää siirrettävyyden ja tehokkuuden. |

💡 Esimerkki:

* Python käyttää tulkkia: `python ohjelma.py`
* C käännetään: `gcc ohjelma.c -o ohjelma`

---

## 🧮 3. **Abstraktiotason mukaan**

| Taso                              | Kuvaus                                                           | Esimerkkejä            | Yhteys opetukseen                         |
| --------------------------------- | ---------------------------------------------------------------- | ---------------------- | ----------------------------------------- |
| **Matalan tason kielet**          | Lähellä konekieltä ja prosessorin rakennetta.                    | Assembly, C            | Hyvä ymmärtää, miten kone todella toimii. |
| **Korkean tason kielet**          | Luettavia ja ihmisen ajatteluun sopivia.                         | Python, Java, C#, Ruby | Hyvä opetuskäyttöön.                      |
| **Erittäin korkean tason kielet** | Abstraktioita vielä enemmän: lähinnä kuvaillaan *mitä* halutaan. | SQL, MATLAB            | Soveltuu erityistehtäviin.                |

💡 Tulkinta:
Korkean tason kielet piilottavat monimutkaisuutta (esim. muistin hallinnan), jotta opiskelija voi keskittyä ohjelman rakenteeseen ja logiikkaan.

---

## 💼 4. **Käyttötarkoituksen mukaan**

| Käyttöalue                       | Kuvaus                                   | Tyypillisiä kieliä                              |
| -------------------------------- | ---------------------------------------- | ----------------------------------------------- |
| **Yleiskäyttöiset kielet**       | Soveltuvat lähes kaikkeen ohjelmointiin. | Python, Java, C++, C#, JavaScript               |
| **Web-kehitys**                  | Frontend ja backend -kehitykseen.        | HTML, CSS, JavaScript, TypeScript, PHP, Node.js |
| **Tietokannat**                  | Tiedon hakuun ja muokkaukseen.           | SQL, PL/SQL                                     |
| **Tieteellinen ja datalaskenta** | Matemaattiseen ja analyyttiseen työhön.  | Python (NumPy, Pandas), R, Julia, MATLAB        |
| **Sulautetut järjestelmät**      | Laitteiden ja sensoreiden ohjaukseen.    | C, C++, Rust, Assembly                          |
| **Mobiilikehitys**               | Sovellusten kehitykseen puhelimille.     | Swift (iOS), Kotlin (Android), Dart (Flutter)   |
| **Pelikoodaus**                  | Pelimoottoreiden käyttöön.               | C#, C++, Lua, GDScript                          |

💡 Tästä näkökulmasta ohjelmointikielen valinta riippuu tehtävästä, ei mieltymyksestä.

---

## 🧩 5. **Muita luokittelutapoja (lyhyesti)**

| Kriteeri              | Vaihtoehtoja                        | Esimerkkejä                                        |
| --------------------- | ----------------------------------- | -------------------------------------------------- |
| **Tyyppijärjestelmä** | Dynaaminen / staattinen             | Python (dynaaminen), Java (staattinen)             |
| **Oliotuki**          | OOP vs ei-OOP                       | Java (OOP), C (ei)                                 |
| **Syntaksityyli**     | C-tyyli / Python-tyyli / Lisp-tyyli | Java, Python, Lisp                                 |
| **Avoimuus**          | Avoin / suljettu                    | Python (open source), C# (Microsoftin hallinnoima) |

---

## 🔍 6. **Esimerkkivertailu kolmen paradigman kautta**

| Paradigma                     | Kieli                                             | Esimerkkikoodi                   | Ajattelutapa |
| ----------------------------- | ------------------------------------------------- | -------------------------------- | ------------ |
| **Proseduraalinen (C)**       | `int add(int a, int b) { return a + b; }`         | Kutsu aliohjelmia                |              |
| **Olio-ohjelmointi (Python)** | `class Calculator: def add(self,a,b): return a+b` | Mallinna olioita ja toimintoja   |              |
| **Funktionaalinen (Haskell)** | `add a b = a + b`                                 | Kuvaa riippuvuuksia, ei vaiheita |              |

---

## 💬 7. **Oppimisen näkökulma**

Kun ohjelmointia opetellaan, **kielestä ei tule aloittaa — ajattelutavasta kyllä**.
IPO-malli ja ohjelmointiparadigmat tarjoavat loogisen jatkumon:

1. **Aloita IPO-ajattelusta** (input → process → output)
2. **Laajenna rakenteiseen ohjelmointiin** (funktiot, ehdot, toistot)
3. **Siirry olio-ohjelmointiin** (olio = itsenäinen IPO)
4. **Näytä vaihtoehtoiset paradigmat** (funktionaalinen, deklaratiivinen)

---

## 📚 **Yhteenveto**

| Luokittelutapa       | Peruste                            | Esimerkkejä                          | Mitä opitaan                           |
| -------------------- | ---------------------------------- | ------------------------------------ | -------------------------------------- |
| **Paradigma**        | Ajattelutapa ohjelmoinnissa        | OOP, funktionaalinen, imperatiivinen | Miten ohjelma jäsennetään              |
| **Käännösmenetelmä** | Miten koodi suoritetaan            | C (käännettävä), Python (tulkattava) | Miksi koodi toimii eri nopeuksilla     |
| **Abstraktiotaso**   | Kuinka lähellä konekieltä kieli on | Assembly → Python                    | Miten kieli piilottaa monimutkaisuutta |
| **Käyttötarkoitus**  | Missä kieliä käytetään             | Web, data, peli, sulautettu          | Kielen ja kontekstin yhteys            |

---

# 🧭 **Ohjelmointiprosessi – ideasta toimivaksi ohjelmaksi**

Ohjelmointi ei ole vain koodaamista. Se on **ongelmanratkaisuprosessi**, jossa edetään vaiheittain:

> **Ongelma → Suunnitelma → Koodi → Testaus → Viimeistely**

Tämä prosessi toistuu syklisesti — ohjelmat **kehitetään, testataan ja parannetaan** useita kertoja.

---

## 🔍 1. **Ongelman määrittely (Problem Definition)**

**Tavoite:** ymmärtää, *mitä ongelmaa ohjelma ratkaisee*.

### Käsitteitä:

* **Vaatimusmäärittely (Requirements Specification):**
  Kirjallinen tai suullinen kuvaus siitä, mitä ohjelman täytyy pystyä tekemään.
  → *Esim. “Ohjelman tulee laskea opiskelijoiden keskiarvo.”*

* **Input ja Output:**
  Mitä tietoja ohjelma ottaa vastaan (input) ja mitä se tuottaa (output)?
  → *Input:* opiskelijoiden arvosanat, *Output:* keskiarvo.

* **Rajoitteet (Constraints):**
  Esim. suoritusaika, muistinkäyttö, käyttöympäristö.

📘 *Esimerkki:*

> Kirjoitetaan ohjelman, joka lukee viisi lukua ja tulostaa niiden keskiarvon.

---

## 🧩 2. **Suunnittelu (Program Design)**

**Tavoite:** määrittää, *miten ongelma ratkaistaan* — ennen kuin kirjoitetaan koodia.

### Käsitteitä:

* **Algoritmi:**
  Tarkka, askel askeleelta etenevä menetelmä ongelman ratkaisuun.
  → voidaan kuvata *pseudokoodina* tai *vuokaaviona*.

* **Pseudokoodi:**
  Yksinkertaistettu, ihmisen luettava “luonnoskieli” ohjelmasta.

  ```text
  lue viisi lukua
  laske summa
  jaa summa viidellä
  tulosta keskiarvo
  ```

* **Vuokaavio (Flowchart):**
  Graafinen esitys ohjelman kulusta (aloitus, ehtoja, toistoja).

* **Modulointi (Modular Design):**
  Suunnitellaan ohjelma osiin (funktiot, luokat, moduulit).
  → Tämä helpottaa ylläpitoa ja testausta.

💡 Suunnittelu ennen koodausta vähentää virheitä ja tekee ohjelmasta helpommin ymmärrettävän.

---

## 💻 3. **Toteutus (Implementation / Coding)**

**Tavoite:** muuttaa suunnitelma ohjelmointikielelle.

### Käsitteitä:

* **Syntaksi:**
  Ohjelmointikielen kielioppi — miten käskyt kirjoitetaan oikein.
  → *Esim.* Pythonissa lohko määritellään sisennyksellä.

* **Komentorakenne / Ohjausrakenne:**
  Sekvenssi, ehto, toisto — ohjelman ohjauslogiikka.

* **Muuttuja ja tietotyyppi:**
  Ohjelmassa käytettävät tiedot tallennetaan muuttujiin (esim. `int`, `str`).

* **Funktio / Metodi:**
  Koodilohko, joka toteuttaa yhden toiminnon (tukee modulointia).

📘 *Esimerkki:*

```python
def average(numbers):
    return sum(numbers) / len(numbers)

scores = [3, 4, 5, 2, 5]
print("Keskiarvo:", average(scores))
```

---

## 🧪 4. **Testaus ja virheenkorjaus (Testing & Debugging)**

**Tavoite:** varmistaa, että ohjelma toimii oikein kaikissa tilanteissa.

### Käsitteitä:

* **Virhe (Error):**
  Ohjelman toiminnan estävä ongelma. Kolme yleistä tyyppiä:

  1. **Syntaksivirhe:** kielioppivirhe (`print("Hei"` ilman sulkua).
  2. **Ajonaikainen virhe:** ohjelma kaatuu suorituksessa (`division by zero`).
  3. **Looginen virhe:** ohjelma toimii, mutta tuottaa väärän tuloksen.

* **Debuggaus (Debugging):**
  Virheiden etsiminen ja korjaaminen (esim. `print`-tulosteilla tai debuggerilla).

* **Testitapaus (Test Case):**
  Tarkkaan suunniteltu syöte ja odotettu tulos.
  → *Esim.* syötteet `[2, 4, 6]` → odotettu keskiarvo `4.0`.

* **Automaattinen testaus:**
  Esim. `pytest`-kirjaston käyttö varmistamaan, että ohjelman osat toimivat aina samalla tavalla.

📘 *Esimerkki testistä:*

```python
def test_average():
    assert average([2,4,6]) == 4
```

---

## 🧰 5. **Dokumentointi ja ylläpito (Documentation & Maintenance)**

**Tavoite:** varmistaa, että ohjelmaa voidaan käyttää, ymmärtää ja kehittää myöhemmin.

### Käsitteitä:

* **Koodikommentit:**
  Lyhyitä selityksiä koodin sisällä (`# Tämä laskee keskiarvon`).

* **Dokumentaatio:**
  Kuvaa ohjelman tarkoituksen, syötteet, tulosteet ja rakenteen.
  → Auttaa muita kehittäjiä ja tulevia käyttäjiä.

* **Versiohallinta:**
  Työkalu (esim. Git), joka tallentaa muutokset ja mahdollistaa yhteistyön.

* **Ylläpito (Maintenance):**
  Ohjelman päivittäminen ja parantaminen käytön aikana.
  → Korjataan virheitä, lisätään ominaisuuksia, optimoidaan.

---

## 🔁 6. **Iteraatio ja kehittäminen (Iteration / Refinement)**

Ohjelmointiprosessi on **iteratiivinen** – eli toistuva.
Harvoin ohjelma on valmis kerralla.

* Jokainen uusi versio tuo korjauksia ja parannuksia.
* Prosessi muistuttaa **sykliä**, ei lineaarista polkua.

📘 *Vaiheet voivat siis toistua:*

> **Suunnittele → Toteuta → Testaa → Paranna → Suunnittele uudelleen**

💡 Tämä ajattelu pohjustaa **nykyaikaista ohjelmistokehitystä**, kuten:

* **Agile** ja **Scrum** – jatkuva kehitys ja palautesykli.
* **DevOps** – yhdistää kehityksen ja ylläpidon.

---

## 📚 **Koko prosessi tiivistetysti**

> **Ohjelmointi on prosessi, ei pelkkä koodaus.**
> Koodi on vain yksi vaihe — tärkeintä on ajattelu, suunnittelu ja parantaminen.

| Vaihe                            | Kuvaus                                            | Keskeisiä käsitteitä                     | Tulos               |
| -------------------------------- | ------------------------------------------------- | ---------------------------------------- | ------------------- |
| **1. Ongelman määrittely**       | Määritetään mitä halutaan ratkaista               | Vaatimusmäärittely, input/output         | Selkeä tavoite      |
| **2. Suunnittelu**               | Laaditaan ratkaisu ennen koodausta                | Algoritmi, pseudokoodi, vuokaavio        | Toimintasuunnitelma |
| **3. Toteutus**                  | Koodi kirjoitetaan ohjelmointikielellä            | Syntaksi, muuttujat, funktiot            | Toimiva ohjelma     |
| **4. Testaus ja debuggaus**      | Tarkistetaan virheet ja toimivuus                 | Testitapaus, virhe, debuggaus            | Luotettava ohjelma  |
| **5. Dokumentointi ja ylläpito** | Tehdään ohjelma ymmärrettäväksi ja kehitettäväksi | Kommentit, dokumentaatio, versiohallinta | Käytettävä ohjelma  |
| **6. Iteraatio**                 | Toistetaan prosessia kehittämiseksi               | Versiointi, parannukset                  | Parempi ohjelma     |

---

Erinomaista, Ville 💪

Nyt siirrytään **teoriasta käytäntöön** — askel askeleelta kuvaus siitä, **miten ohjelmointiprosessi etenee opiskelijan näkökulmasta**, kun käytössä on **Visual Studio Code (VS Code)**.

Tämä on konkreettinen ja opetuksellisesti etenevä malli: opiskelija saa selkeän käsityksen *mitä tehdään, missä vaiheessa, ja miksi*.

---

# 🧭 **Käytännön ohjelmointiprosessi – vaiheittain (VS Code)**

## 🪜 **Vaihe 1: Kehitysympäristön valinta ja valmistelu**

**Tavoite:** luoda ympäristö, jossa ohjelmointia voi tehdä tehokkaasti ja virheettömästi.

### Käsitteitä:

* **IDE (Integrated Development Environment):**
  Työkalu, joka yhdistää tekstieditorin, virheentarkistuksen, versionhallinnan ja terminaalin yhteen paikkaan.
  👉 *Esimerkki:* **Visual Studio Code (VSC)**.
* **Laajennukset (Extensions):**
  VSC:hen lisättävät työkalut, jotka tukevat eri kieliä (esim. *Python*, *Prettier*, *GitHub Copilot*).
* **Tulkki / kääntäjä:**
  Ohjelma, joka suorittaa tai kääntää koodin (esim. *Python interpreter*, *Node.js*).

📘 *Käytännössä:*

1. Lataa ja asenna [**Visual Studio Code**](https://code.visualstudio.com/)

> [!TIP]
> Tämä yleensä suoraviivainen prosessi

2. Lataa ja asenna [**Python-ympäristö**](https://www.python.org/)

> [!TIP]
> Huomioi asennuksessa (Windows), että vaatii yleensä asentamisen kaikille käyttäjille (valinta asennusprosessissa)

3. Asenna **Python extension** (tai halutun kielen laajennus).
4. Tarkista, että komentorivillä (Visual studio code) toimii:

   ```bash
   python --version
   ```
5. Luo uusi kansio projektia varten (esim. `MyFirstProgram`).

💡 **kehitysympäristö on osa ohjelmointiprosessia** — se tekee työstä hallittavaa ja virheet helpommin löydettäviä.

---

## 🧩 **Vaihe 2: Uuden projektin luonti ja tiedoston valmistelu**

**Tavoite:** aloittaa varsinainen ohjelmointityö järjestelmällisesti.

### Käsitteitä:

* **Projekti:**
  Kokoelma tiedostoja, jotka liittyvät samaan ohjelmaan (koodi, kuvat, data, README jne.).
* **Lähdekooditiedosto (Source file):**
  Tiedosto, jossa varsinainen ohjelma on.
  → Python: `.py`, JavaScript: `.js`, C: `.c`

📘 *Käytännössä:*

1. Luo uusi tiedosto: `main.py`
2. Lisää ensimmäinen ohjelmarivi:

   ```python
   print("Hello, world!")
   ```
3. Tallenna tiedosto (Ctrl + S)
4. Aja ohjelma terminaalissa:

   ```bash
   python main.py
   ```

💬 Tämä on **ensimmäinen konkreettinen output** – koodi tuottaa tulosteen.

---

## 💡 **Vaihe 3: Ohjelman suunnittelu ja rakentaminen**

**Tavoite:** muuttaa idea toimivaksi ohjelmaksi.

### Käsitteitä:

* **Algoritmi:**
  Askelsarja, joka määrittää, miten ongelma ratkaistaan.
* **Komentorakenne:**
  Ohjelman logiikka (sekvenssi, ehto, toisto).
* **Muuttuja ja funktio:**
  Muuttuja säilyttää tietoa, funktio toistaa logiikan osia.

📘 *Käytännössä:*

1. Suunnittelee pseudokoodilla:

   ```text
   1. Kysy käyttäjältä nimi
   2. Luo tervehdysviesti
   3. Tulosta tervehdys
   ```
2. Toteuttaa sen koodina:

   ```python
   name = input("Anna nimesi: ")
   message = f"Hei, {name}!"
   print(message)
   ```
3. Ajaa ohjelman uudelleen ja testaa eri syötteillä.

💬 **sovelletaan IPO-mallia**: Input = nimi, Process = viestin muodostus, Output = tulostus.

---

## 🧪 **Vaihe 4: Testaus ja virheenkorjaus**

**Tavoite:** varmistaa, että ohjelma toimii kaikissa olosuhteissa.

### Käsitteitä:

* **Syntaksivirhe:** kirjoitusvirhe, joka estää ohjelman ajamisen.
* **Ajonaikainen virhe:** ohjelma kaatuu kesken suorituksen.
* **Looginen virhe:** ohjelma toimii, mutta tulos on väärä.
* **Debuggaus:** virheiden etsiminen ja korjaaminen.

📘 *Käytännössä:*

1. Teee virheen tahallaan ja tarkista, mitä VS Code näyttää:

   ```python
   print("Hei"  # <- unohtunut sulku
   ```

   IDE näyttää virheen **suoraan rivillä**.
2. Käytä **VSC:n debuggeria**:

   * Aseta **breakpointin**
   * Suorita ohjelman askelittain
   * Tarkista muuttujien arvot reaaliajassa

💬 Tämä vaihe konkretisoi, että ohjelma ei ole “kirjoita ja toimi heti” vaan *kirjoita–testaa–korjaa–toista*.

---

## 📘 **Vaihe 5: Dokumentointi ja versionhallinta**

**Tavoite:** tehdä koodista ymmärrettävää ja säilyttää sen historia.

### Käsitteitä:

* **Kommentti:**
  Ihmisen luettava selite, joka ei vaikuta ohjelman toimintaan.

  ```python
  # Tämä funktio laskee neliön
  def square(n):
      return n * n
  ```
* **README:**
  Tekstitiedosto, joka kertoo ohjelman tarkoituksen ja käyttöohjeet.
* **Git ja GitHub:**
  Versionhallintajärjestelmä, joka tallentaa muutokset ja mahdollistaa yhteistyön.

📘 *Käytännössä:*

1. Luo `README.md` tiedoston:

   ```
   # MyFirstProgram
   This program greets the user.
   ```
2. Alusta versionhallinnan (komentorivi tai Visual studio code):

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
3. Julkaisee projektin GitHubissa tai Azure Static Web Appsissa.

💬 Ohjelmointi on **yhteistyötä ja jatkuvaa kehittämistä**, ei pelkkää yksittäisen tiedoston kirjoittamista.

---

## 🚀 **Vaihe 6: Parantaminen ja jatkokehitys**

**Tavoite:** muuttaa yksinkertainen ohjelma monipuolisemmaksi.

### Käsitteitä:

* **Versiointi:** ohjelman eri kehitysvaiheiden hallinta (v1.0, v1.1, v2.0).
* **Refaktorointi:** koodin rakenteen parantaminen ilman, että sen toiminta muuttuu.
* **Ominaisuuksien lisääminen:** uudet toiminnot tai käyttöliittymä.

📘 *Käytännössä:*

1. Lisää uusi ominaisuus:

   ```python
   def greet(name, age):
       print(f"Hei {name}, olet {age} vuotta vanha.")

   greet("Ville", 35)
   ```

2. Käytä uudelleen aiemmin opittuja käsitteitä:
   → **Parametrit, argumentit, funktiot ja virheenkäsittely.**

3. Kokeile ohjelman julkaisemista (esim. komentorivillä tai verkkopalvelussa).

💬 Ohjelma kehittyy *projektiksi* ja siirrytään ajattelussa “harjoituksesta kehittäjäksi”.

---

## 🧭 **Yhteenveto: ohjelmointiprosessi käytännössä**

> **Ohjelmointi alkaa ideasta ja päättyy jatkuvaan kehittämiseen.**
> Visual Studio Code on vain työkalu, mutta ohjelmointiprosessi on ajattelun malli:
> **Suunnittele – Toteuta – Testaa – Paranna – Toista.**

| Vaihe                                | Toiminta VS Codessa                         | Keskeiset käsitteet                     | Tuloksena                        |
| ------------------------------------ | ------------------------------------------- | --------------------------------------- | -------------------------------- |
| 1️⃣ Kehitysympäristön valmistelu     | Asennukset, kääntäjän valinta, laajennukset | IDE, tulkki, laajennus                  | Työskentelyvalmis ympäristö      |
| 2️⃣ Projektin luonti                 | Kansion ja tiedoston teko                   | Projekti, lähdekoodi                    | Tyhjä ohjelma                    |
| 3️⃣ Suunnittelu ja toteutus          | Kirjoitetaan koodi ja testataan             | IPO, algoritmi, muuttujat               | Toimiva ohjelma                  |
| 4️⃣ Testaus ja debuggaus             | Ajetaan ohjelma ja korjataan virheitä       | Syntaksi, ajonaikainen virhe, debuggaus | Virheetön ohjelma                |
| 5️⃣ Dokumentointi ja versionhallinta | Kommentit, README, Git                      | Dokumentaatio, commit                   | Jäljitettävä ja jaettava ohjelma |
| 6️⃣ Jatkokehitys                     | Parannukset ja julkaisu                     | Refaktorointi, versiointi               | Kehittyvä ohjelma                |

---