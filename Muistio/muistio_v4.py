# -*- coding: cp1252 -*-

import time

def avaaOletus(nimi):
    try:
        tiedosto = open(nimi, "r")
# jos tiedosto ei olemassa, luodaan se
    except IOError:
        print("Oletusmuistioa ei l�ydy, luodaan tiedosto.")
        tiedosto = open(nimi, "w")
        
    tiedosto.close()
	
def avaaTiedosto(syote):
    try:
        tiedosto = open(syote, "r")
# jos tiedosto ei olemassa, luodaan se
    except IOError:
        print("Tiedostoa ei l�ydy, luodaan tiedosto.")
        tiedosto = open(syote, "w")
        
    tiedosto.close()

# tehd��n looppi jota toistetaan
def main():
# annetaan oletustiedoston nimi
    muistio = "muistio.txt"

    avaaOletus(muistio)

    while True:
        print("""
K�ytet��n muistiota:""", muistio, """
(1) Lue muistikirjaa
(2) Lis�� merkint�
(3) Tyhjenn� muistikirja
(4) Vaihda muistiota
(5) Lopeta
""")
# kysyt��n k�ytt�j�lt� toimea
        syote = input("Mit� haluat tehd�?:")
        if syote == "1":
            # luetaan tiedoston sis�lt�
            tiedosto = open(muistio, "r")
            sisalto = tiedosto.read()
            print(sisalto)
            tiedosto.close()
        elif syote == "2":
            # jatketaan kirjoittamista tiedoston lopusta
            tiedosto = open(muistio, "a")
            teksti = input("Kirjoita uusi merkint�:")
            tiedosto.write(teksti + (":::" + time.strftime("%X %x") + "\n"))
            tiedosto.close()
        elif syote == "3":
            # ylikirjoitetaan tiedostoon
            tiedosto = open(muistio, "w")
            teksti = ""
            tiedosto.write(teksti)
            tiedosto.close()
            print("Muistio tyhjennetty.")
        elif syote == "4":
            muistio = input("Anna tiedoston nimi:")
            avaaTiedosto(muistio)
        elif syote == "5":
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta.")

if __name__ == "__main__":
    main()
