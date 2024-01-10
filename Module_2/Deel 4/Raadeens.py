import random

RandomGetal = 0
Fouten = 0
Rondes = 0
Win = 0

def CreateRandom():
    global RandomGetal, Fouten, Rondes
    Fouten = 0
    Rondes += 1
    RandomGetal = random.randint(1, 1000)
    print(RandomGetal)
    RaadGetal()


def NieuweRonde():
    global Rondes
    if Rondes >= 20:
        print(f"Je hebt {Rondes} keer gespeeld en {Win} rondes gewonnen")
    else:
        antw = input("Wil je nog een ronde spelen? ")
        if antw in ["ja", "j", "yes", "y"]:

            CreateRandom()
        else:
            print("Dat is een nee?")
            print(f"Je hebt {Rondes} keer gespeeld en {Win} rondes gewonnen")

def RaadGetal():
    global RandomGetal, Win, Fouten, Rondes
    while True:
        getal = input("Vul een getal in: ")
        try:
            getal = int(getal)
            if getal >= 1 and getal <= 1000:
                break
            else:
                print("Een getal tussen 1-1000!")
        except ValueError:
            print("Dat is geen geldig getal")

    verschil = abs(RandomGetal - getal)
    if getal == RandomGetal:
        print("geraden.")
        Win += 1
        Rondes += 1
        NieuweRonde()
    elif (getal < RandomGetal):
        print("Hoger")
        if verschil <= 20:
            print("Heel warm")
        elif verschil <= 50:
            print("Warm")
        Fouten += 1
        if Fouten >= 10:
            print(f"Je hebt 10x fout geraden het getal was {RandomGetal}")
            NieuweRonde()
        else:
            RaadGetal()
    elif (getal > RandomGetal):
        print("Lager")
        if verschil <= 20:
            print("Heel warm")
        elif verschil <= 50:
            print("Warm")
        Fouten += 1
        if Fouten >= 10:
            print(f"Je hebt 10x fout geraden het getal was {RandomGetal}")
            NieuweRonde()
        else:
            RaadGetal()

        
CreateRandom()