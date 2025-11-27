> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla.

# 📁 Tiedostot, käyttöjärjestelmä ja Python: Mitä tapahtuu?

Tiedostojen käsittely on yksi ohjelmoinnin tärkeimmistä osa-alueista. Jokainen sovellus, aina pienestä skriptistä isoihin palveluihin, **lukee**, **kirjoittaa**, **päivittää** ja **poistaa** tietoa käyttämällä käyttöjärjestelmän tarjoamia mekanismeja.

## 🧠 Miten käyttöjärjestelmä näkee tiedoston?

Käyttöjärjestelmä hallitsee kaikkea, mikä liittyy tiedostoihin:

* missä ne sijaitsevat (tallennuslaite, polku)
* kuka saa lukea/kirjoittaa (oikeudet)
* miten data kulkee ohjelman ja tallennusmedian välillä (I/O-pino)
* miten tiedostoja lukitaan, välimuistitetaan ja synkronoidaan

Kun ohjelma avaa tiedoston, käyttöjärjestelmä antaa `tiedostokahvan` (*file handle*), jonka kautta ohjelma voi käyttää tiedostoa.

---

## 📖 Mitä tapahtuu, kun tiedostoa luetaan?

Kun kutsut esimerkiksi Pythonissa:

```py
with open("data.txt", "r", encoding="utf-8") as f:
    sisältö = f.read()
```

Käyttöjärjestelmä tekee seuraavaa:

1. **📌 Polun tarkistus**
   Löytyykö tiedosto? Onko oikeudet kunnossa?

2. **🔑 Tiedoston avaaminen**
   OS liittää ohjelmalle tiedostokahvan → `f` on vain *osoitin* tähän *kahvaan*.

3. **📤 Tiedon siirto**
   Data luetaan levyltä **välimuistiin (buffer)** ja siitä ohjelmalle: Luku ei välttämättä tapahdu ”bitti kerrallaan”, vaan OS optimoi lukua.

4. **📦 Esitys Pythonissa**
   Tiedostosisältö muunnetaan merkkijonoksi (`str`) tai byteiksi (`bytes`), riippuen avausmoodista.

---

## ✍️ Mitä tapahtuu, kun tiedostoon kirjoitetaan?

Esimerkiksi:

```py
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Uusi sisältö")
```

Käyttöjärjestelmä tekee:

1. **📌 Polun tarkistus**
   Onko lupa kirjoittaa? Onko levy tilassa?

2. **🧽 Tiedoston mahdollinen tyhjennys**
   `w`-moodi tyhjentää tiedoston ennen kirjoittamista.

3. **📥 Välimuisti (buffer)**
   Tieto ei mene suoraan levylle → ensin kirjoitetaan *bufferiin*.

4. **💾 Flush → Sync → Levy**
   OS kirjoittaa datan oikeasti levylle, usein pientä viivettä vastaan:

   * `f.write` → bufferiin
   * `f.flush` → OS:lle
   * `fsync` → fyysiselle levylle

Kirjoitus on itse asiassa monivaiheinen ja `OS` optimoi sitä nopeuden vuoksi.

---

## 🧲 Miksi tiedoston oikeaoppinen avaaminen ja sulkeminen on niin tärkeää?

**✔️ 1. Vältytään datan korruptoitumiselta**

Jos tiedosto jää auki, viimeiset kirjoitukset saattavat olla vain bufferissa → eivät tallennu levylle.

---

**✔️ 2. Vapautetaan resurssit**

Avoimet tiedostot kuluttavat:

* tiedostokahvoja (rajallinen määrä per prosessi)
* muistia (`bufferit`)
* mahdollisesti lukituksia (`file locks`)

---

**✔️ 3. Tiedoston lukitus vapautuu**

Jos tiedosto on lukittuna, muut sovellukset eivät pääse siihen käsiksi → **ongelmia monen käyttäjän järjestelmissä**.

---

**✔️ 4. Helpottaa virhetilanteiden hallintaa**

Oikeaoppinen avausmalli `with open(...)` takaa, että tiedosto suljetaan automaattisesti — myös virheen sattuessa.

