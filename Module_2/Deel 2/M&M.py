import random

kleuren = ("oranje", "blauw", "groen", "bruin")

def GetAwnser(txt):
    while True:
        getal = input(txt)
        try:
            getal = int(getal)
            return getal
        except ValueError:
            print(f"{getal} is geen getal")


Aantal = GetAwnser("Hoeveel M&M's moeten er in de zak komen? ")

Zak = list()
for i in range(Aantal):
    Zak.append(random.choice(kleuren))
print(Zak)