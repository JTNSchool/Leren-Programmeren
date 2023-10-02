# Maak van de gastheer variable in plaats van een boolean een input. Hierin vraag je de gebruiker de volgende vraag: “Wie is de gastheer?”.

# Breid nu je programma uit (dus niet een nieuw bestand) dat het ook nog werkt met de volgende stellingen:

# Als de naam van de gastheer het zelfde is als jouw naam, dan is er hoe dan ook een feest.
# Als de naam van de gastheer het zelfde is als jouw SLB-er dan is er hoe dan ook geen feest.
# Let op: Zorg er voor dat de punten uit de vorige opdracht ook werken, als je geen naam invult bij de vraag in je terminal dan betekend dit dat er geen gastheer is. 
# je mag geen nieuwe if’s aanmaken!


# Commit en push je programma naar github en lever een screenshot van je code in.

gastheer = input("Wie is de gastheer? ").lower()
allowed = ["jacco"]
blacklist = ["bouman", "wilfred"]
gasten = True
drank = True
chips = False

if ((gasten or gastheer in allowed) and ((gastheer in allowed and drank ) or (gasten and chips and drank ))) and gastheer not in blacklist:
    print('Start the Party')
else:
    print('No Party')
