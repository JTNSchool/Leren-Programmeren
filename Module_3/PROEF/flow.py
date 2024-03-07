from functies import *

Welcome()
while 0:  
    Bolletjes = AskBolletjesAmount()
    BakOfHoorn = HoorntjeOrBakje(Bolletjes)
    Smaken = AskSmaak(Bolletjes)

    try:
        Toppingkost = AskTopping(Bolletjes, BakOfHoorn, Toppingkost)
    except NameError:
        Toppingkost = AskTopping(Bolletjes, BakOfHoorn)
    
    try:
        Bestelling, MoreIcecream = GiveIcecream({"BakOfHoorn": BakOfHoorn, "Amount": Bolletjes}, Smaken, Bestelling)
    except NameError:
        Bestelling, MoreIcecream = GiveIcecream({"BakOfHoorn": BakOfHoorn, "Amount": Bolletjes}, Smaken)

    if MoreIcecream in data.NeeOptie:
        break

Bestelling = [{'Bolletjes': 5, 'Bakje': 1, 'Smaken': {'Chocolade': 5}}, {'Bolletjes': 4, 'Bakje': 1, 'Smaken': {'Vanille': 2, 'Aardbei': 1, 'Munt': 1}}]
Toppingkost = 0
PrintReceipt(Bestelling, Toppingkost)