> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla.

# 🧩 Pienimuotoinen ohjelmointiprojekti vaihe vaiheelta

**🧠 Mitä, miksi ja mitä tapahtuu?**

Tervetuloa ensimmäisen ohjelmointiprojektin pariin! 🎉

Tämä materiaali on kirjoitettu niin, että voit aloittaa **vaikka et olisi koskaan tehnyt yhtään projektia** → Et ohjelmointia, et ryhmäprojekteja, et mitään projektia. Kaikki on sinulle täysin uutta? Se on täysin ok. Tämä on sinulle kirjoitettu.

Ajattele tätä pienenä matkakertomuksena: aloitat tyhjästä ja lopulta sinulla on toimiva ohjelma, joka käsittelee dataa ja tulostaa tuloksia komentoriville.

---

## 1. 🔍 Ongelman ymmärtäminen

**✨ Mitä olemme tekemässä → ja miksi se on tärkeää?**

Ennen kuin yhtään riviä koodia kirjoitetaan, pysähdymme kysymään hyvin yksinkertaisen kysymyksen:

---

**❓Mitä olemme ratkaisemassa?**

Tämä vaihe on usein aloitteleville ohjelmoijille hankala, koska mieli haluaisi mennä suoraan tekemiseen:

> ”Anna koodi, haluan vain nähdä miten se toimii!”

Mutta ohjelmointi ei ole vain koodin naputtelua — ohjelmointi on ongelman ratkaisemista. Jos ongelmaa ei ymmärrä, **ei voi valita oikeaa ratkaisua**.

---

**⚠️ Mitä tapahtuu, jos tämän vaiheen ohittaa?**

* Koodi alkaa täyttyä irrallisista kokeiluista
* Lopputuloksena syntyy ”koodisoppaa” 🍲
* Ongelma ei ratkea tai ratkeaa väärällä tavalla
* Aikaa kuluu enemmän kuin jos olisi pysähtynyt alussa

---

**🧠 Vertaus:**

> Rakentaisitko talon ilman että tiedät, montako huonetta tulee? Samaa on ohjelmointi ilman ongelman ymmärtämistä.

---

**🧭 Esimerkkiongelma:**

> Meillä on käytössä dataa, mutta emme tiedä miten sitä saisi järkevästi hyödynnettyä.

