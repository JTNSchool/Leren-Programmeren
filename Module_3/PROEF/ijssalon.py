#Amount, BakOfHoorn
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

def AskBolletjesAmount(Info):
    Amount = int(AskQuestion("Hoeveel bolletjes wilt u?", "integer"))
    if Amount <= 8:
        Info.update({"Amount": Amount})
        HoorntjeOrBakje(Info)
    else:
        print("Sorry, zulke grote bakken hebben we niet")
        AskBolletjesAmount(Info)

def HoorntjeOrBakje(Info):
    if Info["Amount"] <= 3:
        BakOfHoorn = AskQuestion(f"Wilt u deze {Info['Amount']} bolletje(s) in een bakje of een hoorntje?", ["Bakje", "Hoorntje"])
        Info.update({"BakOfHoorn": BakOfHoorn})
    else:
        print(f"Dan krijgt u van mij een bakje met {Info['Amount']} bolletjes")
        Info.update({"BakOfHoorn": "Bakje"})
    AskSmaak(Info)

def AskSmaak(Info):
    Smaken = {
        "C": "Chocolade",
        "V": "Vanille",
        "A": "Aardbei",
        "M": "Munt", 
    }
    Opties = ""
    SmakenList = list(Smaken.keys())
    AllowedAwsners = []
    IjsDict = {}

    for i in Smaken:
        AllowedAwsners.append(i)
        if SmakenList[len(Smaken)-1] == i:
            Opties = Opties + f" {i}) {Smaken[i]}"
        else:
            Opties = Opties + f" {i}) {Smaken[i]},"
    
    for num in range(1, Info["Amount"]+1):
        Letter = AskQuestion(f"Welke smaak wilt u voor bolletje nummer {num}? {Opties}?", AllowedAwsners)
        Smaak = Smaken[Letter]
        if Smaak in IjsDict:
            IjsDict[Smaak] += 1
        else:
            IjsDict.update({Smaak: 1})
    GiveIcecream(Info, IjsDict)

def GiveIcecream(Info, SmakenDict):
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
        AskBolletjesAmount(Info)
    else:
        PrintReceipt(Info)
    
def PrintReceipt(Info):
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
                TotaleStats.update({item: order[item]})

    print('----------["Papi Gelato"]----------')
    #length - item etc
    for item in TotaleStats:
        if item != "Smaken":
            TotalePrijs += round(TotaleStats[item] * Prijzen[item], 2)
            print(f" {item}    {TotaleStats[item]} x €{Prijzen[item]} = € {round(TotaleStats[item] * Prijzen[item], 2)}")
        else:
            for smaak in TotaleStats[item]:
                TotalePrijs += round(TotaleStats[item][smaak] * Prijzen['Bolletjes'], 2)
                print(f" {smaak}    {TotaleStats[item][smaak]} x €{Prijzen['Bolletjes']} = € {round(TotaleStats[item][smaak] * Prijzen['Bolletjes'], 2)}")
    print(f"-------------------- +")
    print(f"Totaal        = €{round(TotalePrijs,2)}")

    print("Bedankt en tot ziens!")
    print(Info)



#----------------------------------------
Welcome()