# -*- coding: cp1252 -*-

import random
import string

# funktio joka kysyy käyttäjältä salasanan pituutta
# ja käytetäänkö erikoismerkkejä
# toisto päättyy vasta kun käyttäjä antaa kelvolliset syötteet
def kyselija():
    while True:
        pituus = input("Kuinka pitkä salasana luodaan? (8, 16, 32)")
        try:
            pituus = int(pituus)
            if pituus == 8 or pituus == 16 or pituus == 32:
                break
            else:
                print("Valitse pituus uudelleen")
        # varaudutaan epäkelpoihin syötteisiin
        except ValueError:
            print("Et antanut lukua")

    while True:    
        merkit = input("Sisällytetäänkö erikoismerkit? (Kyllä tai Ei)")
        try:
            if merkit == "Kyllä" or  merkit == "Ei":
                break
            else:
                print("Valitse Kyllä tai Ei")
        # varaudutaan epäkelpoihin syötteisiin
        except ValueError:
            print("Virheellinen syöte")

    # palautetaan syötteiden arvot
    return pituus, merkit


def generoi(kuinkaPitka, erikoisMerkit):

    # mikäli käyttäjä haluaa sisällyttää erikoismerkit
    if erikoisMerkit == "Kyllä":
        char = string.ascii_uppercase + \
             string.ascii_lowercase + string.digits + string.punctuation
        sala = "".join(random.choice( char ) for x in range(kuinkaPitka))
    # jos ei haluta erikoismerkkejä
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

    
