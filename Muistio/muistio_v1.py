# -*- coding: cp1252 -*-

nimi = input("Minkäniminen tiedosto luodaan?:")

tiedosto = open(nimi, "w")
teksti = input("Mitä kirjoitetaan tiedostoon?:")
tiedosto.write(teksti)
tiedosto.close()
print("Luotiin tiedosto", nimi, "ja siihen tallennettiin teksti:", teksti)
