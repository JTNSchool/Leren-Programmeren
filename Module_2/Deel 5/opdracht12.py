# Print de kleur, het gewicht en naam zoals onderstaand voorbeeld (dus volledig Nederlands) van het fruit met de langste naam, 
# je mag alleen de code het juiste stuk fruit laten kiezen.


from fruitmand import fruitmand

LangsteWoordDict = {'name': '.'}
for fruit in fruitmand:
    if len(fruit['name']) > len(LangsteWoordDict['name']):
        LangsteWoordDict = fruit
print(f"De {LangsteWoordDict['name']} ({len(LangsteWoordDict['name'])} letters) heeft een {LangsteWoordDict['color']} kleur en een gewicht van {LangsteWoordDict['weight'] / 1000} kg")