#lets build a robot barista
from unicodedata import name


print("****************************************")
print("Hallo, Welkom dit is een coffee robot!!")
print("****************************************")
naam = input("Wat is je naam?\n")

if naam == "Ruben":
    kwaad_status = input("Ben je kwaad?\n")
    if kwaad_status == "Ja":
        print("Je bent niet welkom hier!! Ga weg!")
        exit()
    else:
        print("Oh dus jij bent niet kwaad, mooizo")
else:
    print("Hallo " + naam + ", Dankjewel voor het langkomen! :)")

menu = "Zwarte koffie, Cappucino, Latte, Espresso, Frappuccino"

print(naam + " wat zou je graag willen bestellen van het menu?\n" + menu)

bestelling = input()

prijs = 10

if bestelling == "Zwarte koffie":
    prijs = 3
elif bestelling == "Cappucino":
    prijs = 10
elif bestelling == "Latte":
    prijs = 9
elif bestelling == "Espresso":
    prijs = 5
elif bestelling == "Frappuccino":
    prijs = 13
else:
    print("Sorry dat hebben we niet.")

hoeveelheid = input("Hoeveel koffie wil je bestellen?\n")


totaal = prijs * int(hoeveelheid)

print("Dankjewel voor je betselling! Het totaal is: €" + str(totaal))

print("Klinkt goed! " + naam + ", je bestelling is: " + bestelling + " " + hoeveelheid + "X, deze wordt zo bereid")


