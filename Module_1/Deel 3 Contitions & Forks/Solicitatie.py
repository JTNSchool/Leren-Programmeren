# Vacature: Circusdirecteur voor Circus HotelDeBotel
# Bepaal met behulp van een aantal vragen in jouw sollicitatie.py of de kandidaat mag gaan solliciteren naar de functie.
# Stel eerst alle vragen en ga daarna pas beoordelen aan de hand van de gegeven antwoorden of de kandidaat mag solliciteren.

# De kandidaat moet wel voldoen aan de volgende criteria:
# In bezit van een geldig Vrachtwagen rijbewijs. Een echte circusdirecteur rijdt ook de grootste circuswagen zelf!
# In bezit van een hoge hoed.
# Is zwaarder dan 90 kg en lichter dan 120 kg
# Is langer dan 150 cm en korter dan 220 cm
# Heeft Certificaat “Overleven met gevaarlijk personeel”
# Heeft:
# minimaal 4 jaar praktijkervaring met dieren-dressuur OF
# minimaal 5 jaar ervaring met jongleren OF
# minimaal 3 jaar praktijkervaring met acrobatiek.

from termcolor import colored

def checkint(txt):
    try:
        return int(txt)
    except ValueError:
        return 0


print(colored("-----{Circusdirecteur voor Circus HotelDeBotel}-----", "red"))
print()
rijbewijs = input(colored("Heeft u een vrachtwagen rijbewijs? ", "green")).lower()
hoed = input(colored("Heeft u een Hoge hoed? ", "blue")).lower()
gewicht = checkint(input(colored("Hoe zwaar bent u in kg? ", "yellow")))
lengte = checkint(input(colored("Hoe lang bent u in hele centimeters? ", "green")))
certificaat = input(colored("heeft u het certificaat Overleven met gevaarlijk personeel? ", "red")).lower()
ervaring1 = checkint(input(colored("Hoeveel jaar ervaring heeft u met dieren-dresuur? ", "blue")))
ervaring2 = checkint(input(colored("Hoeveel jaar ervaring heeft u met jongleren? ", "green")))
ervaring3 = checkint(input(colored("Hoeveel jaar ervaring heeft u met acrobatiek? ", "red")))
print()
Jalist = ["ja", "yes", "j", "y"]
if (rijbewijs in Jalist) and (hoed in Jalist) and (gewicht >= 90 and gewicht <= 120) and (lengte >= 150 and lengte <= 220) and (ervaring1 >= 4 or ervaring2 >= 5 or ervaring3 >= 3):
    print(colored("Gefeliciteerd je bent aangenomen!"), "green")
else:
    print(colored("Helaas je bent niet aangenomen!"), "red")
