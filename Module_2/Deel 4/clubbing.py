PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

#bouw hieronder de floowchart na
prijs = 0
Naam = ""
leeftijd = 0
bandje = None
Drankje = None

def GetAwnser(vraag, antwoorden):
    while True:
        UserInput = input(vraag).lower()
        if UserInput in antwoorden:
            return UserInput
        else:
            print(f"{UserInput} is geen geldig antwoord.\n")


def Vraag(num):
    global leeftijd, bandje, prijs, Drankje

    if num == 1:
        vraag = "Hoe oud ben je? "
        antwoorden = [str(i) for i in range(1, 100)]
        antwoord = int(GetAwnser(vraag, antwoorden))
        
        if antwoord < 18:
            print("Sorry je mag niet naar binnen")
            print(f"probeer het in {18- antwoord} jaar nog een keer")
        else:
            leeftijd = antwoord
            Vraag(2)

    if num == 2:
        vraag = "Wat is je naam? "
        antwoord = input(vraag).lower()
        
        if antwoord in VIP_LIST:
            if leeftijd >= 21:
                bandje = "Blauw"
            else:
                bandje = "Rood"
            print(f"Je krijgt van mij een {bandje} bandje")
            Vraag(3)
        else:
            if leeftijd >= 21:
                print("Je krijgt van mij een stempel")
                bandje = "Stempel"
                Vraag(3)
            else:
                Vraag(3)

    if num == 3:
        vraag = "Wat wil je drinken? "
        antwoord = input(vraag).lower()
        
        if antwoord in DRANKJES:
            if antwoord == "cola":
                Drankje = antwoord
                prijs = PRIJS_COLA
                Vraag(5)

            elif antwoord == "bier":
                if bandje != None:
                    Drankje = antwoord
                    prijs = PRIJS_BIER
                    Vraag(5)
                else:
                    print("Sorry je mag geen alcohol bestellen onder de 21")
                    print(f"probeer het in {21- leeftijd} jaar nog een keer")
            
            elif antwoord == "champagne":
                Drankje = antwoord
                if bandje == "Blauw":
                    prijs = PRIJS_BIER
                    print(f"Alstublieft u {antwoord} dat is dan €{prijs}")
                elif bandje == "Rood":
                    print("Sorry je mag geen alcohol bestellen onder de 21")
                    print(f"probeer het in {21- leeftijd} jaar nog een keer")
                else:
                    print("Sorry alleen VIPS mogen champagne bestellen")
                    

        else:
            print("Sorry geen idee wat u bedoeld, hier een glaasje water")

    if num == 5:
        if bandje == "Rood" or bandje == "Blauw":
            print(f"Alsjeblieft complimenten van het huis")
        else:
            print(f"Alstublieft u {Drankje} dat is dan €{prijs}")

    



Vraag(1)