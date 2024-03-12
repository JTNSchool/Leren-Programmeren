import data
#Vraag een vraag door alleen goede antwoorden vanuit opties 
def VraagVraag(Question, Options):
    while True:
        Awnser = input(Question + " ").capitalize()
        if Options == "integer":
            try:
                Awnser = int(Awnser)
                return Awnser
            except ValueError:
                print("Sorry dat is geen optie die we aanbieden...")
        else:
            if Awnser in Options:
                return Awnser
            else:
                print("Sorry dat is geen optie die we aanbieden...")

#Vraag of de klant een Particulier is of Zakelijk
def ParticulierOfZakelijk() -> str:
    Antwoord = VraagVraag("Bent u 1) een particuliere klant of 2) een zakelijke klant?", ["1","2"])
    if Antwoord == "1":
        return "Particulier"
    else:
        return "Zakelijk"

#Vraag het aantal bolletjes of liters
def VraagBolletjesAantal(TypeKlant) -> int:
    if TypeKlant == "Particulier":
        while True:
            Aantal = int(VraagVraag("Hoeveel bolletjes wilt u?", "integer"))
            if Aantal <= 8 and Aantal >= 1:
                return Aantal
            else:
                print("Sorry, zulke grote bakken hebben we niet")
    else:
        while True:
            Aantal = int(VraagVraag("Hoeveel liter ijs wilt u?", "integer"))
            if Aantal >= 1:
                return Aantal
            else:
                print("Sorry, zulke grote bakken hebben we niet")

#Vraag of de klant zijn ijsje in een hoorntje of bakje wilt
def HoorntjeOrBakje(Bolletjes, TypeKlant) -> str:
    if TypeKlant == "Particulier": 
        if Bolletjes <= 3:
            BakOfHoorn = VraagVraag(f"Wilt u deze {Bolletjes} bolletje(s) in een bakje of een hoorntje?", ["Bakje", "Hoorntje"])
        else:
            print(f"Dan krijgt u van mij een bakje met {Bolletjes} bolletjes")
            BakOfHoorn = "Bakje"
        return BakOfHoorn
    else:
        return 0

#Vraag de smaken per bolletje of liter ijs
def VraagSmaak(bolletjes, TypeKlant) -> dict:
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
    
    if TypeKlant == "Particulier":
        objectt = "bolletje"
    else:
        objectt = "liter"
    for num in range(1, bolletjes+1):
        Letter = VraagVraag(f"Welke smaak wilt u voor {objectt} nummer {num}? {Opties}?", ToegestaanAntwoorden)
        Smaak = Smaken[Letter]
        if Smaak in BolletjesDict:
            BolletjesDict[Smaak] += 1
        else:
            BolletjesDict.update({Smaak: 1})
    return BolletjesDict

#Vraag de topping voor over het ijsje heen
def VraagTopping(bolletjes, BakOfHoorn, TypeKlant, ToppingKost=0):
    if TypeKlant == "Zakelijk":
        return 0
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

#Geeft het ijsje aan de klant en als het particulier is dan vragen of hij meer wilt bestellen
def GeefIjsje(Info, SmakenDict, TypeKlant, Bestelling=0):
    
    HuidigIjsje = {'Bolletjes': Info['Aantal'], Info["BakOfHoorn"]: 1, "Smaken": SmakenDict}
    if TypeKlant == "Particulier":
        print(f"Hier is uw {Info['BakOfHoorn']} met {Info['Aantal']} bolletje(s).")
        #Save order in list
        if Bestelling != 0:
            OudIjsje = Bestelling
        else:
            OudIjsje = []
        
        
        Bestelling = OudIjsje + [HuidigIjsje]
        MeerIjs = VraagVraag("Wilt u nog meer bestellen?", data.JaNeeOptie)
        
        return Bestelling, MeerIjs
    else:
        print(f"Hier is uw bestelling met {Info['Aantal']} liter(s).")
        return HuidigIjsje


def Creeerbonnetje(Bestelling, ToppingKost, TypeKlant):
    TotaleStatastieken = {}
    if TypeKlant == "Particulier": 
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
    else:
        TotaleStatastieken = Bestelling

    ToonBonnetje(TotaleStatastieken, ToppingKost, TypeKlant)

    

#Toon het bonnetje aan de klant  
def ToonBonnetje(TotaleStatastieken, ToppingKost, TypeKlant):
    Prijzen = data.Prijzen
    Lengte = 15
    TotalePrijs = 0
    print('----------["Papi Gelato"]----------')
    if TypeKlant == "Zakelijk":
        #{'Bolletjes': 3, 0: 1, 'Smaken': {'Chocolade': 2, 'Vanille': 1}}
        for Smaak in TotaleStatastieken['Smaken']:
            Ruimte = (Lengte- len(Smaak)) * " "
            TotalePrijs += round(TotaleStatastieken['Smaken'][Smaak] * Prijzen['Liter'], 2)
            print(f" {Smaak}{Ruimte}{TotaleStatastieken['Smaken'][Smaak]} x €{Prijzen['Liter']:.2f} = €{round(TotaleStatastieken['Smaken'][Smaak] * Prijzen['Liter'], 2):.2f}")
    else:
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
    if TypeKlant == "Zakelijk":
        procent = 100 + data.BTW
        print(f"BTW ({data.BTW}%){' ' * 18}= €{round(TotalePrijs/procent*data.BTW,2):.2f}")
    print("Bedankt en tot ziens!")