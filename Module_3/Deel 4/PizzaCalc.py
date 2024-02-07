PRIJZEN = {
    "Small": 6.50,
    "Medium": 9.30,
    "Large": 11.10,
    "TEST": 1999
}

def Input_Int(txt):
    while True:
        antwoord = input(txt + " ")
        try:
            antwoord = int(antwoord)
            return antwoord
        except ValueError:
            print(f"{antwoord} is geen heel getal")


#Aantal pizzas
AantalPizzas = {}
for grote in PRIJZEN:
    amount = Input_Int(f"Hoeveel {grote} pizza's wilt u?")
    if amount >= 1:
        AantalPizzas.update({grote: amount})

#kosten berekenen
Kosten = {}
for pizza in AantalPizzas:
    cost = round(AantalPizzas[pizza] * PRIJZEN[pizza], 2)
    try:
        cost = int(cost)
    except ValueError:
        pass
    Kosten.update({pizza: cost})

#Bonnentje
print('************** KASSA BON *************')
totaal = 0
for pizza in Kosten:
    print(f"Pizza's {pizza}:    {AantalPizzas[pizza]} x {PRIJZEN[pizza]} = {Kosten[pizza]}")
    totaal += Kosten[pizza]

print('--------------------------------------')
print(f'Te betalen:                   €{totaal}')