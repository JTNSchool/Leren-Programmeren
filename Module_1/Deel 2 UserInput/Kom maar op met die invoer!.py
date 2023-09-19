# Het werk van een programmeur is nooit echt af.

# Pas feestlunch.py en speelhaldag.py van het vorige leerpad aan om input te accepteren

# Programmeer de invoer van de waarden (via input) van alle variabelen in feestlunch.py
# Programmeer de invoer van de waarden (via input) van alle variabelen in speelhaldag.py
# Zorg voor conversies naar integers en floats. Hoe kan je ervoor zorgen dat prijzen en bedragen van de invoer worden opgeslagen als centen?

# Pas feestlunch.py zo aan dat je gaat rekenen met centen (integer values) in plaats van met euro's (float values)
# Pas speelhaldag.py zo aan dat je gaat rekenen met centen (integer values) in plaats van met euro's (float values)
 
# Test de goede werking van beide programma’s! Maak daarvan screenshots.
# Commit beide bestanden.
# Lever hier de programma’s + screenshots in


a = int(input("Welk antwoord wil je 1 of 2? "))

if a == 1:
    Crossantjes = int(input("Hoeveel crossantjes? "))
    CrossantjeKosten = 0.39
    Stokbroden = int(input("Hoeveel Stokbroden? "))
    StokbrodenKosten = 2.78
    KostingsBonnen = int(input("Hoeveel Kortingsbonnen? "))
    Korting = 0.5
    antwoord = (Crossantjes * CrossantjeKosten) + (Stokbroden * StokbrodenKosten) - (KostingsBonnen * Korting)
    print(f"De feestlunch kost je bij de bakker {antwoord} euro voor de {Crossantjes} croissantjes en de {Stokbroden} stokbroden als de {KostingsBonnen} kortingsbonnen nog geldig zijn!")

else:
    personen = int(input("Hoeveel personen? "))
    toegang = 7.45
    VIPVR = 0.37
    tijd = int(input("Hoelang vr gamen? "))
    kosten = (personen * toegang) + (tijd / 5 * VIPVR * personen)
    print(f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {tijd} minuten VR kost je maar {kosten} euro")
