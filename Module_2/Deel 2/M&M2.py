
# Maak functionaliteit die één lege Dictionary datatype (zak met M&M’s) vult aan de hand van het gekozen aantal. 
# De kleuren moeten willekeurig gekozen worden uit de beschikbare kleuren in de List aangemaakt in punt 1.
# Het programma print als laatste de zak met M&M’s.
 
# Let op: Elke kleur komt maar 1x voor als key in de dictionary. 
# De value is een nummer van de hoeveelheid M&M’s van de betreffende kleur die zich in de zak bevinden! en een kleur die niet in de zak voorkomt 
# (value 0) mag ook niet in de dictionary voorkomen.


import random

kleuren = ("oranje", "blauw", "groen", "geel", "bruin")

kleurendict = {
    "oranje": 0,
    "blauw": 0,
    "groen": 0,
    "geel": 0,
    "bruin": 0,
}

def GetAwnser(txt):
    while True:
        getal = input(txt)
        try:
            getal = int(getal)
            return getal
        except ValueError:
            print(f"{getal} is geen getal")


Aantal = GetAwnser("Hoeveel M&M's moeten er in de zak komen? ")


for i in range(Aantal):
    kleurendict[random.choice(kleuren)] += 1
print(kleurendict)