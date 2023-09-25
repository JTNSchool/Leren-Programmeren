# De kandidaat moet ook nog voldoen aan de volgende criteria:

# # In bezit van een Diploma MBO-4 ondernemen OF
# # Is al meer dan 3 jaar ondernemer EN met minimaal 5 werknemers in loondienst.
# # Is man EN heeft snor breder dan 10 cm OF
# # is vrouw EN draagt rood krulhaar langer dan 20 cm OF
# # is anders EN heeft brede glimlach breder dan 10 cm

# # Let op: Het programma wil geen enkele kandidaat beledigen. 
# Het programma mag daarom alleen een man vragen naar zijn snor en snorlengte 
# en mag alleen een vrouw vragen naar haar haar en haarlengte en mag anders (geen man of vrouw) alleen vragen naar de breedte van de glimlach!
# Let op: De vragen met getallen mogen de kritieke grens (zoals bijvoorbeeld 3 jaar of 20 cm) van een criterium niet verklappen.

# Let op: Eerst de relevante vragen stellen, daarna pas de geschiktheid berekenen op basis van de gegeven antwoorden! 
# Pas na het berekenen van de geschiktheid geeft u de uitslag van de sollicitatie aan de invuller.

# Waarom afgewezen?
# Zorg dat het programma na afwijzing een lijst print met alle criteria onder elkaar waaraan niet is voldaan. 
# Houdt dus bij (in een variabele) of een criteria wel of niet is voldaan. 
# Bijvoorbeeld voor het criterium: “heeft als schoenmaat van de linkervoet minimaal 45” zou je kunnen programmeren:

# Gebruik zeker de volgende technieken:

from termcolor import colored

Jalist = ["ja", "yes", "j", "y"]

def checkint(txt):
    try:
        return int(txt)
    except ValueError:
        print(colored(f"Kan {txt} niet omzetten naar integer! er word 0 ingevoerd", "red"))
        return 0

print(colored("-----{Circusdirecteur voor Circus HotelDeBotel}-----", "red"))
print()

diploma = input(colored("Heeft u een Diploma MBO-4 ondernemen? ", "blue")).lower()
ondernemer = input(colored("bent u een ondernemer? ", "yellow")).lower()
if ondernemer in Jalist:
    ondernemer_tijd = input(colored("Hoe lang onderneemt u al? ", "yellow"))
    ondernemer_aantal = input(colored("Hoeveel mensen heeft u in dienst? ", "yellow"))

rijbewijs = input(colored("Heeft u een vrachtwagen rijbewijs? ", "green")).lower()
hoed = input(colored("Heeft u een Hoge hoed? ", "blue")).lower()
gewicht = checkint(input(colored("Hoe zwaar bent u in kg? ", "yellow")))
lengte = checkint(input(colored("Hoe lang bent u in hele centimeters? ", "green")))
certificaat = input(colored("heeft u het certificaat Overleven met gevaarlijk personeel? ", "red")).lower()
ervaring1 = checkint(input(colored("Hoeveel jaar ervaring heeft u met dieren-dresuur? ", "blue")))
ervaring2 = checkint(input(colored("Hoeveel jaar ervaring heeft u met jongleren? ", "green")))
ervaring3 = checkint(input(colored("Hoeveel jaar ervaring heeft u met acrobatiek? ", "red")))
print()

afgewezenlijst = []
aangenomenpunten = 0

if (diploma not in Jalist) and (ondernemer not in Jalist) or (ondernemer_tijd < 3) or (ondernemer_aantal < 5):
    if (diploma not in Jalist) and (ondernemer not in Jalist):
        afgewezenlijst.append("U heeft geen diploma of u bent geen werknemer.")
    if (ondernemer in Jalist) and (ondernemer_tijd < 3):
        afgewezenlijst.append("U heeft minder dan 3 jaar ervaring als ondernemer.")
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
if (ervaring1 < 4 or ervaring2 < 5 or ervaring3 < 3):
    afgewezenlijst.append("U heeft te weinig ervaring.")
    aangenomenpunten += 1

if aangenomenpunten >= 1:
    print(colored("Helaas je bent niet aangenomen!", "red"))
    for reason in afgewezenlijst:
        print(reason)

if aangenomenpunten == 0:
    print(colored("Gefeliciteerd je bent aangenomen!"), "green")
