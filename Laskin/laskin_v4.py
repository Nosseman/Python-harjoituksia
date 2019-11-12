# -*- coding: cp1252 -*-
import math

def kyselija():
    while True:
        kysy1 = input("Anna luku:")
        try:
            luku1 = int(kysy1)
            break
        except ValueError:
            print("Virheellinen syöte!")

    while True:            
        kysy2 = input("Anna luku:")
        try:
            luku2 = int(kysy2)
            break
        except ValueError:
            print("Virheellinen syöte!")

    return luku1, luku2

def main():

    luku1, luku2 = kyselija()

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
        valinta = input("Tee valinta (1-8):")

        try:
            syote = int(valinta)
        except ValueError:
            print("Virheellinen syöte!")

        if syote == 1:
            print("Tulos on:", int(luku1)+int(luku2))
        elif syote == 2:
            print("Tulos on:", int(luku1)-int(luku2))
        elif syote == 3:
            print("Tulos on:", int(luku1)*int(luku2))
        elif syote == 4:
            print("Tulos on:", int(luku1)/int(luku2))
        elif syote == 5:
            print("Tulos on:", math.sin(luku1/luku2))
        elif syote == 6:
            print("Tulos on:", math.cos(luku1/luku2))
        elif syote == 7:
            luku1, luku2 = kyselija()
        else:
            break

if __name__ == "__main__":
    main()
