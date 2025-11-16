> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla.

# 💡 Pythonin virallinen tyyliopas → PEP 8

[PEP 8](https://peps.python.org/pep-0008/) on Pythonin virallinen *style guide*, joka määrittelee, miten Python-koodi tulisi kirjoittaa, jotta se olisi selkeää, luettavaa ja yhtenäistä. Oppaan tarkoitus on helpottaa yhteistyötä, vähentää virheitä ja tehdä koodista ammattimaisempaa.

## 🔑 Keskeiset periaatteet

* **Sisennys**
  Käytä neljää välilyöntiä per taso. Ei tabulaattoreita (IDE-ympäristöt esim. Visual Studio Code muotoilee tabulaattorin automaattisesti neljäksi välilyönniksi).

* **Rivien pituus**
  Suositeltu maksimi on 79 merkkiä. Pitkät lausekkeet voi jakaa useille riveille.

* **Tyhjät rivit**
  Käytä tyhjiä rivejä loogisten kokonaisuuksien erottamiseen.

* **Importit**
  Importit kirjoitetaan tiedoston alkuun, yksi per rivi, järjestettynä standardikirjasto → kolmannen osapuolen kirjastot → omat moduulit.

* **Nimeämiskäytännöt**

  * funktiot ja muuttujat: `lowercase_with_underscores`
  * luokat: `CapWords`
  * vakioita muistuttavat: `UPPER_CASE`

* **Asettelu ja välilyönnit**
  Pidä välilyönnit selkeinä esimerkiksi operaattorien ympärillä (`a + b`), mutta vältä turhia välilyöntejä sulkeiden sisällä.

* **Kommentit ja dokumentointi**
  Kommenttien tulee olla ymmärrettäviä ja ajantasaisia. Docstringit kirjoitetaan kolmella lainausmerkillä toimintoja, luokkia ja moduuleja varten.

## 🎯 Miksi PEP 8 on tärkeä?

* Parantaa koodin **luettavuutta** ja **ylläpidettävyyttä**.
* Tekee yhteistyöstä **sujuvampaa**, koska kaikki noudattavat samoja sääntöjä.
* Luo pohjan **ammattimaiselle Python-kehitykselle**.

---

# 🧠 **Muuttujat ja laskuoperaatiot**

## 1️⃣ Mitä muuttuja tarkoittaa?

Muuttuja on nimetty säilytyspaikka, johon ohjelma voi tallentaa tietoa. Voit ajatella muuttujaa kuin laatikkoa, jossa on nimi ja jonka sisään voi laittaa arvoja.

* Muuttuja **syntyy, kun sille annetaan arvo**.
* Muuttujan sisältöä voi käyttää ohjelmoinnissa milloin tahansa.
* Muuttujan arvo voi myös muuttua — siitä nimi *muuttuja*.

---

**💡 Esimerkki:**

```python
age = 25
name = "Ville"
temperature = -3.5
```

## 2️⃣ Muuttujien nimeäminen

Python sallii seuraavat:

✔ Kirjaimet
✔ Numerot (ei alussa)
✔ Alaviiva `_`

Hyviä käytäntöjä:

* Käytä kuvaavia nimiä: `total_price`, `average_speed`
* Käytä snake_case-tyyliä: sanat erotetaan alaviivalla
* Älä aloita numerolla

❌ Vältä: `1name`, `x`, `Price€`

---

## 3️⃣ Pythonin perusarvotyypit muuttujissa

| Tyyppi  | Esimerkki        | Käyttö                 |
| ------- | ---------------- | ---------------------- |
| `int`   | `age = 30`       | Kokonaisluvut          |
| `float` | `temp = 3.14`    | Desimaaliluvut         |
| `str`   | `text = "Hello"` | Tekstimuotoiset tiedot |
| `bool`  | `is_open = True` | Tosi/epätosi           |

---

## 4️⃣ Laskuoperaatiot Pythonissa

**💡 Peruslaskut:**

| Operaatio        | Merkki | Esimerkki                      |
| ---------------- | ------ | ------------------------------ |
| Yhteenlasku      | `+`    | `5 + 3`                        |
| Vähennys         | `-`    | `10 - 2`                       |
| Kertolasku       | `*`    | `7 * 2`                        |
| Jakolasku        | `/`    | `10 / 2` → tulos on aina float |
| Kokonaislukujako | `//`   | `10 // 3` → tulos 3            |
| Jakojäännös      | `%`    | `10 % 3` → tulos 1             |
| Potenssi         | `**`   | `2 ** 3` → tulos 8             |

---

## 5️⃣ Laskeminen muuttujilla

Muuttujia voi käyttää kuten tavallisia numeroita:

```python
a = 10
b = 3

summa = a + b
ero = a - b
tulo = a * b
osamaara = a / b

print(summa, ero, tulo, osamaara)
```

---

**💡 Muuttujan arvon päivittäminen**

```python
counter = 0
counter = counter + 1
```

Lyhyempi ja yleisempi:

```python
counter += 1
```

Saatavilla myös: `-=`, `*=`, `/=`, `//=`, `%=`.

---

## 6️⃣ Laskuoperaatiot käytännössä – pieni varausjärjestelmäesimerkki

Ajatellaan vähäistä varausjärjestelmää, jossa lasketaan varauksen hinta.

```python
hours = 5
price_per_hour = 12.5

total_price = hours * price_per_hour

print("Varauksen kokonaishinta on:", total_price, "€")
```

Tulostus:

```
Varauksen kokonaishinta on: 62.5 €
```

---

## 7️⃣ Tekstin ja numeroiden yhdistäminen

Teksti ja numerot on yhdistettävä **str()**-funktiolla, jos käytät `+`-operaattoria.

```python
age = 20
print("Ikä on " + str(age))
```

Tai f-string (suositeltu moderni tapa):

```python
print(f"Ikä on {age}")
```

---

# 🗂️ **Listojen hallinta**

## 1️⃣ Mikä lista on?

Lista on järjestetty kokoelma arvoja.
Voit ajatella listaa kuin hyllyä, jossa jokaisella paikalla on numero ja arvo.

* Listan arvot voivat olla *minkä tahansa tyyppisiä*
* Lista voi muuttua (se on *muokattava tietorakenne*)
* Arvoja viitataan indeksin avulla
  → indeksit alkavat 0:sta

---

**💡 Esimerkki:**

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = [1, "Ville", True, 3.14]
```

---

## 2️⃣ Arvojen hakeminen listasta

**💡 Sijainnin perusteella (indeksi):**

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # apple
print(fruits[2])  # cherry
```

---
**💡 Viimeinen alkio:**

```python
print(fruits[-1])  # cherry
```

---

## 3️⃣ Arvon muuttaminen

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"

print(fruits)  # ["apple", "orange", "cherry"]
```

---

## 4️⃣ Alkioiden lisääminen ja poistaminen

**💡 Lisää listaan**

```python
numbers = [1, 2, 3]

numbers.append(4)       # lisää loppuun
numbers.insert(1, 10)   # lisää kohtaan 1

print(numbers)  # [1, 10, 2, 3, 4]
```

---

**💡 Poista listasta**

```python
numbers.remove(10)   # poistaa arvon 10
numbers.pop()        # poistaa viimeisen
numbers.pop(0)       # poistaa indeksin 0
```

---

## 5️⃣ Listan pituus

```python
names = ["Liisa", "Matti", "Ville"]
print(len(names))   # 3
```

---

## 6️⃣ Silmukointi listan läpi

**💡 For-silmukka:**

```python
cars = ["Audi", "BMW", "Volvo"]

for car in cars:
    print(car)
```

---

**💡 Indeksien kanssa:**

```python
for i in range(len(cars)):
    print(i, cars[i])
```

---

## 7️⃣ Listan järjestäminen ja kääntäminen

**💡 Järjestys:**

```python
numbers = [5, 1, 8, 3]
numbers.sort()

print(numbers)  # [1, 3, 5, 8]
```

---

**💡 Käänteinen järjestys:**

```python
numbers.sort(reverse=True)
```

---

**💡 Kääntäminen ilman lajittelua:**

```python
numbers.reverse()
```

---

## 8️⃣ List comprehension — tehokas listaoperaatio

Lyhyt tapa luoda listoja:

```python
numbers = [x * 2 for x in range(5)]
print(numbers)  # [0, 2, 4, 6, 8]
```

---

**💡 Esimerkki varausjärjestelmästä: luo lista nimitägeistä:**

```python
names = ["Ville", "Anna", "Matti"]
tags = [name.lower() for name in names]
```

---

# 🧩 **Kaksiulotteiset listat (2D listat)**

Kaksiulotteinen lista = lista, jonka alkiot ovat listoja. Voit kuvitella sen matriisiksi tai taulukoksi:

```
[ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]
```

## 1️⃣ Luominen

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

## 2️⃣ Arvojen hakeminen

```python
print(matrix[0][1])  # tulos 2
print(matrix[2][0])  # tulos 7
```

Ensimmäinen indeksi = rivi
Toinen indeksi = sarake

---

## 3️⃣ Edeten kaksiulotteisen listan läpi

**💡 Perinteinen tapa:**

```python
for row in matrix:
    for value in row:
        print(value)
```

---

**💡 Indeksien kanssa:**

```python
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")
```

---

## 4️⃣ Käytännön esimerkki kahdenulotteisesta listasta

Oletetaan varausjärjestelmä, jossa 7 päivän ja 24 tunnin varauskalenteri luodaan 0 (vapaa) arvoilla:

```python
calendar = [[0 for hour in range(24)] for day in range(7)]

# Merkitään maanantai klo 10 varatuksi
calendar[0][10] = 1

print(calendar[0][10])  # 1 (varattu)
```

---