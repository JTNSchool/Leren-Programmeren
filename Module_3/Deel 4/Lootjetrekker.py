import random

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
                print("Vul een getal in hoger dan 3")
        except ValueError:
            print("Vul een getal in")

def ShuffleAndGive():
    global Lijst, Personen
    Personen = [] + Namen
    random.shuffle(Personen)
    Lijst = {}
    for naam in Namen:
        Lijst.update({naam: Personen[0]})
        Personen.pop(0)

def GetPresents():
    Kados = []
    max = 3
    while True:
        kado = input(f"Welk kado wil je? ({len(Kados)+1}/{max})").capitalize()
        if kado not in Kados:
            Kados.append(kado)
            if len(Kados) >= max:
                return Kados
        else:
            print("Dit kado zit er al in")


AantalDeelnemers = VraagDeelnemers()
KadoDict = {}
Namen = []

Aantal = AantalDeelnemers
while Aantal > 0:
    naam = input("Vul een naam in: ").capitalize()
    if naam not in Namen:
        Namen.append(naam)
        Kados = GetPresents()
        KadoDict.update({naam: Kados})
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

NaamZien = input("Hoe heet je? ").capitalize()
if NaamZien in Lijst:
    print(f'''
{NaamZien} jij hebt {Lijst[NaamZien]} getrokken hier is {Lijst[NaamZien]}'s lijstje:
{KadoDict[Lijst[NaamZien]]}
          ''')
else:
    print("Dat is geen geldige naam in de Lijst")