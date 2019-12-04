# -*- coding: cp1252 -*-

import time
import pickle

nimi = "muistio.dat"
# yritet��n avata tiedosto
try:
    tiedosto = open(nimi, "rb")
    luettu = pickle.load(tiedosto)
except EOFError:
    luettu = []
# jos tiedosto ei olemassa, luodaan se
except IOError:
    print("Virhe tiedostossa, luodaan uusi", nimi, ".")
    tiedosto = open(nimi, "wb")
    luettu = []
else:
    tiedosto.close()

# toistettava silmukka
while True:
    print("""
(1) Lue muistikirjaa
(2) Lis�� merkint�
(3) Muokkaa merkint��
(4) Poista merkint�
(5) Tallenna ja lopeta

""")
    # kysyt��n k�ytt�j�lt� toimea
    syote = input("Mit� haluat tehd�?:")
    if syote == "1":
        for i in luettu:
            print(i)
    elif syote == "2":
        teksti = input("Kirjoita uusi merkint�:")
        luettu.append((teksti + (":::" + time.strftime("%X %x"))))
    elif syote == "3":
        # lasketaan alkioiden m��r�
        print("Listalla on", len(luettu), "merkint��.")
        valinta = int(input("Mit� niist� muutetaan?:")) -1
        if valinta < 0 or valinta > len(luettu):
            print("Virheellinen valinta")
        else:
            print(luettu[valinta])
            luettu.pop(valinta)
            uusiMerkinta = (input("Anna uusi teksti:") + (":::" + time.strftime("%X %x")))
            luettu.insert(valinta, uusiMerkinta)
    elif syote == "4":
        print("Listalla on", len(luettu), "merkint��.")
        valinta = int(input("Mit� niist� poistetaan?:")) -1
        if valinta < 0 or valinta > len(luettu):
            print("Virheellinen valinta")
        else:
            poistettu = luettu.pop(valinta)
            print("Poistettiin merkint�", poistettu)
    elif syote == "5":
        tiedosto = open(nimi, "wb")
        pickle.dump(luettu, tiedosto)
        tiedosto.close()
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta.")

			
