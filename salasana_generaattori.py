# -*- coding: cp1252 -*-

import random
import string

# funktio joka kysyy k�ytt�j�lt� salasanan pituutta
# ja k�ytet��nk� erikoismerkkej�
# toisto p��ttyy vasta kun k�ytt�j� antaa kelvolliset sy�tteet
def kyselija():
    while True:
        pituus = input("Kuinka pitk� salasana luodaan? (8, 16, 32)")
        try:
            pituus = int(pituus)
            if pituus == 8 or pituus == 16 or pituus == 32:
                break
            else:
                print("Valitse pituus uudelleen")
        # varaudutaan ep�kelpoihin sy�tteisiin
        except ValueError:
            print("Et antanut lukua")

    while True:    
        merkit = input("Sis�llytet��nk� erikoismerkit? (Kyll� tai Ei)")
        try:
            if merkit == "Kyll�" or  merkit == "Ei":
                break
            else:
                print("Valitse Kyll� tai Ei")
        # varaudutaan ep�kelpoihin sy�tteisiin
        except ValueError:
            print("Virheellinen sy�te")

    # palautetaan sy�tteiden arvot
    return pituus, merkit


def generoi(kuinkaPitka, erikoisMerkit):

    # mik�li k�ytt�j� haluaa sis�llytt�� erikoismerkit
    if erikoisMerkit == "Kyll�":
        char = string.ascii_uppercase + \
             string.ascii_lowercase + string.digits + string.punctuation
        sala = "".join(random.choice( char ) for x in range(kuinkaPitka))
    # jos ei haluta erikoismerkkej�
    else:
        char = string.ascii_uppercase + \
             string.ascii_lowercase + string.digits
        sala = "".join(random.choice( char ) for x in range(kuinkaPitka))

    return sala


def main():
    pitka, erikois = kyselija()
    
    salaSana = generoi(pitka, erikois)
    print("Generoitu salasana:", salaSana)


if __name__ == "__main__":
    main()

    
