# Breid nu het programma uit. 
# Je gaat een nieuwe functie maken die net zolang de functie van het vragen uitvoert totdat je het woord 'stop' invoert bij de vraag: 
# “Toets enter om door te gaan of stop om te printen:” (let op: de eerste functie laat je met rust).
# De nieuwe functie is verrantwoordelijk voor het verzamelen en het stoppen vragen van de gegevens en heeft een output/return van een list
# Pas je output bestand aan zodat de verzamel functie word aangeroepen ipv de vragen functie en dan deze output geeft.

def NaamEnLeeftijd(aantal):
    Name = input("Vul u naam in: ")
    while True:
        Age = input("Vul u leeftijd in: ")
        try:
            Age = int(Age)
            break
        except ValueError:
            print(f"{Age} is not a integer")

    return {aantal: {"Name": Name, "Age": Age}}

def InfLoopTotStop():
    dict = {}
    txt = ""
    while True:
        dict.update(NaamEnLeeftijd(len(dict)))
        inp = input("Wil je nog een naam toe voegen? ").lower()
        if inp not in ("ja", "yes", "j", "y"):
            for persoon in dict:
                txt = txt + f"{dict[persoon]['Name']} is {dict[persoon]['Age']} jaar\n"
            return txt



print(InfLoopTotStop())