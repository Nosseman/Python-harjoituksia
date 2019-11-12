# -*- coding: cp1252 -*-

class Emo:
    arvo = 0
    tila = "Toiminnassa"

    def nimi(self):
        print("Minä olen emoluokka.")

class Lapsi(Emo):

    def nimi(self):
        print("Minä olen lapsiluokka.")

def main():

    vanhempi = Emo()
    skidi = Lapsi()

    print(vanhempi.tila)
    vanhempi.nimi()
    print(skidi.tila)
    skidi.nimi()
    
if __name__ == "__main__":
    main()
