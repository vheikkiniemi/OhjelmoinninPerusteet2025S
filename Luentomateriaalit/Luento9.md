> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla.

# 🗂️ **Dictionary Pythonissa → Avainten ja arvojen tehokas tietorakenne**

## 📘 Mikä on dictionary?

**Dictionary** (suomeksi sanakirja tai hajautustaulu) on Pythonin sisäänrakennettu tietotyyppi, joka tallentaa tietoa **avain–arvo**-pareina.

```python
{
    avain1: arvo1,
    avain2: arvo2,
    ...
}
```

Dictionary on erinomainen valinta, kun haluat:

* hakea tietoa **avainperusteisesti**,
* yhdistää asioita toisiinsa (esim. nimi → puhelinnumero),
* tallentaa rakennetta, jossa jokaisella tietueella on selkeä identiteetti.

---

## 🎯 Miksi dictionary on hyödyllinen?

**✔️ Nopea haku**

Haku on yleensä **O(1)** → erittäin nopea.

---

**✔️ Luettavuus**

Avain kertoo *mitä* arvo kuvaa:

```python
user["email"]
reservation["date"]
```

---

**✔️ Joustava tietorakenne**

Arvot voivat olla:

* merkkijonoja
* kokonaislukuja
* listoja
* toisia dictionaryjä
* jopa funktioita!

---

**✔️ Helppo muokata**

Voit lisätä, poistaa tai päivittää avaimia lennossa.

---

## 🔧 Dictionaryn luonti

**Perusmuoto:**

```python
user = {
    "name": "Ville",
    "email": "ville@example.com",
    "age": 40
}
```

---

**Tyhjä dictionary:**

```python
data = {}
# tai
data = dict()
```

---

**Avain–arvo -parin lisääminen:**

```python
user["phone"] = "040-123-4567"
```

---

## 🔍 Arvojen hakeminen

**Suora haku (virhe jos avainta ei ole):**

```python
print(user["name"])
```

---

**Turvallinen haku `.get()` (ei aiheuta virhettä):**

```python
print(user.get("address"))       # palauttaa None, jos ei löydy
print(user.get("address", "Ei osoitetta"))  # palauttaa oletusarvon
```

Tämä on erityisen hyvä harjoitusvaiheessa, kun avaimet helposti puuttuvat.

---

## ✏️ Dictionaryn muokkaaminen

**Arvon päivittäminen:**

```python
user["email"] = "new-mail@example.com"
```

---

**Poistaminen:**

```python
del user["age"]
# tai turvallisesti:
user.pop("age", None)
```

---

**Kaikkien arvojen tyhjennys:**

```python
user.clear()
```

---

## 🔁 Iterointi (läpikäynti)

**Käydään läpi vain avaimet:**

```python
for key in user:
    print(key)
```

---

**Käydään läpi avaimet ja arvot:**

```python
for key, value in user.items():
    print(key, value)
```

---

**Vain arvot:**

```python
for value in user.values():
    print(value)
```

---

## 🧱 Sisäkkäiset dictionaryt

**Dictionary voi sisältää toisia dictionaryjä:**

```python
reservation = {
    "user": {"name": "Ville", "role": "admin"},
    "resource": {"id": 5, "name": "Meeting room"},
    "date": "2025-12-04"
}

print(reservation["user"]["role"])
```

**Tuloste:**

```
admin
```

