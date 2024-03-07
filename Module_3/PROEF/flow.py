from functies import *

Welcome()
while 0:  
    Bolletjes = VraagBolletjesAantal()
    BakOfHoorn = HoorntjeOrBakje(Bolletjes)
    Smaken = VraagSmaak(Bolletjes)

    try:
        Toppingkost = VraagTopping(Bolletjes, BakOfHoorn, Toppingkost)
    except NameError:
        Toppingkost = VraagTopping(Bolletjes, BakOfHoorn)
    
    try:
        Bestelling, MeerIjs = GiveIcecream({"BakOfHoorn": BakOfHoorn, "Aantal": Bolletjes}, Smaken, Bestelling)
    except NameError:
        Bestelling, MeerIjs = GiveIcecream({"BakOfHoorn": BakOfHoorn, "Aantal": Bolletjes}, Smaken)

    if MeerIjs in data.NeeOptie:
        break

Bestelling = [{'Bolletjes': 5, 'Bakje': 1, 'Smaken': {'Chocolade': 5}}, {'Bolletjes': 4, 'Bakje': 1, 'Smaken': {'Vanille': 2, 'Aardbei': 1, 'Munt': 1}}]
Toppingkost = 0
PrintReceipt(Bestelling, Toppingkost)