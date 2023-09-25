# Maak van de gasten variable in plaats van een boolean een integer. Aan de hand van wat je aan het testen bent pas je steeds de code aan.

# Breid nu je programma uit (dus niet een nieuw bestand) dat het ook nog werkt met de volgende stellingen:

# Een feest met gasten kan pas beginnen als er minimaal 4 gasten zijn.
# Een feest kan niet starten als er meer dan 20 aanwezigen zijn.
# Let op: Zorg er voor dat de punten uit de vorige opdracht ook werken, als je 0 gasten hebt betekend dit dat er geen gasten zijn. 
# Je mag geen nieuwe if’s aanmaken!

# Commit en push je programma naar github en lever een screenshot van je code in.

gastheer = input("Wie is de gastheer? ").lower()
allowed = ["jacco", "bouman", "wilfred"]
gasten = int(input("Hoeveel gasten zijn er? "))
drank = True
chips = False

if ((gasten >= 4 and gasten <= 20) or gastheer in allowed) and (gastheer in allowed and drank == True) or (gasten >= 4 and gasten <= 20) and (chips == True and drank == True):
    print('Start the Party')
else:
    print('No Party')
