> [!NOTE]
> Materiaali on luotu ChatGPT:n ja Copilotin avulla.

# 🐍  Varausrivin käsittely tiedostosta

## 🎯 Tavoite

Tehtävän tavoitteena on harjoitella:

* merkkijonojen (`str`) käsittelyä ja pilkkomista
* erilaisten tietotyyppien (`int`, `float`, `bool`, `datetime`) käyttöä
* tietotyyppien välisiä muunnoksia
* tietojen jäsenneltyä tulostamista

> [!NOTE]
> Halutessa työn voi tehdä **`pareittain (max. kaksi)`**. Tällöin kohdassa [Palautusohje Itslearningiin](#-palautusohje-itslearningiin) pari tekee vain yhden palautuksen, johon on yhdistetty molemmat.

---

## 📄 Kuvaus

Sinulle on annettu tekstitiedosto **`varaukset.txt`**, jossa oleva rivi sisältää yhden varauksen tiedot.
Lisäksi sinulle on annettu Python-skripti **`lue_varaukset.py`**, joka lukee tiedostossa **`varaukset.txt`** olevat varaukset.
Tietoja on eroteltu pystypalkilla `|`.

> [!TIP]
> Tämä tapa rakentaa tietoa on hyvin yleinen ja näissä Python on loistava!

**Esimerkkirivi:**

```
123|Anna Virtanen|2025-10-31|10:00|2|19.95|True|Kokoustila A|0401234567|anna.virtanen@example.com
```

Rivillä on seuraavat tiedot:

| Sarake | Selite         | Tietotyyppi                 |
| ------ | -------------- | --------------------------- |
| 1      | Varausnumero   | `int`                       |
| 2      | Varaajan nimi  | `str`                       |
| 3      | Varauspäivä    | `datetime`                  |
| 4      | Aloitusaika    | `datetime.time`             |
| 5      | Tuntimäärä     | `int`                       |
| 6      | Tuntihinta (€) | `float`                     |
| 7      | Maksettu       | `bool`                      |
| 8      | Varauskohde    | `str`                       |
| 9      | Puhelinnumero  | `str`                       |
| 10     | Sähköposti     | `str`                       |

---

## 🧠 Tehtäväohjeet

1. Kopioi tiedosto nimeltä **`varaukset.txt`** omaan `Git repoosi` ja kansioon `Viikko2`.
2. Kopioi Python-skripti nimeltä **`lue_varaukset.py`** omaan `Git repoosi` ja kansioon `Viikko2`.
3. Muokkaa skriptiä niin, että se tekee suoritettaessa seuraavaan tulosteen:

```
Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 2025-10-31
Aloitusaika: 10:00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com
```

---

### 🧩 Vihjeitä

* Pilko rivi `split('|')`-metodilla → tuottaa listatyyppisen muuttujan
* Muunna tietotyypit. Seuraavassa muutama esimerkki:

  ```python
  varausnumero = int(varaus[0])
  tuntihinta = float(varaus[5])
  maksettu = varaus[6].strip() == "True"
  ```
* Päivämäärän ja aloitusajan voi muuntaa `datetime`-muotoon:

  ```python
  from datetime import datetime
  paiva = datetime.strptime(varaus[2], "%Y-%m-%d").date()
  aika = datetime.strptime(varaus[3], "%H:%M").time()
  ```

> [!TIP]
> Miksi tämä on tärkeää, vaikka voitaisiin käyttää pelkkää tekstiä?
> KOSKA `datetime` ei tunne päivämäärää 2025-10-32 ja nostaa muunnoksissa virheen!
> Näin pidetään tieto eheänä ja oikeana!

* Laske kokonaishinta kertomalla tuntimäärä ja tuntihinta.
* Jos haluat tulostaa "Kyllä" tai "Ei" maksettu-tiedon perusteella, voit käyttää ehtolauseketta seuraavasti:

  ```python
  print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")
  ```

---

## 🚀 Bonustehtävää (valinnaisia)

💎 **A)** Muuta tiedoston `varaukset.txt` sisältöä ja testaa, että tulostus on oikea
💎 **B)** Tulosta tuntimäärän perusteella varauksen lopppumisaika
💎 **C)** Lisää tiedostoon `varaukset.txt` useampi varaus ja tulosta kaikki rivit tiedostosta.
💎 **D)** Laske kaikkien varausten yhteishinta.
💎 **E)** Tulosta vain ne varaukset, joita ei ole vielä maksettu.
💎 **F)** Tulosta vain ne varaukset, jotka alkavat klo 8–12 välillä.

---

## 📤 Palautusohje Itslearningiin

Palauta **linkki GitHub-repoon** ja **kuvankaappaus konsolista**, jossa näkyy ohjelman suoritus ja tulostus.

Lisää palautukseen myös lyhyt teksti:
> Mitä jäi päällimmäisenä tehtävästä mieleen?

---

## 💬 Hyvä fiilis tekemiseen!

**Muista:** kaikki ohjelmoijat aloittavat jostain.
Tärkeintä ei ole täydellinen koodi, vaan **oppiminen, kokeilu ja oivallus**.
Pidä hauskaa ja tutki, miten ihan oikeita asioita ihan oikeasti tehdään! 🚀💡😎

---

## 💡 Yleisimmät virheet ja ratkaisut

| Virhe | Syy | Ratkaisu |
|-------|-----|----------|
| “Tiedostoa ei löydy” | Skriptiä ajetaan väärässä kansiossa | Siirry kansioon jossa skripti on |
| “Tiedostoa ei löydy” | Tiedostoja ei ole kopioitu | Kopioi tiedostot kansioosi |
| “Tiedostoa ei löydy” | Tiedostot on nimetty väärin | Varmista tiedostojen nimien oikeellisuus |