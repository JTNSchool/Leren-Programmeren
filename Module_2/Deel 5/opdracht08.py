from fruitmand import fruitmand

Meloen = [{
    'name' : 'meloen',
    'weight' : 10000,
    'color' : 'green',
    'round' : True
}]

fruitmand = fruitmand + Meloen
Gewicht = 0
for fruit in fruitmand:
    Gewicht += fruit["weight"]

print(Gewicht)