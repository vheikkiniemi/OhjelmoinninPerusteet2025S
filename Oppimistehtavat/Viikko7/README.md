> [!NOTE]  
> Materiaali on luotu ChatGPT:n ja Copilotin avulla.

# 🐍 Viikko 7: Tietorakenteiden refaktorointi → Listasta sanakirjaksi tai olioksi

Tehtävän tavoitteena on harjoitella:

* listarakenteen muuttamista **sanakirjaksi (`dict`)** tai **olioksi (`class`)**
* koodin **refaktorointia** ilman toiminnallisuuden muuttamista
* selkeämmän ja luettavamman koodin tekemistä (ei enää “mystisiä” indeksejä tyyliin `varaus[8]`)

> [!NOTE]  
> Suositus on käyttää **sanakirjaa (`dict`)**.
> Vaihtoehtoisesti voit tehdä version **olioilla (`class Varaus`)**, jos haluat haastetta.
> **VAHVA SUOSITUS:** Käytä tekoälyä kaverina (koska niin myös oikeasti tällaisissa tehtäisiin) 

---

> [!NOTE]
> Halutessa työn voi tehdä **`pareittain (max. kaksi)`**.
> Tällöin kohdassa [Palautusohje Itslearningiin](#-palautusohje-itslearningiin) pari tekee vain yhden palautuksen, johon on yhdistetty molemmat.

---

## 📄 Kuvaus

* Sinulle on annettu tekstitiedosto **`varaukset.txt`**, jossa jokainen rivi sisältää yhden varauksen tiedot.
* Lisäksi sinulle on annettu Python-skripti **`lue_varaukset.py`** (viikon 4B -työpajan pohja), joka:

  * lukee `varaukset.txt` -tiedoston
  * muuntaa rivit listaksi (`varaus = varaus.split('|')`)
  * tekee erilaisia tulosteita hyödyntäen listan indeksejä (`varaus[1]`, `varaus[8]`, ...).

Tällä hetkellä ohjelma käyttää **listoja**, joissa varauksen eri kentät ovat **kiinteissä indekseissä**. Esimerkiksi:

```python
if varaus[8]:
    print(f"- {varaus[1]}, {varaus[9]}, {varaus[4].strftime('%d.%m.%Y')} klo {varaus[5].strftime('%H.%M')}")
```

Tavoitteena on muuttaa ohjelma niin, että:

* **jokainen varaus** tallennetaan joko

  * sanakirjana (**suositus**) tai
  * oliona (**vaihtoehtoinen versio**)
* muu koodi päivitetään käyttämään **avainsanoja** tai **olioattribuutteja** indeksien sijaan.

---

## 🔧 Tietorakenteet tehtävässä

### Vaihtoehto A → sanakirja (suositus ✅)

Yksi varaus voisi näyttää tältä:

```python
varaus = {
    "id": 123,
    "nimi": "Anna Virtanen",
    "sahkoposti": "anna.virtanen@example.com",
    "puhelin": "0401234567",
    "paiva": datetime.date(...),
    "kellonaika": datetime.time(...),
    "kesto": 2,
    "hinta": 19.95,
    "vahvistettu": True,
    "kohde": "Kokoustila A",
    "luotu": datetime.datetime(...),
}
```

Käyttö esimerkki:

```python
if varaus["vahvistettu"]:
    print(f"- {varaus['nimi']}, {varaus['kohde']}, {varaus['paiva'].strftime('%d.%m.%Y')}")
```

---

### Vaihtoehto B → olio (`class Varaus`) (vaihtoehto 🚀)

Luokka voisi näyttää esimerkiksi tältä:

```python
class Varaus:
    def __init__(self, varaus_id, nimi, sahkoposti, puhelin,
                 paiva, kellonaika, kesto, hinta,
                 vahvistettu, kohde, luotu):
        self.varaus_id = varaus_id
        self.nimi = nimi
        self.sahkoposti = sahkoposti
        self.puhelin = puhelin
        self.paiva = paiva
        self.kellonaika = kellonaika
        self.kesto = kesto
        self.hinta = hinta
        self.vahvistettu = vahvistettu
        self.kohde = kohde
        self.luotu = luotu

    # Esimerkkimetodeja
    def is_confirmed(self):
        return self.vahvistettu

    def is_long(self):
        return self.kesto >= 3

    def total_price(self):
        return self.kesto * self.hinta
```

Käyttö esimerkki:

```python
if varaus.is_confirmed():
    print(f"- {varaus.nimi}, {varaus.kohde}, {varaus.paiva.strftime('%d.%m.%Y')}")
```

---

## ✅ Tehtäväohjeet

1. **Luo kansio** `Viikko7` omaan Git-repoosi.

2. **Kopioi** opettajan jakamat tiedostot (**`varaukset.txt`** ja **`lue_varaukset.py`**) tähän kansioon.

3. Aja ohjelma kerran ja varmista, että se toimii **alkuperäisessä** muodossa (listaversio).

4. Etsi koodista kohta, jossa rivi pilkotaan listaksi, esim.:

   ```python
   varaus = varaus.split('|')
   ```

5. **Tee funktio**, joka muuttaa listan sanakirjaksi **tai** olioksi.
   Esim. sanakirjaversiossa:

   ```python
   def muunna_varaustiedot(varaus_lista: list[str]) -> dict:
       return {
           "id": int(varaus_lista[0]),
           "nimi": varaus_lista[1],
           # ...
       }
   ```

   **Tai olioversiossa:**

   ```python
   def muunna_varaustiedot(varaus_lista: list[str]) -> Varaus:
       return Varaus(
           varaus_id=int(varaus_lista[0]),
           nimi=varaus_lista[1],
           # ...
       )
   ```

6. **Muuta `hae_varaukset`-funktiota** niin, että:

   * se ei enää palauta listoja, vaan:

     * joko listan sanakirjoja: `list[dict]`
     * tai listan olioita: `list[Varaus]`
   * et enää lisää otsikkoriviä listaan (ei `varaukset[1:]` -kikkailua myöhemmin).

7. Käy läpi skripti ja **korvaa indekseihin viittaavat kohdat**:

   * Esim. `varaus[1]` → `varaus["nimi"]` tai `varaus.nimi`
   * Esim. `varaus[8]` → `varaus["vahvistettu"]` tai `varaus.vahvistettu`
   * Esim. `varaus[6] * varaus[7]` → esim. `varaus["kesto"] * varaus["hinta"]` tai `varaus.total_price()`

8. Varmista, että ohjelma tekee **saman logiikan** kuin alkuperäinen:

   * tulostaa vahvistetut varaukset
   * tulostaa pitkät varaukset
   * laskee kokonaistulot jne. (riippuen pohjakoodista)

9. Lisää kommentti tiedoston alkuun, jossa kerrot:

   * käytätkö **sanakirjoja** vai **olioita**
   * miksi tämä tuntuu sinusta **selkeämmältä** kuin pelkät listat.

---

## 💡 Vihjeitä

* Tee muutos **askel kerrallaan**, ei kaikkea kerralla:

  1. ensin `muunna_varaustiedot`
  2. sitten `hae_varaukset`
  3. sitten yksi tulostusfunktio
  4. ja lopuksi loput.
* Jos käytät sanakirjaa, varmista että **avainten nimet ovat loogisia**: `nimi`, `paiva`, `kesto`, `hinta`, `vahvistettu`, `kohde`, …
* Jos käytät oliota, tee ainakin pari **metodia**, joita oikeasti käytät:

  * esim. `is_confirmed()`, `is_long()`, `total_price()`.
* Jos saat `KeyError`-virheen → avain kirjoitettu väärin.
* Jos saat `AttributeError`-virheen → käytät `varaus.nimi`, vaikka sinulla on sanakirja (`varaus["nimi"]`).

---

## ⭐ Bonustehtäviä (valinnaisia)

**💎1️⃣**
Tee ohjelmasta **kaksi versiota**:

* toinen käyttää **sanakirjoja**
* toinen **olioita**

Vertaile lyhyesti kommenteissa: kumpi on luettavampi?

---

**💎2️⃣**
Lisää olio-/sanakirjarakenteeseen uusi kenttä, esim. `"asiakasnumero"` tai `"lisatiedot"`, ja päivitä logiikka käyttämään sitä (esim. tulosteessa).

---

**💎3️⃣**
Tee olioluokkaan (`class Varaus`) metodi:

```python
def tulosta_yhteenveto(self):
    # tulostaa yhden varauksen yhteenvedon selkeässä muodossa
```

ja käytä tätä metodia jossakin kohtaa tulostuksessa.

---

**💎4️⃣**
Lisää tyyppivihjeet kaikkiin uusiin funktioihin.

Esim. sanakirjaversio:

```python
def hae_varaukset(tiedoston_nimi: str) -> list[dict]:
    ...
```

Olioversio:

```python
def hae_varaukset(tiedoston_nimi: str) -> list[Varaus]:
    ...
```

---

## 📤 Palautusohje Itslearningiin

Palauta **linkki GitHub-repoon** ja **kuvankaappaus konsolista**, jossa näkyy ohjelman suoritus ja tulostus.

> [!NOTE]
> Ota kuvakaappaus ilman bonustehtäviä

---

## 😀 Hyvä fiilis tekemiseen!

**Muista:** nyt et “vain koodaa uutta ohjelmaa”, vaan **parannat olemassa olevaa koodia** → Tämä on iso osa oikeaa ohjelmoijan työtä.

Refaktorointi (koodin siistiminen) on taito, jota tarvitaan **joka projektissa**.
Tämä tehtävä on ensimmäinen askel siihen suuntaan. 💪
