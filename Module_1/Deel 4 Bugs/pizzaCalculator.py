def IntVraag(vraag):
    while True:
        antwoord = input(vraag)
        try:
            return int(antwoord)
        except ValueError:
            print(f"{antwoord} is geen integer! probeer opnieuw")


prijzen = {
    "small": 7.49,
    "medium": 9.49,
    "large": 14.49
}

#inputs
small = IntVraag("Hoeveel pizza Small will je? ")
medium = IntVraag("Hoeveel pizza Medium will je? ")
large = IntVraag("Hoeveel pizza Large will je? ")

#Berekeningen
smallTotaal = small * prijzen["small"]
mediumTotaal = small * prijzen["medium"]
largeTotaal = small * prijzen["large"]
totaal = smallTotaal + mediumTotaal + largeTotaal

#Bonnetje

print("--------------------------------------------------")
print()
print(f"Small: {small} * €{prijzen['small']} = €{smallTotaal}")
print(f"medium: {medium} * €{prijzen['medium']} = €{mediumTotaal}")
print(f"large: {large} * €{prijzen['large']} = €{largeTotaal}")
print(f"Totaal: {small + medium + large} Pizzas =  €{totaal}")
print()
print("--------------------------------------------------")

