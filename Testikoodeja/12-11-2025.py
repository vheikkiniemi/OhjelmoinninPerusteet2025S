def ekafunktio():
    print("Tämä on eka funktio")

def tokafunktio(kurssi="", numero=0):
    #sana = "lisätään " + sana
    print(f"{kurssi} arvosana {numero}")
    print(kurssi, "arvosana", numero)
    print(kurssi, end=" ")
    print("arvosana", end=" ")
    print(numero)

def kolmasfunktio(etunimi="Mikko", sukunimi="Mallikas"):
    """Tämä palauttaa jotain"""
    return etunimi + " " + sukunimi

def neljasfunktio():
    return "ioij"

def leikkialistankanssa():
    teksti = "opiskelija;ohjelmoija;kehittäjä"
    #print(teksti.split(";")[0])
    sana = teksti.rsplit(";",1)
    print(sana)
    

def main():
    #print("lkj")
    #ekafunktio()
    #tokafunktio("Ohjelmoinnin perusteet", 5)
    #kolmannenpalautus = kolmasfunktio("Matti", "Meikäläinen")
    #print(kolmannenpalautus)
    #print(kolmasfunktio())
    #print(neljasfunktio())
    leikkialistankanssa()
    #print("jklkl" + str(12) + "ljkjlk")

if __name__ == "__main__":
    main()