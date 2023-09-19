# de klant kan een keuze maken uit 3 afmetingen pizza's,
# namelijk: small, medium en large. Voor elke afmeting wordt er gevraagd hoeveel pizza's de klant wil.
# zoek op internet naar passende prijzen voor deze pizza afmetingen en noteer deze prijzen in je applicatie
# Toon op het scherm met goede omschrijving het aantal bestelde pizza's voor elke afmeting en berekenen per afmeting de prijs uit
# Toon op het scherm de totaalprijs van alle pizza's.
# Bovenaan in de Python file noteer je als commenteer het volgende: voornaam, achternaam en opdracht: Pizza calculator
# De volgende zaken dienen ook op orde te zijn:

# leesbare layout van de code
# naamgeving is duidelijk en 'self explaining'
# er is passend commentaar toegevoegd in de code
# laat de uitkomst er uit zien als een bonnetje
 
# Test het programma grondig. Maak daarvan screenshots.
# Commmit en push pizzaCalculator.py
# Lever hier het programma + screenshot in.

#Prijzen
prijzen = {
    "small": 7.49,
    "medium": 9.49,
    "large": 14.49
}

#inputs
small = int(input("Hoeveel pizza Small will je? "))
medium = int(input("Hoeveel pizza Medium will je? "))
large = int(input("Hoeveel pizza Large will je? "))

#Berekeningen
smallTotaal = small * prijzen["small"]
mediumTotaal = small * prijzen["medium"]
largeTotaal = small * prijzen["large"]
totaal = smallTotaal + mediumTotaal + largeTotaal

#Bonnetje

print("--------------------------------------------------")
print()
print(f"Small: {small} * €{prijzen['small']} = €{smallTotaal}")
print(f"medium: {medium} * €{prijzen['medium']} = €{mediumTotaal}")
print(f"large: {large} * €{prijzen['large']} = €{largeTotaal}")
print(f"Totaal: {small + medium + large} Pizzas =  €{totaal}")
print()
print("--------------------------------------------------")

