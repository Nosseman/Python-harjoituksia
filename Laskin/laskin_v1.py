# -*- coding: cp1252 -*-

luku1 = input("Anna ensimmäinen luku:")
luku2 = input("Anna toinen luku:")

print("""
(1) +
(2) -
(3) *
(4) /
""")
syote = input("Tee valinta (1-4):")

if syote == "1":
	print("Tulos on:", int(luku1)+int(luku2))
elif syote == "2":
	print("Tulos on:", int(luku1)-int(luku2))
elif syote == "3":
	print("Tulos on:", int(luku1)*int(luku2))
elif syote == "4":
	print("Tulos on:", int(luku1)/int(luku2))
else:
	print("Valintaa ei tunnistettu.")
