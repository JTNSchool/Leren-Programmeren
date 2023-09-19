
# Voor het programma speelhaldag.py voor de 
# berekening van de 'Speelhal-dag’ van lab 1 voeg je een print statement toe. Stel dat het berekende bedrag is: 44.44 euro dan moet het volgende worden geprint in de terminal:
# ‘Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 44.44 euro’

# Alle getallen in de output moeten afkomstig zijn van de daarvoor gebruikte variabelen.


a = int(input("Welk antwoord wil je 1 of 2? "))

if a == 1:
    Crossantjes = 17
    CrossantjeKosten = 0.39
    Stokbroden = 2
    StokbrodenKosten = 2.78
    KostingsBonnen = 3
    Korting = 0.5
    antwoord = (Crossantjes * CrossantjeKosten) + (Stokbroden * StokbrodenKosten) - (KostingsBonnen * Korting)
    print(f"De feestlunch kost je bij de bakker {antwoord} euro voor de {Crossantjes} croissantjes en de {Stokbroden} stokbroden als de {KostingsBonnen} kortingsbonnen nog geldig zijn!")

else:
    personen = 4
    toegang = 7.45
    VIPVR = 0.37
    tijd = 45
    kosten = (personen * toegang) + (tijd / 5 * VIPVR * personen)
    print(f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {tijd} minuten VR kost je maar {kosten} euro")