# -*- coding: cp1252 -*-

nimi = input("Mink�niminen tiedosto luodaan?:")

tiedosto = open(nimi, "w")
teksti = input("Mit� kirjoitetaan tiedostoon?:")
tiedosto.write(teksti)
tiedosto.close()
print("Luotiin tiedosto", nimi, "ja siihen tallennettiin teksti:", teksti)
