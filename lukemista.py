# -*- coding: cp1252 -*-

# luetaan tiedostoon random_salasanoja.txt tallennettuja salasanoja
# hyv�ksyt��n (ep�loogisesti) ainoastaan salasanat jotka eiv�t sis�ll�
# erikoismerkkej�

tiedosto = open("random_salasanoja.txt", "r")
sisalto = tiedosto.readlines()

for i in sisalto:
    if i[:-1].isalnum():
        print(i, "kelpaa salasanaksi.")
    else:
        print(i, "sis�lt�� virheellisi� merkkej�.")
