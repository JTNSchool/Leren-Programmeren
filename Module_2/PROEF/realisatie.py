# Vraag namen op van deelnemers (alle namen moeten uniek zijn)
# Bij minder dan 3 namen, blijf je doorvragen naar namen.
# Als er 3 of meer namen zijn opgegeven kunnen er lootjes worden getrokken
# Iedereen krijgt (random) één uniek lootje
# Aan het einde mag niemand het lootje van zichzelf hebben
# Als alles verdeeld is wordt er een lijst met namen geprint en de bijbehorende lootjes

import random, time

Lijst = {}
Personen = []

def VraagDeelnemers():
    while True:
        AantalDeelnemers = input("Hoeveel deelnemers doen er mee? ").lower()
        try:
            AantalDeelnemers = int(AantalDeelnemers)
            if AantalDeelnemers in range(3, 99999999999999):
                return AantalDeelnemers
            else:
                raise ValueError
        except ValueError:
            print("Vul een getal in hoger dan 3")

def ShuffleAndGive():
    global Lijst, Personen
    Personen = [] + Namen
    random.shuffle(Personen)
    Lijst = {}
    for naam in Namen:
        Lijst.update({naam: Personen[0]})
        Personen.pop(0)


NamenRandom = []
AantalDeelnemers = VraagDeelnemers()
Namen = []

Aantal = AantalDeelnemers
while Aantal > 0:
    naam = input("Vul een naam in: ").lower()
    if naam not in Namen:
        Namen.append(naam)
        Aantal -= 1
    else:
        print("Deze naam zit er al in")

Wrong = 0
while True:
    ShuffleAndGive()
    MaxScore = len(Lijst)
    Score = 0
    for Naam in Lijst:
        if Naam != Lijst[Naam]:
            Score += 1
    if Score == MaxScore:
        print(f"De lijst is gemaakt in {Wrong} Pogingen")
        print(Lijst)
        break
    else:
        Wrong += 1

NaamZien = input("Hoe heet je? ").lower()
if NaamZien in Lijst:
    print(f"{NaamZien} jij hebt {Lijst[NaamZien]} getrokken")
else:
    print("Dat is geen geldige naam in de Lijst")