#Verwijder (met code) de druif uit de fruitmand en print alleen alle verschillende kleuren in de fruitmand, in maximaal 8 regels code (minus lege regels en de import).

from fruitmand import fruitmand
Txt = ""
for fruit in fruitmand:
    if fruit["name"] == "druif":
        fruitmand.remove(fruit)
    else:
        if fruit["color"] not in Txt:
            Txt = Txt + fruit["color"] + " "
print(Txt)



        #Print 1 keeer iedere kleur