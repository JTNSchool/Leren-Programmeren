# Gebruik geen global variabelen: wissel gegevens met functions alleen uit via parameters en returns
# Laat een function maar één taak uitvoeren.
# Geef een function een naam die precies aanduidt wat de taak is.

def AskQuestion(Question, Options):
    while True:
        Awnser = input(Question + " ").capitalize()
        if Awnser in Options:
            return Awnser
        else:
            print("Sorry dat snap ik niet...")


def Welcome():
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zo lang het maar vanilleijs is.")
    Info = {}
    AskBolletjesAmount(Info)

def AskBolletjesAmount(Info):
    Amount = int(AskQuestion("Hoeveel bolletjes wilt u?", [str(i) for i in range(1, 9999999)]))
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
    GiveIcecream(Info)

def GiveIcecream(Info):
    print(f"Hier is uw {Info['BakOfHoorn']} met {Info['Amount']} bolletje(s).")
    #Save order in list
    if "Order" in Info:
        OldIcecreams = Info["Order"] 
    else:
        OldIcecreams = []
    CurrentIcecream = [Info['Amount'], Info["BakOfHoorn"]]
    Info = {"Order": OldIcecreams + [CurrentIcecream]}

    MoreIcecream = AskQuestion("Wilt u nog meer bestellen?", ["Ja", "J", "Nee", "N"])

    if MoreIcecream in ["Ja", "J"]:
        AskBolletjesAmount(Info)
    else:
        print("Bedankt en tot ziens!")
        #Print order (test)
        for i in Info["Order"]:
            print(i)


#----------------------------------------
Welcome()