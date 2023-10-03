from termcolor import colored

Jalist = ["ja", "yes", "j", "y"]
afgewezenlijst = []
def checkint(txt):
    try:
        return int(txt)
    except ValueError:
        print(colored(f"Kan {txt} niet omzetten naar integer! er word 0 ingevoerd", "red"))
        return 0

print(colored("-----{Circusdirecteur voor Circus HotelDeBotel}-----", "yellow"))
print()

diploma = input(colored("Heeft u een Diploma MBO-4 ondernemen? ", "yellow")).lower()
ondernemer = input(colored("bent u een ondernemer? ", "yellow")).lower()
if ondernemer in Jalist:
    ondernemer_tijd = checkint(input(colored("Hoe lang onderneemt u al? ", "yellow")))
    ondernemer_aantal = checkint(input(colored("Hoeveel mensen heeft u in dienst? ", "yellow")))
else:
    ondernemer_tijd = 0
    ondernemer_aantal = 0
geslacht = input(colored("wat voor geslacht bent u? ", "yellow")).lower()
if geslacht == "man":
    Heeftsnor = input(colored("Heeft u een snor? ", "yellow"))
    if Heeftsnor in Jalist:
        SnorLengte = checkint(input(colored("Hoelang is uw snor? ", "yellow")))
    glimlach = 0
elif geslacht == "vrouw":
    haarlengte = 0
    Heeftroodhaar = input(colored("Heeft u rood haar? ", "yellow")).lower()
    if Heeftroodhaar in Jalist:
        haarlengte = checkint(input(colored("hoelang is uw haar? ", "yellow")))
    else:
        afgewezenlijst.append("Haarkleur voldoet niet")
    glimlach = 0
else:
    glimlach = checkint(input(colored("hoe groot is uw glimlach? ", "yellow")))
rijbewijs = input(colored("Heeft u een vrachtwagen rijbewijs? ", "yellow")).lower()
hoed = input(colored("Heeft u een Hoge hoed? ", "yellow")).lower()
gewicht = checkint(input(colored("Hoe zwaar bent u in kg? ", "yellow")))
lengte = checkint(input(colored("Hoe lang bent u in hele centimeters? ", "yellow")))
certificaat = input(colored("heeft u het certificaat Overleven met gevaarlijk personeel? ", "yellow")).lower()
ervaring1 = checkint(input(colored("Hoeveel jaar ervaring heeft u met dieren-dresuur? ", "yellow")))
ervaring2 = checkint(input(colored("Hoeveel jaar ervaring heeft u met jongleren? ", "yellow")))
ervaring3 = checkint(input(colored("Hoeveel jaar ervaring heeft u met acrobatiek? ", "yellow")))
print()

aangenomenpunten = 0

if (diploma not in Jalist) and (ondernemer not in Jalist) or (ondernemer_tijd < 3) or (ondernemer_aantal < 5) and (geslacht in Jalist and Heeftsnor in Jalist and SnorLengte >= 10) or (geslacht not in Jalist and (haarlengte >= 20 or glimlach >= 10)):
    if (diploma not in Jalist) and (ondernemer not in Jalist):
        aangenomenpunten += 1
        afgewezenlijst.append("U heeft geen diploma of u bent geen werknemer.")
    if (ondernemer in Jalist) and (ondernemer_tijd < 3):
        aangenomenpunten += 1
        afgewezenlijst.append("U heeft minder dan 3 jaar ervaring als ondernemer.")
    if (geslacht == "man") and (SnorLengte < 10):
        aangenomenpunten += 1
        afgewezenlijst.append("U heeft een tekleine snor.")
    if (geslacht == "vrouw") and (haarlengte < 20):
        aangenomenpunten += 1
        afgewezenlijst.append("U heeft te kort haar.")
    if (geslacht != "vrouw" and geslacht != "man") and glimlach < 10:
        aangenomenpunten += 1
        afgewezenlijst.append("Tekleine glimlach")
    if (ondernemer in Jalist) and (ondernemer_aantal < 5):
        afgewezenlijst.append("U heeft minder dan 5 werknemers in dienst.")
        aangenomenpunten += 1

if (rijbewijs not in Jalist):
    afgewezenlijst.append("U heeft geen vrachtwagen rijbewijs.")
    aangenomenpunten += 1
if (hoed not in Jalist):
    afgewezenlijst.append("U heeft geen hoge hoed.")
    aangenomenpunten += 1
if (gewicht < 90 or gewicht > 120):
    afgewezenlijst.append("U bent te licht of te zwaar.")
    aangenomenpunten += 1
if lengte < 150 or lengte > 220:
    afgewezenlijst.append("U bent te klein of te groot.")
    aangenomenpunten += 1
if ervaring1 < 4 and ervaring2 < 5 and ervaring3 < 3:
    afgewezenlijst.append("U heeft te weinig ervaring.")
    aangenomenpunten += 1

if aangenomenpunten >= 1:
    print(colored("Helaas je bent niet aangenomen!", "red"))
    for reason in afgewezenlijst:
        print(reason)

if aangenomenpunten == 0:
    print(colored("Gefeliciteerd je bent aangenomen!", "green"))
