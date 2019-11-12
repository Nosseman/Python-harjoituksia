# -*- coding: cp1252 -*-

# luetaan tiedostoon random_salasanoja.txt tallennettuja salasanoja
# hyväksytään (epäloogisesti) ainoastaan salasanat jotka eivät sisällä
# erikoismerkkejä

tiedosto = open("random_salasanoja.txt", "r")
sisalto = tiedosto.readlines()

for i in sisalto:
    if i[:-1].isalnum():
        print(i, "kelpaa salasanaksi.")
    else:
        print(i, "sisältää virheellisiä merkkejä.")