---

## 🐍 Pythonin oikeaoppinen käyttö

**📦 Tiedoston lukeminen**

```py
with open("data.txt", "r", encoding="utf-8") as f:
    sisältö = f.read()
    print(sisältö)
```

---

**✍️ Tiedoston kirjoittaminen**

```py
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hei maailma!\n")
```

---

**➕ Tiedoston päivittäminen (`append`)**

```py
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Lisätty rivi\n")
```

---

**💾 Tiedoston lukeminen riveittäin**

```py
with open("data.txt", "r", encoding="utf-8") as f:
    for rivi in f:
        print(rivi.strip())
```

---

## ⚠️ Vaaran paikat → Nämä kaatavat skriptejä ja ohjelmia!

**❌ 1. Tiedostoa ei suljeta**

→ data ei tallennu
→ OS-lukitus jää päälle
→ resurssivuoto

Siksi **älä käytä koskaan**:

```py
f = open("data.txt", "w")
f.write("Hei")
# f.close() unohtui!
```

---

**❌ 2. Kirjoittaminen ilman oikeuksia**

→ PermissionError
→ ohjelma voi kaatua
→ lokit eivät päivity

---

**❌ 3. Tiedoston tyhjentyminen vahingossa**

`w`-moodi **aina korvaa** tiedoston.
Turvallisempi tapa on käyttää:

* `a` (append)
* tai `r+` jos haluat sekä lukea että kirjoittaa ilman tyhjennystä

---

**❌ 4. Tiedostopolut Windows vs Linux**

Windows → `C:\\data\\tiedosto.txt`
Linux → `/home/user/data/tiedosto.txt`

Parempi tapa:

```py
from pathlib import Path

polku = Path("data") / "log.txt"
```

---

**❌ 5. Suuret tiedostot → muistiongelmia**

`f.read()` lukee KOKO tiedoston kerralla.

Parempi tapa:

```py
for chunk in f.read(1024):
    käsittele(chunk)
```

---

**❌ 6. Samanaikaiset kirjoitukset**

→ tiedot voivat mennä sekaisin
→ tarvitaan lukituksia tai transaktioita

---

## 🎓 Yhteenveto 

| Osa-alue            | Miksi tärkeää?                        | Python-esimerkki            |
| ------------------- | ------------------------------------- | --------------------------- |
| Tiedoston avaaminen | Luo yhteyden tiedostoon               | `open("file.txt")`          |
| Tiedostokahva       | OS antaa ohjelmalle resurssin         | `f = open(...)`             |
| Luku                | Data → buffer → ohjelma               | `f.read()`                  |
| Kirjoitus           | Ohjelma → buffer → levy               | `f.write()`                 |
| Sulkeminen          | Vapauttaa resurssit + tallentaa datan | `f.close()` tai `with open` |
| Vaaran paikat       | Estää kaatumiset ja datavirheet       | `with open(...)`            |

---

# 🐍 Huonot vs hyvät käytännöt Pythonissa

Verkko on täynnä erilaisia vinkkejä ja neuvoja tiedostojen käsittelyyn. Koska skripti/ohjelma ottaa yhteyttä tiedostoon ja tiedostojärjestelmään käyttöjärjestelmän kautta, saattaa väärät tavat aiheuttaa pahimmillaan todella arvaamattomia tilanteita. Käyttöjärjestelmässä on usein samaan aikaan käynnissä useita ohjelmia, joten samoja resursseja käytetään lähtökohtaisesti. Tämä sama pätee käyttäjiin, eli käyttöjärjestelmässä saattaa olla samaan tai eri aikaan useita eri käyttäjiä. 

## 1️⃣ Unohtunut `close()` → “kyllä tämä nyt toimii…”

**❌ Huono tapa**

```py
f = open("data.txt", "r", encoding="utf-8")
content = f.read()
print(content)
# f.close() unohtui
```

**Miksi tämä on ongelma?**

