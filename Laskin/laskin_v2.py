# -*- coding: cp1252 -*-

luku1 = int(input("Anna ensimmäinen luku:"))
luku2 = int(input("Anna toinen luku:"))

jatko = True

while jatko:
    print("""(1) +
(2) -
(3) *
(4) /
(5)Vaihda luvut
(6)Lopeta
Valitut luvut:""", luku1, luku2)
    syote = input("Tee valinta (1-6):")

    if syote == "1":
        print("Tulos on:", int(luku1)+int(luku2))
    elif syote == "2":
        print("Tulos on:", int(luku1)-int(luku2))
    elif syote == "3":
        print("Tulos on:", int(luku1)*int(luku2))
    elif syote == "4":
        print("Tulos on:", int(luku1)/int(luku2))
    elif syote == "5":
        luku1 = int(input("Anna uusi ensimmäinen luku:"))
        luku2 = int(input("Anna uusi toinen luku:"))
    else:
        jatko = False