Rakenteellinen data on hyvin yleinen esim. [JSON-muodoissa](https://fi.wikipedia.org/wiki/JSON).

---

## 🧪 Dictionary vs list

| Ominaisuus           | Dictionary                                 | List                 |
| -------------------- | ------------------------------------------ | -------------------- |
| Järjestys            | Säilyttää lisäysjärjestyksen (Python 3.7+) | Järjestetty          |
| Hakutapa             | Haku avaimella                             | Haku indeksillä      |
| Hyvä käyttötarkoitus | Rakenteellinen data, tunnisteet            | Järjestetty kokoelma |

Esim. varausjärjestelmässä:

* **List** → monta varausta järjestyksessä
* **Dictionary** → yhden varauksen kentät avaimilla

---

## ⚠️ Sudenkuoppia ja huomioita

**❗ Avainten täytyy olla *uniikkeja***

```python
d = {"a": 1, "a": 2}
print(d)  # {"a": 2}
```

---

**❗ Avainten tulee olla *hashattavia***

Yleensä:

* str ✔️  
* int ✔️  
* tuple ✔️  
* list ✖️ ei käy  

---

**❗ `.get()` on parempi kuin `[ ]` epävarmoissa tilanteissa**

---

## ✨ Hyviä käytäntöjä

**✔️ Käytä selkeitä avaimia**

```python
good = {"price": 10.5}
bad  = {"p": 10.5}
```

---

**✔️ Yhdistä dictionaryt toimiviksi yksiköiksi**

Esim. varaus:

```python
reservation = {
    "id": 1,
    "user_id": 3,
    "room": "A123",
    "date": "2025-12-04"
}
```

---

**✔️ Hyödynnä dictionary comprehensionia**

```python
squares = {x: x*x for x in range(5)}
```

---

## 🧰 Käytännön miniprojekti: käyttäjän tallennus

```python
def create_user(name, email, age):
    return {
        "name": name,
        "email": email,
        "age": age
    }

user = create_user("Ville", "ville@example.com", 40)
print(user)
```

---

## 🎓 Yhteenveto

Dictionary on yksi Pythonin tärkeimmistä tietorakenteista, ja sitä käytetään lähes jokaisessa sovelluksessa → Web-kehityksestä tietorakenteisiin ja tiedostomuotoihin kuten JSON.

---

# 🧱 **Olio-ohjelmointi → Mitä ja miksi?**

## 📜 Taustaa ja historiaa

1970–1980-luvuilla ohjelmistot kasvoivat nopeasti monimutkaisiksi. Perinteinen proseduraalinen ohjelmointi (jossa ohjelma koostui pitkistä funktio- ja aliohjelmaketjuista) alkoi olla vaikeasti hallittavaa. Syntyi tarve mallintaa ohjelmia samankaltaisesti kuin todellinen maailma.

Pioneereja olivat:

* **Simula** (1967) → ensimmäinen kieli, jossa oli luokka-käsitys.
* **Smalltalk** (1972) → ensimmäinen puhdas olio-ohjelmointikieli, jossa *kaikki* oli olio.
* 1990-luvulla: **C++**, **Java**, **Python** ja myöhemmin mm. **C#** toivat olio-ohjelmoinnin laajaan käyttöön.

Keskeinen historiallinen idea oli:

> “Jos ohjelmat mallinnetaan todellisten ilmiöiden ja asioiden kaltaisiksi, ne ovat helpommin ymmärrettäviä, ylläpidettäviä ja laajennettavia.”

Olio-ohjelmoinnista tuli nopeasti yksi ohjelmoinnin pääparadigmoista, ja nykyään sitä käytetään lähes kaikessa sovelluskehityksessä webistä mobiiliin, peliohjelmista palvelinohjelmointiin.

---

## 🧠 Mikä on olio?

Olio on ohjelmassa **kokonaisuus**, joka yhdistää:

* **tiedon** (attribuutit / data)
* **toiminnot** (metodit / funktiot)

Voit ajatella oliota kuin "pientä ohjelmaa ohjelmassa":
esimerkiksi Koira-olio sisältää:

* tietoa: nimi, ikä, rotu
* toimintoja: hauku(), syö(), nukku()

Olio on siis *data + toiminta + rajapinta saman logiikan alla*.

---

## 🎯 Miksi olioita käytetään?

Alla tärkeimmät ohjelmistotuotannolliset syyt.

**✔️ Jäsennys ja hallittavuus**

Oliot jakavat ison ohjelman pieniin loogisiin kokonaisuuksiin.
Kun ohjelma kasvaa, oliopohjainen rakenne pysyy huomattavasti helpommin ylläpidettävänä.

---

**✔️ Uudelleenkäytettävyys**

Luokista voidaan tehdä monta oliota, ja luokista voi tehdä periviä aliluokkia.
Tämä vähentää toisteista koodia ja tukee tehokasta kehitystä.

---

**✔️ Muutoskestävyys**

Jos esim. auton moottorilaskenta muuttuu, muutokset tehdään vain Moottori-luokkaan.
Koko ohjelmaa ei tarvitse korjata.

---

**✔️ Abstraktio ja kapselointi**

Olio piilottaa sisäisen toiminnallisuutensa.
Käyttäjä saa selkeät metodit ("rajapinnan"), eikä muiden tarvitse tietää, miten olio toimii sisäisesti.

---

**✔️ Luonnollinen tapa mallintaa maailmaa**

Kun sovellusta suunnitellaan:

* käyttäjä → olio
* varaus → olio
* peli-hahmo → olio
* pankkitili → olio

Tämä on intuitiivista erityisesti isoissa projekteissa.

---

# 🐍 Olio-ohjelmointi Pythonissa

Pythonissa olio-ohjelmointi on keskeinen osa kieltä, mutta Python ei pakota OOP:ia. Voit tehdä proseduraalisia skriptejä tai rakentaa isoja oliopohjaisia järjestelmiä → valinta on sinun. Tämä tekee Pythonista hyvän opetuskielen.

---

## 🔧 Luokan (class) määrittely

```python
class Dog:
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age        # attribute

    def bark(self):           # method
        print(f"{self.name} barks!")
```

**Mitä tässä tapahtuu?**

* `class Dog:`
  Määrittelee luokan.
* `__init__`
  Python kutsuu tätä automaattisesti, kun luodaan uusi olio.
* `self`
  Viittaa *tähän* olioon.
  Jokainen luokan metodi saa selfin ensimmäisenä parametrina.
* `self.name` ja `self.age`
  Nämä tallentuvat olion sisälle.

---

## 🐾 Olion luominen

```python
my_dog = Dog("Max", 5)
my_dog.bark()
```

Tuloste:

```
Max barks!
```

**Selitys**

* `Dog("Max", 5)` luo uuden olion.
* `my_dog` on olion viite.
* `my_dog.bark()` kutsuu olion metodia.

---

## 🗂️ Attribuutit ja metodit

Pythonissa olion sisällä voi olla:

* **Attribuutteja** (dataa)
* **Metodeja** (toimintoja)

Esimerkki lisätyllä metodilla:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")
```

---

## 🧬 Perintä (inheritance)

Perintä mahdollistaa luokan laajentamisen:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} eats food.")

class Dog(Animal):          # Dog PERII Animal-luokan
    def bark(self):
        print(f"{self.name} barks!")
```

Käyttö:

```python
d = Dog("Buddy")
d.eat()
d.bark()
```

Tuloste:

```
Buddy eats food.
Buddy barks!
```

---

## 🔒 Kapselointi käytännössä

Pythonissa ei ole tiukkaa private-käsitettä, mutta käytetään konventioita:

* `_name` → “älä käytä tätä ulkopuolelta ilman syytä”
* `__name` → name mangling, tekee attribuutin vaikeammin saavutettavaksi

Esimerkki:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # semi-private

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
```

---

## 🧱 Luokan ja olion ero

| Käsite     | Selitys                                                               |
| ---------- | --------------------------------------------------------------------- |
| **Luokka** | Rakenne, malli, ohje, joka määrittää millaisia olioita voidaan luoda. |
| **Olio**   | Luokan konkreettinen toteutuma, jolla on oma tila.                    |

Vertaus:

* **Luokka = muotti**
* **Olio = muotista tehty esine**

---

## 📦 Esimerkki: Olioilla rakennettu pieni sovellus

```python
class Reservation:
    def __init__(self, user, resource, date):
        self.user = user
        self.resource = resource
        self.date = date

    def summary(self):
        return f"{self.user} booked {self.resource} on {self.date}"


res1 = Reservation("Ville", "Meeting Room", "2025-12-10")
print(res1.summary())
```

Tuloste:

```
Ville booked Meeting Room on 2025-12-10
```

Tässä näkyy olioiden pääajatus: ➡️ **Yhdistetään data ja siihen liittyvä toiminta yhteen kokonaisuuteen.**

---