* Tiedosto voi **jäädä auki**:

  * Bufferit ei välttämättä tyhjenny oikein.
  * OS-resurssit kuluvat (liikaa avoimia tiedostoja).
  * Joissain ympäristöissä (pitkäkestoiset palvelut) tämä on iso ongelma.

---

**✅ Parempi tapa → Käytä `with`-rakennetta**

```py
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
# Tiedosto suljetaan automaattisesti täällä
```

---

## 2️⃣ Tiedoston avaaminen väärässä moodissa ja datan hukkaaminen

**❌ Huono tapa → “Avataan vaan `w` ja kirjoitetaan”**

```py
# Tarkoitus oli lisätä uutta lokiin, mutta...
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("New log line\n")
```

**Miksi tämä on ongelma?**

* `w`-moodi **tyhjentää koko tiedoston ensin**.
* Jos logi tai data on tärkeää, tuhoat kaiken vanhan sisällön joka kerta.

---

**✅ Parempi tapa → Käytä `a` tai tarkempaa logiikkaa**

```py
# Lisää rivejä olemassa olevan perään
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log line\n")
```

Tai jos haluat tarkistaa ensin:

```py
from pathlib import Path

log_path = Path("log.txt")
if log_path.exists():
    mode = "a"
else:
    mode = "w"

with open(log_path, mode, encoding="utf-8") as f:
    f.write("New log line\n")
```

---

## 3️⃣ Kaiken nielevä `except:` piilottaa virheet

**❌ Huono tapa → “korjataan vaan try–exceptillä”**

```py
try:
    f = open("data.txt", "r")
    data = f.read()
    f.close()
except:
    print("Something went wrong")
```

**Miksi tämä on ongelma?**

* `except:` nappaa **kaiken**:

  * myös ohjelmointivirheet (IndentationError, NameError, yms.)
  * myös KeyboardInterrupt (Ctrl+C)
* Et näe, **mikä oikeasti meni pieleen**.
* Virheet jäävät helposti piiloon → vaikeampi debugata.

---

**✅ Parempi tapa → Rajaa virhe ja käytä `with`**

```py
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found – check the path.")
except PermissionError:
    print("No permission to read the file.")
```

Tarvittaessa voit lisätä myös “yleisen” haun, mutta erikseen:

```py
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## 4️⃣ `eval()` tiedoston sisältöön → Tietoturvaklassikko 💣

Netissä näkee joskus vinkkejä tyyliin “lue asetukset tai data `eval`-funktiolla”.

**❌ Todella huono tapa**

```py
with open("config.txt", "r", encoding="utf-8") as f:
    config = eval(f.read())  # esim. "{'debug': True}"
```

**Miksi tämä on vaarallista?**

* `eval()` suorittaa **mitä tahansa Python-koodia**:

  * jos tiedostoon on päässyt hyökkääjä → koodin suoritus
  * ei sovi koskaan tilanteeseen, jossa data tulee ulkoa
* Tämä on suora tietoturvariski.

---

**✅ Parempi tapa → Käytä turvallista formaattia**

Esim. JSON:

```py
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print(config["debug"])
```

---

## 5️⃣ Kaikki muistiin kerralla → Toimii demossa, mutta ei tuotannossa

**❌ Huono tapa → Luetaan megat tai gigat kerralla**

```py
with open("really_big_file.log", "r", encoding="utf-8") as f:
    data = f.read()  # koko tiedosto muistiin
    # käsittely...
```

**Miksi tämä voi olla ongelma?**

* Jos tiedosto on iso:

  * muistinkulutus kasvaa valtavaksi
  * skripti hidastuu ja voi kaatua
* Toimii “näytekoodissa”, mutta ei oikeassa ympäristössä.

---

**✅ Parempi tapa → Rivittain tai paloissa**

**Rivittain:**

```py
with open("really_big_file.log", "r", encoding="utf-8") as f:
    for line in f:
        process(line)
```

---

**Paloissa (chunk):**

```py
def read_in_chunks(file_obj, chunk_size=1024):
    while True:
        data = file_obj.read(chunk_size)
        if not data:
            break
        yield data

with open("big.bin", "rb") as f:
    for chunk in read_in_chunks(f):
        process_binary(chunk)
