# -*- coding: cp1252 -*-

jatka = True

while jatka:
    print("""
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
""")
    syote = input("Mitä haluat tehdä?:")
    if syote == "1":
        tiedosto = open("muistio.txt", "r")
        sisalto = tiedosto.read()
        print(sisalto)
        tiedosto.close()
    elif syote == "2":
        tiedosto = open("muistio.txt", "a")
        teksti = input("Kirjoita uusi merkintä:")
        tiedosto.write(teksti + "\n")
        tiedosto.close()
    elif syote == "3":
        tiedosto = open("muistio.txt", "w")
        teksti = ""
        tiedosto.write(teksti)
        tiedosto.close()
        print("Muistio tyhjennetty.")
    elif syote == "4":
        jatka = False
        print("Lopetetaan.")
    else:
        print("Tuntematon valinta.")
