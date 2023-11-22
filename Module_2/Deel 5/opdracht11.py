from fruitmand import fruitmand

KleurenLijst = []

for fruit in fruitmand:
    if fruit["color"] not in KleurenLijst:
        KleurenLijst.append(fruit["color"])

while True: 
    Kleur = input(f"Kies een kleur uit de lijst {KleurenLijst}: ").lower()
    if Kleur in KleurenLijst:
        break
    else:
        print(f"De kleur {Kleur} zit er niet in de fruitmand")

Rond = 0
NietRond = 0

for fruit in fruitmand:
    if fruit['color'] == Kleur:
        if fruit["round"]:
            Rond += 1
        else:
            NietRond += 1

Verschil = abs(Rond-NietRond)

if Rond > NietRond:
    print(f"Er zijn {Verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {Kleur}")
elif Rond < NietRond:
    print(f"Er zijn {Verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {Kleur}")
else:
    print(f"Er zijn {Rond} ronde vruchten en {NietRond} niet ronde vruchten in de kleur {Kleur}")