```

---

## 6️⃣ Kovakoodatut polut → “toimii minun koneella” 🧨

**❌ Huono tapa**

```py
# Windows-koneen kovakoodattu polku
f = open("C:\\Users\\Ville\\Desktop\\data\\tiedot.txt", "r", encoding="utf-8")
```

**Miksi tämä on huono?**

* Ei toimi:

  * toisella käyttäjällä
  * toisessa käyttöjärjestelmässä
  * palvelimella
* Rikkoo siirrettävyyden (“works on my machine” -syndrooma).

---

**✅ Parempi tapa → Suhteelliset polut ja `pathlib`**

```py
from pathlib import Path

base_dir = Path(__file__).parent  # hakemisto, jossa skripti sijaitsee
data_file = base_dir / "data" / "tiedot.txt"

with open(data_file, "r", encoding="utf-8") as f:
    content = f.read()
```

---

## 7️⃣ Useita funktioita, jotka jakavat “globaalin” tiedostokahvan

**❌ Huono tapa → Globaali file-handle**

```py
f = open("data.txt", "r", encoding="utf-8")

def read_first_line():
    return f.readline()

def read_second_line():
    return f.readline()

# jossain:
print(read_first_line())
print(read_second_line())
f.close()
```

**Miksi tämä on huono?**

* Funktiot ovat riippuvaisia *globaalista tilasta* → vaikeampi testata.
* Jos joku unohtaa sulkea tai muuttaa f:n tilaa → sivuvaikutuksia.
* Rikkoo hyvää ohjelmointityyliä (funktioiden pitäisi olla mahdollisimman selkeitä ja ennustettavia).

---

**✅ Parempi tapa → Anna tiedoston nimi tai sisältö parametrina**

```py
from pathlib import Path

def read_first_two_lines(path: Path) -> tuple[str, str]:
    with open(path, "r", encoding="utf-8") as f:
        first = f.readline().rstrip("\n")
        second = f.readline().rstrip("\n")
    return first, second

path = Path("data.txt")
line1, line2 = read_first_two_lines(path)
print(line1, line2)
```

---

## 8️⃣ Race condition: `if exists` + `open`

Netissä näkee usein:

```py
import os

if os.path.exists("data.txt"):
    f = open("data.txt", "x")  # "create new file"
else:
    f = open("data.txt", "w")
```

**Miksi tämä voi olla huono?**

* Jos samalla hetkellä toinen prosessi luo tai poistaa tiedoston:

  * ehtolauseen ja open-kutsun välillä → **race condition**
* Harvoin ongelma pienessä opiskelijaskriptissä, mutta tärkeä idea ymmärtää.

---

**✅ Parempi tapa → Luota suoraan open-kutsuun ja virheenkäsittelyyn**

```py
from pathlib import Path

path = Path("data.txt")

try:
    # "x" → luo tiedoston, jos sitä ei ole
    with open(path, "x", encoding="utf-8") as f:
        f.write("Initial content\n")
except FileExistsError:
    # tiedosto oli jo olemassa
    with open(path, "a", encoding="utf-8") as f:
        f.write("Appended line\n")
```

---

## 🎯 Yhteenveto → Mitä kannattaa opetella “haistamaan” vääräksi?

Kun selaat verkon koodiesimerkkejä, hälytyskellojen pitäisi soida, jos näet:

* ❌ Tiedosto avataan `open()` mutta `close()` puuttuu ja `with`-rakennetta ei käytetä.
* ❌ `w`-moodia käytetään “varmuuden vuoksi” miettimättä, että se tyhjentää tiedoston.
* ❌ `eval()` käytetään tiedoston sisältöön.
* ❌ Kaikki data luetaan kerralla muistiin, vaikka voisi käsitellä riveittäin.
* ❌ Kovakoodattuja polkuja, jotka toimivat vain yhdessä ympäristössä.
* ❌ Globaalit tiedostokahvat, joita funktiot pyörittävät edestakaisin.
* ❌ Kaiken nielevät `except:`-lohkot ilman tarkennusta.