from fruitmand import fruitmand

Meloen = [{
    'name' : 'meloen',
    'weight' : 10000,
    'color' : 'green',
    'round' : True
}]

fruitmand = fruitmand + Meloen
for fruit in fruitmand:
    print(fruit["weight"])