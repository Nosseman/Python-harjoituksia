# -*- coding: cp1252 -*-

jatka = True

while jatka:
    print("""
(1) Lue muistikirjaa
(2) Lis�� merkint�
(3) Tyhjenn� muistikirja
(4) Lopeta
""")
    syote = input("Mit� haluat tehd�?:")
    if syote == "1":
        tiedosto = open("muistio.txt", "r")
        sisalto = tiedosto.read()
        print(sisalto)
        tiedosto.close()
    elif syote == "2":
        tiedosto = open("muistio.txt", "a")
        teksti = input("Kirjoita uusi merkint�:")
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
