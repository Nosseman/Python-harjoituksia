# -*- coding: cp1252 -*-
import math

luku1 = int(input("Anna ensimm�inen luku:"))
luku2 = int(input("Anna toinen luku:"))

while True:
    print("""(1) +
(2) -
(3) *
(4) /
(5)sin(luku1/luku2)
(6)cos(luku1/luku2)
(7)Vaihda luvut
(8)Lopeta
Valitut luvut:""", luku1, luku2)
    syote = input("Tee valinta (1-8):")

    if syote == "1":
        print("Tulos on:", int(luku1)+int(luku2))
    elif syote == "2":
        print("Tulos on:", int(luku1)-int(luku2))
    elif syote == "3":
        print("Tulos on:", int(luku1)*int(luku2))
    elif syote == "4":
        print("Tulos on:", int(luku1)/int(luku2))
    elif syote == "5":
        print("Tulos on:", math.sin(luku1/luku2))
    elif syote == "6":
        print("Tulos on:", math.cos(luku1/luku2))
    elif syote == "7":
        luku1 = int(input("Anna uusi ensimm�inen luku:"))
        luku2 = int(input("Anna uusi toinen luku:"))
    else:
        break
