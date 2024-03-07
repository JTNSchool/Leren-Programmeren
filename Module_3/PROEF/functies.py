import data

def VraagQuestion(Question, Options):
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

def Welcome():
    print("Welkom bij Papi Gelato")

def VraagBolletjesAmount():
    Amount = int(VraagQuestion("Hoeveel bolletjes wilt u?", "integer"))
    if Amount <= 8:
        return Amount
    else:
        print("Sorry, zulke grote bakken hebben we niet")
        VraagBolletjesAmount()

def HoorntjeOrBakje(bolletjes):
    if bolletjes <= 3:
        BakOfHoorn = VraagQuestion(f"Wilt u deze {bolletjes} bolletje(s) in een bakje of een hoorntje?", ["Bakje", "Hoorntje"])
    else:
        print(f"Dan krijgt u van mij een bakje met {bolletjes} bolletjes")
        BakOfHoorn = "Bakje"
    return BakOfHoorn

def VraagSmaak(bolletjes):
    Smaken = data.Smaken
    Opties = ""
    SmakenList = list(Smaken.keys())
    AllowedAwsners = []
    BolletjesDict = {}

    for i in Smaken:
        AllowedAwsners.append(i)
        if SmakenList[len(Smaken)-1] == i:
            Opties = Opties + f" {i}) {Smaken[i]}"
        else:
            Opties = Opties + f" {i}) {Smaken[i]},"
    
    for num in range(1, bolletjes+1):
        Letter = VraagQuestion(f"Welke smaak wilt u voor bolletje nummer {num}? {Opties}?", AllowedAwsners)
        Smaak = Smaken[Letter]
        if Smaak in BolletjesDict:
            BolletjesDict[Smaak] += 1
        else:
            BolletjesDict.update({Smaak: 1})
    return BolletjesDict

def VraagTopping(bolletjes, BakOfHoorn, ToppingKost=0):
    Toppings = data.Toppings
    Toppings["C"]["Kost"] *= 0.3 * bolletjes
    if BakOfHoorn == "Bakje":
        Toppings["D"]["Kost"] = 0.9

    Opties = ""
    ToppingsList = list(Toppings.keys())
    AllowedAwsners = []

    for i in Toppings:
        AllowedAwsners.append(i)
        if ToppingsList[len(Toppings)-1] == i:
            Opties = Opties + f" {i}) {Toppings[i]['Naam']}"
        else:
            Opties = Opties + f" {i}) {Toppings[i]['Naam']},"
    
    Letter = VraagQuestion(f"Wat voor topping wilt u op dit ijsje?: {Opties}?", AllowedAwsners)
    ToppingKost += Toppings[Letter]["Kost"]

    return ToppingKost

def GiveIcecream(Info, SmakenDict, Bestelling=0):
    print(f"Hier is uw {Info['BakOfHoorn']} met {Info['Amount']} bolletje(s).")
    #Save order in list
    if Bestelling != 0:
        OldIcecreams = Bestelling
    else:
        OldIcecreams = []
    
    CurrentIcecream = {'Bolletjes': Info['Amount'], Info["BakOfHoorn"]: 1, "Smaken": SmakenDict}
    Bestelling = OldIcecreams + [CurrentIcecream]
    MoreIcecream = VraagQuestion("Wilt u nog meer bestellen?", data.JaNeeOptie)
    
    return Bestelling, MoreIcecream
    
def PrintReceipt(Bestelling, ToppingKost):
    TotaleStats = {}
    Prijzen = data.Prijzen
    TotalePrijs = 0
    for order in Bestelling:
        for item in order:
            if item in TotaleStats:
                if item != "Smaken":
                    TotaleStats[item] += order[item]
                else:
                    for i in order[item]:
                        if i in TotaleStats["Smaken"]:
                            TotaleStats["Smaken"][i] += order[item][i]
                        else:
                            TotaleStats["Smaken"][i] = order[item][i]
            else:
                if item != "Bolletjes":
                    TotaleStats.update({item: order[item]})

    Lengte = 15

    print('----------["Papi Gelato"]----------')
    for item in TotaleStats:
        
        if item != "Smaken":
            Ruimte = (Lengte- len(item)) * " "
            TotalePrijs += round(TotaleStats[item] * Prijzen[item], 2)
            print(f" {item}{Ruimte}{TotaleStats[item]} x €{Prijzen[item]:.2f} = €{round(TotaleStats[item] * Prijzen[item], 2):.2f}")
        else:
            for smaak in TotaleStats[item]:
                Ruimte = (Lengte- len(smaak)) * " "
                TotalePrijs += round(TotaleStats[item][smaak] * Prijzen['Bolletjes'], 2)
                print(f" {smaak}{Ruimte}{TotaleStats[item][smaak]} x €{Prijzen['Bolletjes']:.2f} = €{round(TotaleStats[item][smaak] * Prijzen['Bolletjes'], 2):.2f}")
    if ToppingKost > 0:
        TotalePrijs += ToppingKost
        Ruimte = (25- len("Toppings")) * " "
        print(f" Toppings{Ruimte}= €{round(ToppingKost,2):.2f}")
        
    print(f"{'-' * 34} +")  
    print(f"Totaal{' ' * 20}= €{round(TotalePrijs,2):.2f}")
    print("Bedankt en tot ziens!")