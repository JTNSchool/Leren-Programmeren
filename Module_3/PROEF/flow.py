from functies import *

print("Welkom bij Papi Gelato")
TypeKlant = ParticulierOfZakelijk()
while True: 
    Bolletjes = VraagBolletjesAantal(TypeKlant)
    BakOfHoorn = HoorntjeOrBakje(Bolletjes, TypeKlant)
    Smaken = VraagSmaak(Bolletjes, TypeKlant)

    try:
        Toppingkost = VraagTopping(Bolletjes, BakOfHoorn, Toppingkost, TypeKlant)
    except NameError:
        Toppingkost = VraagTopping(Bolletjes, BakOfHoorn, TypeKlant)

    if TypeKlant == "Particulier":    
        try:
            Bestelling, MeerIjs = GeefIjsje({"BakOfHoorn": BakOfHoorn, "Aantal": Bolletjes}, Smaken, TypeKlant, Bestelling)
        except NameError:
            Bestelling, MeerIjs = GeefIjsje({"BakOfHoorn": BakOfHoorn, "Aantal": Bolletjes}, Smaken, TypeKlant)

        if MeerIjs in data.NeeOptie:
            break
    else:
        Bestelling = GeefIjsje({"BakOfHoorn": BakOfHoorn, "Aantal": Bolletjes}, Smaken, TypeKlant)
        break

    
Creeerbonnetje(Bestelling, Toppingkost, TypeKlant)