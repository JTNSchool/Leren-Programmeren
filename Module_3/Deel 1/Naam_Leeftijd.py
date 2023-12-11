# Je gaat een programma maken die een naam en leeftijd vraagt en op het scherm print. 
# De volgende eisen worden gesteld aan de applicatie:
# De gebruiker kan de namen en leeftijden zelf invullen via een input
# Aan het einde van het programma word het resultaat netjes geprint zoals dit:
# Voor het vragen van de naam en de leeftijd maak je een functie die dit voor je doet.
# De output/return van deze functie is een dictionairy met de properties ‘name’ en ‘age’.
# Buiten de functie doe je de print, door eerst de functie aan te roepen.
# Lever hier een screenshot van het resultaat in en vergeet niet te commiten


def NaamEnLeeftijd():
    Name = input("Vul u naam in: ")
    while True:
        Age = input("Vul u leeftijd in: ")
        try:
            Age = int(Age)
            break
        except ValueError:
            print(f"{Age} is not a integer")

    return {"Name": Name, "Age": Age}

Info = NaamEnLeeftijd()
print(f"{Info['Name']} is {Info['Age']} jaar")