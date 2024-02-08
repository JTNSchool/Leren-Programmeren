import sys, time, random   

antwoordlistJA=["ja","j"]
antwoordlistNEE=["nee","n"]
antwoordlistJANEE=antwoordlistJA + antwoordlistNEE
aantwoordlistAB=["a","b"]
antwoordlistABC=["a","b","c"]

#Maakt de print mooier
def delay_print(Tekst):
    for Letter in Tekst:
        sys.stdout.write(Letter)
        sys.stdout.flush()
        time.sleep(0.005)

#Schoont de terminal op
def clear_terminal():
    print("\033c", end="")

#Check of het antwoord op de vraag een van de goede antwoorden is
def StelVraag(Vraag, antwoordlist, Kies):
    while True:
        try:
            antwoord = input(delay_print(Vraag), "\n").lower()
            if antwoord not in antwoordlist:
                print(Kies)
            else:
                return antwoord
        except ValueError:
            print(Kies)

#Print als je wint
def WinScherm(Tekst):
    clear_terminal()
    delay_print(f'''{Tekst} \n
                        GEWONNEN!!!''')
#Print als je af gaat
def AfScherm(Tekst, VerliesTekst="JE HEBT VERLOREN."):
    clear_terminal()
    delay_print(f'''{Tekst} \n                     
                        {VerliesTekst}''')


#Stel de vraag functie
def Functievraag(nummer):
    clear_terminal()
    if nummer == 1:
        Vraag = "ga je via de steeg? ja/nee "
        antwoordlist = antwoordlistJANEE
        Kies = "kies uit ja/nee"
        antwoord = StelVraag(Vraag, antwoordlist, Kies)

        if antwoord in antwoordlistJA:
            Functievraag(2)
        elif antwoord in antwoordlistNEE:
            Functievraag(5)
            
    elif nummer == 2:
        Vraag = '''je loopt door de steeg heen en komt een zwerver tegen wat doe je?
                            a: je biedt hem wat geld aan.
                            b: je loopt door
                            voer a of b in '''
        antwoordlist = aantwoordlistAB
        Kies = "kies uit a/b"
        antwoord = StelVraag(Vraag, antwoordlist, Kies)

        if antwoord == "a":
            AfScherm("hij wordt erg boos en agressief omdat je hem als zwerver ziet en steekt je neer")
        elif antwoord == "b":
            Functievraag(3)

    elif nummer == 3:
        vraag = '''je komt aan de andere kant van de steeg uit. Je ziet je huis al maar de brug staat open wat doe je?
                        a: je sprint in het water en probeert naar de overkant te zwemmen?
                        b: je wacht tot  dat de brug weer beneden is
                        c: je gaat naar links om te zoeken voor een plek om om te lopen '''
        antwoordlist = antwoordlistABC
        kies = "kies uit a/b/c"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            AfScherm("Het water is veel te koud en je vriest dood")
        elif antwoord == "b":
            AfScherm("Je komt heel thuis aan maar je bent wel telaat en je vader is erg boos op je!", "JE HEBT VERLOREN MAAR JE BENT WEL HEEL THUIS")
        elif antwoord == "c":
            Functievraag(4)
    
    elif nummer == 4:
        vraag = '''Je ziet rechts je huis maar als je loopt kom je niet optijd thuis. Je ziet ook een fiets staan maar de eigenaar staat verderop?
                            a: Je gaat gewoon naar huis
                            b: Je probeert z'n fiets te stelen '''
        antwoordlist = aantwoordlistAB
        kies = "kies uit a/b"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            AfScherm("je komt heel thuis maar je komt telaat aan. Je vader is erg boos!", "JE HEBT VERLOREN MAAR JE BENT WEL HEEL THUIS")
        elif antwoord == "b":
            fietskans = random.randint(0, 10)
            time.sleep(1.5)
            if fietskans > 5:
                WinScherm("je hebt succesvol z'n fiets gestolen en komt optijd thuis.") 
            elif fietskans < 5:
                AfScherm("De eigenaar heeft het door, hij belt de politie en je wordt opgepakt.", "JE HEBT VERLOREN EN ZIT NU IN DE CELL")

    elif nummer == 5:
        vraag = '''je komt een kruispunt tegen ga je links of rechts? 
                a: rechts
                b: links '''
        antwoordlist = aantwoordlistAB
        kies = "kies uit a/b"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            WinScherm("je bent de juiste kant op gegaan en je komt veilig thuis aan.") 
        elif antwoord == "b":
            Functievraag(6)

    elif nummer == 6:
        vraag = '''je raakt verdwaald wat doe je?
                a: je probeert de weg terug te vinden.
                b: je loopt door '''
        antwoordlist = aantwoordlistAB
        kies = "kies uit a/b"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            Functievraag(7)
        elif antwoord == "b":
            Functievraag(9)

    elif nummer == 7:
        vraag = '''je vind de terug weg niet maar komt wel een schuur tegen wat nu?
                a: je gaat naar binnen
                b: je gaat niet naar binnen en loopt verder '''
        antwoordlist = aantwoordlistAB
        kies = "kies uit a/b"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            Functievraag(8)
        elif antwoord == "b":
            Functievraag(10)
        
    elif nummer == 8:
        vraag = '''binnen zie je een matras liggen.
                a: je gaat slapen.
                b: je gaat weer naar buiten '''
        antwoordlist = aantwoordlistAB
        kies = "kies uit a/b"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            AfScherm("je slaapt in het schuurtje en overleeft de nacht maar bent niet thuis gekomen ", "JE VADER IS ERG BEZORGT OMDAT JE NIET THUIS BENT GEKOMEN, VERLOREN.")   
        elif antwoord == "b":
            AfScherm("buiten zie je de zwerver aan komen rennen met een mes hij steekt je neer omdat je in zijn huis was binnen gegaan.", "JE BENT DOOD GEGAAN, VERLOREN.")
            
    elif nummer == 9:
        input(delay_print('''je loopt door en komt toevallig weer bij de bar uit en probeert vanaf daar weer naar huis te gaan.\n\n druk op enter om door te gaan'''))
        Functievraag(1)

    elif nummer == 10:
        vraag = '''je komt 1 van je minder betrouwbare vrienden tegen, hij vertelt je dat je de andere kant op moet gaan om thuis te komen. Vertrouw je hem?
                a: je vertrouwd hem en gaat de andere kant op.
                b: je vertrouwd hem niet en gaat niet de andere kant op maar je blijft dezelfde kant op gaan. '''
        antwoordlist = aantwoordlistAB
        kies = "kies uit a/b"
        antwoord = StelVraag(vraag, antwoordlist, kies)

        if antwoord == "a":
            WinScherm("hij vertelde de waarheid en je komt thuis.")        
        elif antwoord == "b":
            AfScherm("je bent de verkeerde kant op gegaan en kon je huis nooit vinden.", "JE VADER IS ERG BEZORGT OMDAT JE NIET THUIS BENT GEKOMEN, VERLOREN.")

#Start van het programma
clear_terminal()
input(delay_print('''Welkom bij mijn game. Het is winter en je ging gezellig een avondje uit met je vrienden je hebt goed wat drank op en je voelt je allemaal niet meer zo helder.
Aan de eind van de avond kijk je op je horloge en zie je dat al heel laat is je moet snel thuis komen anders is je vader boos. 
je doel is om optijd thuis zien te komen terwijl je dronken bent en niet meer goed weet waar je heen moet, ook zie je een steegje die waarschijnlijk sneller is... \n\n\n
                                                               klik enter om door te gaan '''))
#Stelt de eerste vraag
Functievraag(1)