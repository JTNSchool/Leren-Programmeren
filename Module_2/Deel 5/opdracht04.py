from fruitmand import fruitmand
import random

def GetAwnser(txt):
    while True:
        getal = input(txt)
        try:
            getal = int(getal)
            return getal
        except ValueError:
            print(f"{getal} is geen getal")

amount = GetAwnser("Hoeveel fruitstukken wil je? ")
mand = {}
for i in range(amount):
    RandomFruit = random.choice(fruitmand)
    print(RandomFruit["name"])
    if RandomFruit["name"] in mand:
        mand[RandomFruit["name"]] += 1
    else:
        mand.update({RandomFruit["name"]: 1})
print(f"De fruitstukken: {mand}")
