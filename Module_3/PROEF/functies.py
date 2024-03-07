import data

def VraagVraag(Question, Options):
    while True:
        Awnser = input(Question + " ").capitalize()
        if Options == "integer":
            try:
                Awnser = int(Awnser)
                return Awnser
            except ValueError:
                print("Sorry dat snap ik niet...")
        else:
            if Awnser in Options:
                return Awnser
            else:
                print("Sorry dat snap ik niet...")

def Welkom():
    print("Welkom bij Papi Gelato")

def VraagBolletjesAantal():
    while True:
        Aantal = int(VraagVraag("Hoeveel bolletjes wilt u?", "integer"))
        if Aantal <= 8 and Aantal >= 1:
            return Aantal
        else:
            print("Sorry, zulke grote bakken hebben we niet")

def HoorntjeOrBakje(Bolletjes):
    if Bolletjes <= 3:
        BakOfHoorn = VraagVraag(f"Wilt u deze {Bolletjes} bolletje(s) in een bakje of een hoorntje?", ["Bakje", "Hoorntje"])
    else:
        print(f"Dan krijgt u van mij een bakje met {Bolletjes} bolletjes")
        BakOfHoorn = "Bakje"
    return BakOfHoorn

def VraagSmaak(bolletjes):
    Smaken = data.Smaken
    Opties = ""
    SmakenLijst = list(Smaken.keys())
    ToegestaanAntwoorden = []
    BolletjesDict = {}

    for i in Smaken:
        ToegestaanAntwoorden.append(i)
        if SmakenLijst[len(Smaken)-1] == i:
            Opties = Opties + f" {i}) {Smaken[i]}"
        else:
            Opties = Opties + f" {i}) {Smaken[i]},"
    
    for num in range(1, bolletjes+1):
        Letter = VraagVraag(f"Welke smaak wilt u voor bolletje nummer {num}? {Opties}?", ToegestaanAntwoorden)
        Smaak = Smaken[Letter]
        if Smaak in BolletjesDict:
            BolletjesDict[Smaak] += 1
        else:
            BolletjesDict.update({Smaak: 1})
    return BolletjesDict

def VraagTopping(bolletjes, BakOfHoorn, ToppingKost=0):
    Toppings = data.Toppings
    Toppings["C"]["Kost"] = 0.3 * bolletjes
    if BakOfHoorn == "Bakje":
        Toppings["D"]["Kost"] = 0.9

    Opties = ""
    ToppingsLijst = list(Toppings.keys())
    ToegestaanAntwoorden = []

    for i in Toppings:
        ToegestaanAntwoorden.append(i)
        if ToppingsLijst[len(Toppings)-1] == i:
            Opties = Opties + f" {i}) {Toppings[i]['Naam']}"
        else:
            Opties = Opties + f" {i}) {Toppings[i]['Naam']},"
    
    Letter = VraagVraag(f"Wat voor topping wilt u op dit ijsje?: {Opties}?", ToegestaanAntwoorden)
    ToppingKost += Toppings[Letter]["Kost"]

    return ToppingKost

def GeefIjsje(Info, SmakenDict, Bestelling=0):
    print(f"Hier is uw {Info['BakOfHoorn']} met {Info['Aantal']} bolletje(s).")
    #Save order in list
    if Bestelling != 0:
        OudIjsje = Bestelling
    else:
        OudIjsje = []
    
    HuidigIjsje = {'Bolletjes': Info['Aantal'], Info["BakOfHoorn"]: 1, "Smaken": SmakenDict}
    Bestelling = OudIjsje + [HuidigIjsje]
    MeerIjs = VraagVraag("Wilt u nog meer bestellen?", data.JaNeeOptie)
    
    return Bestelling, MeerIjs
    
def ToonBonnetje(Bestelling, ToppingKost):
    TotaleStatastieken = {}
    Prijzen = data.Prijzen
    TotalePrijs = 0
    for order in Bestelling:
        for item in order:
            if item in TotaleStatastieken:
                if item != "Smaken":
                    TotaleStatastieken[item] += order[item]
                else:
                    for i in order[item]:
                        if i in TotaleStatastieken["Smaken"]:
                            TotaleStatastieken["Smaken"][i] += order[item][i]
                        else:
                            TotaleStatastieken["Smaken"][i] = order[item][i]
            else:
                if item != "Bolletjes":
                    TotaleStatastieken.update({item: order[item]})

    Lengte = 15

    print('----------["Papi Gelato"]----------')
    print(TotaleStatastieken)
    for item in TotaleStatastieken:
        
        if item != "Smaken":
            Ruimte = (Lengte- len(item)) * " "
            TotalePrijs += round(TotaleStatastieken[item] * Prijzen[item], 2)
            print(f" {item}{Ruimte}{TotaleStatastieken[item]} x €{Prijzen[item]:.2f} = €{round(TotaleStatastieken[item] * Prijzen[item], 2):.2f}")
        else:
            for smaak in TotaleStatastieken[item]:
                Ruimte = (Lengte- len(smaak)) * " "
                TotalePrijs += round(TotaleStatastieken[item][smaak] * Prijzen['Bolletjes'], 2)
                print(f" {smaak}{Ruimte}{TotaleStatastieken[item][smaak]} x €{Prijzen['Bolletjes']:.2f} = €{round(TotaleStatastieken[item][smaak] * Prijzen['Bolletjes'], 2):.2f}")
    if ToppingKost > 0:
        TotalePrijs += ToppingKost
        Ruimte = (25- len("Toppings")) * " "
        print(f" Toppings{Ruimte}= €{round(ToppingKost,2):.2f}")
        
    print(f"{'-' * 34} +")  
    print(f"Totaal{' ' * 20}= €{round(TotalePrijs,2):.2f}")
    print("Bedankt en tot ziens!")