> [!TIP]  
> Edellinen on hyvin yleinen tilanne nykyään esim. organisaatioissa, koska erilaista dataa on saatavilla valtava märää.  
> **Ohjelmointitaito tekee datasta käyttökelpoisen!** → **[Tutustu tiedon pyramidiin eli DIKW-pyramidiin](https://fi.wikipedia.org/wiki/DIKW-pyramidi)**

---

## 2. ✏️ Ratkaisun suunnittelu

**✂️ Miten ohjelma ratkaisee ongelman askel askeleelta?**

Kun ymmärrämme mitä haluamme tehdä, mietimme **Miten tämän voisi ratkaista?**

> **👉 Tässä vaiheessa ei kirjoiteta vielä koodia → Mietitään vain rakennetta.**

---

**Esimerkiksi projektissamme:**

* On CSV-tiedosto (esim. tuntikohtaista dataa)
* Tavoitteenamme on tehdä **kuukausitasoisia yhteenvetoja**
* Meidän täytyy siis:

  1. Lukea tiedosto rivi riviltä
  2. Erotella sarakkeet
  3. Poimia päivämäärästä kuukausi
  4. Muuntaa numerot oikeiksi numeroiksi
  5. Laskea kuukausikohtaiset summat
  6. Tulostaa tulos

> **👉 Tästä syntyy kuin pieni kartta tai resepti.**

---

**⚠️ Mitä tapahtuu, jos suunnittelun ohittaa?**

* Koodista tulee sekavaa, koska et tiedä mitä seuraavaksi tehdä
* Teet saman työn kahdesti (tai kolme kertaa…)
* Funktiot jäävät puuttumaan → koodi kasvaa yhdeksi jättiläiseksi
* Ongelmia on vaikea löytää ja korjata

---

**🧠 Vertaus:**

> Et lähtisi rakentamaan IKEA-kalustetta ilman ohjeita (toivottavasti). Suunnittelu on kuin kokoamisohje → Se säästää hermot ja vähentää virheitä.

---

## 3. ⚙️ Ympäristön valmistelu

**🔧 Mitä työkaluja tarvitsemme?**

Aivan kuten kokki tarvitsee veitsen ja pannun, ohjelmoija tarvitsee mm.:

* Pythonin 🐍 → **Ohjelmointikielen**
* Visual Studio Coden 🧰 → **Ohjelmointiympäristön (IDE)**
* Projektikansion 📁 → **Ohjelma perustuu tiedostoihin**
* Tiedoston `2025.csv` → **Datan**

Tässä vaiheessa testataan myös, että kaikki toimii:

```python
print("Projektimme alkaa!")
```

> Jos tämä toimii, kaikki toimii.

---

**⚠️ Mitä tapahtuu, jos ympäristöä ei laita kuntoon?**

* Koodi ei käynnisty
* Tiedostoja ei löydy
* Polut menevät sekaisin
* VS Code ei ymmärrä Pythonia

---

**🧠 Vertaus:**

> Yritäpä paistaa lettuja ilman paistinpannua → Hankalaa.

---

## 4. 💻 Perusversion toteutus

**📌 Ensin yksinkertainen → sitten hienompi (iteraatiivinen prosessi)**

Ohjelmointiprojekti ei koskaan rakennu kerralla oikein. Siksi luodaan ensin **perusversio**, joka tekee hyvin vähän esim.:

* lukee tiedoston
* tulostaa muutaman rivin

Se ei tee vielä hienoa laskentaa → Eikä kuulu tehdäkään.

> [!TIP]  
> **Muista edetä pienen askelin → Muutos → Testaus → Muutos → ...**

Tärkeintä on saada **perusputki toimimaan**.

---

**⚠️ Mitä tapahtuu, jos yrittää tehdä kaiken kerralla?**

* Virheet kasautuvat
* Et tiedä, mikä osa koodia rikki
* Motivaatio romahtaa
* Lopulta on helpompi aloittaa alusta

Perusversio on kuin talon perustukset  Jollei niitä ole, mikään muu ei pysy pystyssä.

---

## 🔧 Mikä ihmeen ”perusputki” (engl. *pipeline*)? → ohjelmointiprosessin selkäranka

**🎯 Lyhyt määritelmä**

*Perusputki tarkoittaa projektin perusvirtausta: syöte → käsittely → tuloste.*

Se on koko projektin ydintoiminnallisuus → Mitä ohjelman *minimissään* pitää pystyä tekemään, jotta kaikki muu voidaan rakentaa sen päälle.

---

### 🪠 Miksi puhutaan ”putkesta”?

Kuvittele oikea putki keittiössä tai kylpyhuoneessa:

* toisesta päästä tulee vettä (syöte)
* putki kuljettaa sen eteenpäin (käsittely)
* lopusta tulee se, mitä odotetaan (tuloste)

Jos putki vuotaa, on tukossa tai väärin rakennettu → koko järjestelmä kaatuu. Sama pätee ohjelmaan.

---

### 🧬 Miltä perusputki näyttää ohjelmoinnissa?

Tyypillinen pipeline pienessä projektissa (kuten meidän projektissa) on:

1. **Lue data jostain**

   * tiedosto
2. **Käsittele data**

   * pilko
   * muunna tietotyyppejä
   * laske
   * analysoi
3. **Tuota tulos**

   * tulosta konsoliin

---

**Yksinkertainen esitys:**

```
[ CSV-tiedosto ] --> [ luku ] --> [ muotoilu / ryhmittely ] --> [ tuloste ]
```

Jos nämä kolme toimivat, **putki toimii**.

---

### 🧱 Miksi perusputki on tärkeä?

Koska ilman sitä:

* et voi testata laskentaa
* et voi testata tyyppimuunnoksia
* et voi testata ryhmittelyä
* et tiedä, toimiiko ohjelma *yhtään*
* seuraavat vaiheet perustuvat arvailuun

Perusputki on ohjelman **perustukset**.

---

### ⚠️ Mitä tapahtuu, jos perusputkea ei tee ensin?

Aloitetaan samaan aikaan:

* datan luku
* tulostus
* laskenta
* virheenkäsittely
* ryhmittely
* muotoilut

→  **tuloksena on kaaos.**

---

Ilman perusputkea:

* virheitä tulee paljon
* virheet ovat vaikeita paikantaa
* et tiedä, mikä osa ohjelmaa toimii ja mikä ei
* motivaatio laskee, koska mikään ei tunnu onnistuvan
* koodista tulee sekava, kun sitä yrittää korjata ilman toimivaa perustaa

---

> [!TIP]  
> Perusputki on siis psykologinenkin työkalu: **se tuo onnistumisen tunteen ja varmistaa etenemisen (motivaatio säilyy)**.

---

### 🎯 Miltä perusputki näyttää konkreettisesti meidän projektissa?

Tässä projektissa (2025.csv → kuukausitasot)
**perusputki on yhtä kuin tämä:**

```
1. Lue tiedosto
2. Tulosta muutama rivi
```

Siis vain tämä. Ei laskentaa, ei ryhmittelyä, ei desimaalipilkkuja.

**Kun tämä toimii**, pipeline on käynnissä.
Sen jälkeen pipelinea laajennetaan:

```
3. Pilko sarakkeet
4. Muunna arvot numeroiksi
5. Laske summat
6. Tulosta kooste
```

> [!TIP]  
> Mutta nämä lisätään **yksi askel (muutos → testaus) kerrallaan**.

---

### 🏗️ Pipeline laajenee aina askel kerrallaan

Pipeline-ajattelun kauneus on siinä, että se on helppo testata:

* Onko tiedosto luettu?
  → Näen ensimmäiset rivit → OK.

* Toimiiko pilkkominen?
  → Tulostuu lista sarakkeista → OK.

* Toimiiko numeromuunnos?
  → print(type(arvo)) → float → OK.

---

> **💡 Jos jossain kohtaa tulee virhe, tiedät tasan tarkkaan missä kohtaa.**

---

## 5. 🔧 Laajennukset ja parannukset

**🔥 Kun perusversio toimii, laitetaan ohjelma oikeasti tekemään asioita**

Nyt lisätään askel kerrallaan:

* datan pilkkominen
* numeromuunnokset
* kuukausien laskeminen
* funktiot
* lopuksi siistit tulosteet

> [!TIP]  
> Tärkeää (edelleen): 👉 Lisää vain **yksi asia kerrallaan** 👉 Aja ohjelma jokaisen muutoksen jälkeen

---

**⚠️ Mitä tapahtuu, jos lisää liikaa kerralla?**

* Kymmenen virhettä yhtä aikaa
* Et tiedä mistä aloittaa
* Et tiedä mikä muutos rikkoi ohjelman
* Korjaamisesta tulee pelkkää arpapeliä 🎲

---

**🧠 Vertaus:**

> Auton korjaamisessa ei kannata vaihtaa kaikkea moottorista alustaan ja sähköihin samalla kertaa. → Korjataan yksi osa → testataan → jatketaan.  
> **JA MUISTA → Toimivaa ei tarvitse korjata!**

---

## 6. 🧪 Testaus ja viimeistely

**🤔 Toimiiko ohjelma oikeasti?**

Testauksessa kysytään:

* tuottaako ohjelma järkeviä tuloksia?
* kaatuuko se?
* onko tuloste selkeä?
* onko koodi luettavaa?

Testaus ei ole vain tekninen vaihe — se on tapa **ymmärtää oma ohjelma**.

---

**⚠️ Mitä tapahtuu, jos testauksen ohittaa?**

* Ohjelma näyttää toimivan… mutta antaa vääriä tuloksia
* Virheet tulevat esiin vasta käytössä

---

**🧠 Vertaus:**

> Testaamaton ohjelma on kuin ruokaa, jota et maista ennen tarjoilua. Jos suola unohtui → kaikki huomaavat.  
> **Demo-ilmiö on hyvin yleinen → Ja inhottava → Omalle työlle sokeutuu ja jokin oleellinen osa jää huomioimatta**

---

## 7. 📤 Palautus ja esittely

**🤝 Projektin viimeinen vaihe: tulosten jakaminen**

Kun ohjelma on:

* kirjoitettu
* testattu
* siivottu

**…on aika palauttaa se tai esittää se.**

---

Usein opintojakson yhteydessä palautukseen kuuluu :

* koodi
* kuvakaappaus tulosteesta
* lyhyt selitys (mitä ohjelma tekee)

> Tämä vaihe opettaa tärkeän taidon 👉 ohjelmoija ei vain tee koodia, vaan **osaa esitellä ja dokumentoida työnsä**

---

**⚠️ Mitä tapahtuu, jos palautus on huolimaton?**

Opintojaksolla:

* väärät tiedostot → tehtävä hylätty
* tulostetta ei mukana → pisteitä vähennetään
* koodi ei toimi → vaikeampi arvioida

> [!TIP]  
> **Ajatusleikki → Mitä oikeasti tapahtuu oikeassa ympäristössä?**

---

**🧠 Vertaus:**

> Projektin palautus on kuin tarjoilu ravintolassa: Ei riitä, että ruoka on hyvää → sen tulee olla myös **siististi esille laitettua**.

---

## 🎉 Lopuksi – Mitä tästä kaikesta pitäisi jäädä mieleen?

Ohjelmointiprojekti ei ole mysteeri tai sattuma. Se on **selkeä prosessi**, jossa jokainen vaihe vaikuttaa seuraavaan:

| Vaihe                 | Miksi tärkeä?       | Mitä jos oikaisee?                |
| --------------------- | ------------------- | --------------------------------- |
| Ongelman ymmärtäminen | Tiedät mitä teet    | Koodi ei ratkaise oikeaa ongelmaa |
| Suunnittelu           | Sinulla on kartta   | Eksyt matkalla                    |
| Ympäristön valmistelu | Työkalut toimivat   | Ohjelma ei käynnisty              |
| Perusversio           | Perusta kuntoon     | Seurauksena kaaos                 |
| Laajennukset          | Askel kerrallaan    | Virheet kertautuvat               |
| Testaus               | Varmistat toiminnan | Lopputulos on virheellinen        |
| Palautus              | Työ hyväksytään     | Arviointi vaikeutuu               |

🎯 *Kun nämä vaiheet ovat hallussa, pystyt tekemään minkä tahansa pienen Python-projektin.*

---