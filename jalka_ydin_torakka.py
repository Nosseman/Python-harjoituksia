# -*- coding: cp1252 -*-

import random

def ratkaise(syote_p, luku):    
    if ((syote_p == "Jalka") and (luku == 1)) or\
       ((syote_p == "Ydinase") and (luku == 2)) or\
       ((syote_p == "Torakka") and (luku == 3)):
        print("Tasapeli!")
        return 1
    elif ((syote_p == "Jalka") and (luku == 3)) or\
       ((syote_p == "Torakka") and (luku == 2)) or\
       ((syote_p == "Ydinase") and (luku == 1)):
        print("Voitit!")
        return 2
    else:
        print("Hävisit!")
        return 0

def main():
    kierros = 0
    pisteet = 0
    tasapeli = 0
    
    while True:
        syote = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa):")
        if syote == "Lopeta":
            print("Pelasit", kierros, "kierrosta, joista voitit", pisteet, "ja pelasit tasan", tasapeli, "peliä.")
            break
        else:
            print("Sinä valitsit:", syote)
            kone = random.randint(1,3)
            if kone == 1:
                print("tietokone valitsi: Jalka")
            elif kone == 2:
                print("tietokone valitsi: Ydinase")
            else:
                print("tietokone valitsi: Torakka")

        kierros += 1
        tulos = ratkaise(syote, kone)
        if tulos == 0:
            continue
        elif tulos == 1:
            tasapeli += 1
        else:
            pisteet += 1
     
if __name__ == "__main__":
    main()
