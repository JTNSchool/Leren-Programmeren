def AskQuestion(Question, Options):
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
    Info = {}
    AskBolletjesAmount(Info)

def AskBolletjesAmount(Info, ToppingKost=0):
    Amount = int(AskQuestion("Hoeveel bolletjes wilt u?", "integer"))
    if Amount <= 8:
        Info.update({"Amount": Amount})
        HoorntjeOrBakje(Info, ToppingKost)
    else:
        print("Sorry, zulke grote bakken hebben we niet")
        AskBolletjesAmount(Info, ToppingKost)

def HoorntjeOrBakje(Info, ToppingKost):
    if Info["Amount"] <= 3:
        BakOfHoorn = AskQuestion(f"Wilt u deze {Info['Amount']} bolletje(s) in een bakje of een hoorntje?", ["Bakje", "Hoorntje"])
        Info.update({"BakOfHoorn": BakOfHoorn})
    else:
        print(f"Dan krijgt u van mij een bakje met {Info['Amount']} bolletjes")
        Info.update({"BakOfHoorn": "Bakje"})
    AskSmaak(Info, ToppingKost)

def AskSmaak(Info, ToppingKost):
    Smaken = {
        "C": "Chocolade",
        "V": "Vanille",
        "A": "Aardbei",
        "M": "Munt", 
    }
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
    
    for num in range(1, Info["Amount"]+1):
        Letter = AskQuestion(f"Welke smaak wilt u voor bolletje nummer {num}? {Opties}?", AllowedAwsners)
        Smaak = Smaken[Letter]
        if Smaak in BolletjesDict:
            BolletjesDict[Smaak] += 1
        else:
            BolletjesDict.update({Smaak: 1})
    AskTopping(Info, BolletjesDict, ToppingKost)


def AskTopping(Info, BolletjesDict, ToppingKost):
    Toppings = {
        "A": {"Naam": "Geen", "Kost": 0},
        "B": {"Naam": "Slagroom", "Kost": 0.5},
        "C": {"Naam": "Sprinkels", "Kost": 0.3 * Info["Amount"]},
        "D": {"Naam": "Caramel Saus", "Kost": 0.6} 
    }
    if Info["BakOfHoorn"] == "Bakje":
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
    
    Letter = AskQuestion(f"Wat voor topping wilt u op dit ijsje?: {Opties}?", AllowedAwsners)
    ToppingNaam = Toppings[Letter]["Naam"]
    ToppingKost += Toppings[Letter]["Kost"]


    
    GiveIcecream(Info, BolletjesDict, ToppingKost)


def GiveIcecream(Info, SmakenDict, ToppingKost):
    print(f"Hier is uw {Info['BakOfHoorn']} met {Info['Amount']} bolletje(s).")
    #Save order in list
    if "Order" in Info:
        OldIcecreams = Info["Order"] 
    else:
        OldIcecreams = []
    
    CurrentIcecream = {'Bolletjes': Info['Amount'], Info["BakOfHoorn"]: 1, "Smaken": SmakenDict}
    Info = {"Order": OldIcecreams + [CurrentIcecream]}
    MoreIcecream = AskQuestion("Wilt u nog meer bestellen?", ["Ja", "J", "Nee", "N"])
    if MoreIcecream in ["Ja", "J"]:
        AskBolletjesAmount(Info, ToppingKost)
    else:
        PrintReceipt(Info, ToppingKost)
    
def PrintReceipt(Info, ToppingKost):
    TotaleStats = {}
    Prijzen = {
        'Bolletjes': 1.10,
        "Hoorntje": 1.25,
        "Bakje": 0.75
    }
    TotalePrijs = 0
    #1 Big Dict
    for order in Info["Order"]:
        for item in order:
            if item in TotaleStats:
                if item != "Smaken":
                    TotaleStats[item] += order[item]
                else:
                    for i in order[item]:
                        if i in TotaleStats["Smaken"]:
                            print(i, order[item] )
                            TotaleStats["Smaken"][i] += order[item][i]
            else:
                if item != "Bolletjes":
                    TotaleStats.update({item: order[item]})

    Bonnetje = []
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



#----------------------------------------
Welcome()