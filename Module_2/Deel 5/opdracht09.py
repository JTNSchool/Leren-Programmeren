from fruitmand import fruitmand
Txt = ""
for fruit in fruitmand:
    if fruit["name"] == "druif":
        fruitmand.remove(fruit)
    else:
        print(fruit)
        if fruit["color"] not in Txt:
            Txt = Txt + fruit["color"] + " "
print(Txt)