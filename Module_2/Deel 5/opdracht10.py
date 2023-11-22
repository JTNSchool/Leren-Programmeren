#Print (met code) de namen en het gewicht in kilogram van het fruit op volgorde van gewicht (zwaarste bovenaan).
from fruitmand import fruitmand

Fruit = []
for fruit in fruitmand:
    Fruit.append(fruit["weight"])
Fruit.sort()
print(Fruit)