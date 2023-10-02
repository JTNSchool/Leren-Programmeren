# Je gaat een app maken die advies geeft aan SD studenten.

# De app legt de gebruiker 7 stellingen voor. 
# De gebruiker moet per stelling antwoorden hoeveel dat geldt voor hem/haar. 
# Er kan geantwoord worden met een van de opties: 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit. 
# Bij elke te beantwoorden stelling worden die opties nog eens getoond.

# De app telt de antwoorden op in een score. 
# Hoe hoger de score, hoe beter het gaat met de student. 
# Als alle stellingen worden beantwoord met een 4 dan wordt de score van 7 antwoorden: 28. 
# Als alle stellingen worden beantwoord met een 0 dan wordt de score: 0.

# Als gemiddelde score gelijk aan 2 of lager:
#   Advies is 'zorgelijk'
# Anders-als gemiddelde score gelijk aan 3 of lager:
#   Advies is 'twijfelachtig'
# Anders:
#   Advies is 'geruststellend'

# Opdracht A
# Je gaat de app maken met gebruik van de teksten in studieadviestext.py. 
#Je moet zoveel mogelijk teksten gebruiken. De stellingen staan er ook, gelukkig maar!


STUDIEDOKTER_TITEL = '''
*********************** STUDIEADVIES ***********************
Ik ga jou helpen met jouw opleiding. Jij krijgt een aantal stellingen te zien.
Voor elke stelling moet je zeggen hoeveel dat bij jou voorkomt. Je kunt steeds 
antwoorden: 0 is 'altijd'; 1 is 'vaak'; 2 is 'regelmatig'; 3 is 'soms'; 4 is 'nooit'.
Het is belangrijk om eerlijk te zijn. Op basis van jouw antwoorden krijg je advies. 
'''
OPTIES = "Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit"
# punten geven voor vragen en dan advies geven
AANTAL_WEKEN_VRAAG = 'Hoeveel weken ben je al bezig met de opleiding?'
COMPETENTIE_STELLING_1 = 'Ik voel stress of blokkades bij het maken van programmeeropdrachten.'
COMPETENTIE_STELLING_2 = 'Ik stel programmeeropdrachten en -uitdagingen uit.'
COMPETENTIE_STELLING_3 = 'Ik denk dat ik geen talent heb voor de opleiding.'
COMPETENTIE_STELLING_4 = 'Ik vermijd assessments (CJV) en feedback van kritische docenten. '
COMPETENTIE_STELLING_5 = 'Ik vergelijk mezelf met anderen die beter lijken te zijn.'
COMPETENTIE_STELLING_6 = 'Ik voel geen interesse in nieuwe programmeertechnieken.'
COMPETENTIE_STELLING_7 = 'Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.'

COMPETENTIE_ADVIES_TITEL = '''
*********************** STUDIEADVIES ***********************'''
COMPETENTIE_ADVIES_ZORGELIJK = '''
Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart 
in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad 
op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.
'''
COMPETENTIE_ADVIES_TWIJFELACHTIG = '''
Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart
in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!
'''
COMPETENTIE_ADVIES_GERUSTSTELLEND = '''
Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in
het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!
'''


antwoorden = []

def addToCount(amount):
    ant_0 = 0
    ant_1 = 0
    ant_2 = 0
    antwoorden.append(stelling_1)
    antwoorden.append(stelling_2)
    antwoorden.append(stelling_3)
    antwoorden.append(stelling_4)
    antwoorden.append(stelling_5)
    if amount == 7:
        antwoorden.append(stelling_6)
        antwoorden.append(stelling_7)
    for int in antwoorden:
        if int == 0:
            ant_0 += 1
        if int == 1:
            ant_1 += 1
        if int == 2:
            ant_2 += 1
    return [ant_0, ant_1, ant_2]


print(STUDIEDOKTER_TITEL)
aantalWeken = int(input(AANTAL_WEKEN_VRAAG))
print()
print(OPTIES)
stelling_1 = int(input(COMPETENTIE_STELLING_1))
print()
print(OPTIES)
stelling_2 = int(input(COMPETENTIE_STELLING_2))
print()
print(OPTIES)
stelling_3 = int(input(COMPETENTIE_STELLING_3))
print()
print(OPTIES)
stelling_4 = int(input(COMPETENTIE_STELLING_4))
print()
print(OPTIES)
stelling_5 = int(input(COMPETENTIE_STELLING_5))
if aantalWeken >= 10:
    vragen = 7
    print()
    print(OPTIES)
    stelling_6 = int(input(COMPETENTIE_STELLING_6))
    print()
    print(OPTIES)
    stelling_7 = int(input(COMPETENTIE_STELLING_7))
else:
    vragen = 5

if vragen == 5:
    gemiddelde = (stelling_1 + stelling_2 + stelling_3 + stelling_4 + stelling_5) / 5
if vragen == 7:
    gemiddelde = (stelling_1 + stelling_2 + stelling_3 + stelling_4 + stelling_5 + stelling_6 + stelling_7) / 7
antlist = addToCount(vragen)
ant_0 = antlist[0]
ant_1 = antlist[1]
ant_2 = antlist[2]

if gemiddelde <= 2 or (ant_0 + ant_1 > round(vragen / 2)):
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif gemiddelde <= 3 or (ant_0 + ant_1 + ant_2 > round(vragen / 2)):
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)



# Opdracht C Uitbreiding van de app
# De app gaat voor het advies ook kijken hoevaak de gebruiker bepaalde antwoorden geeft. Zo kan de app beter beoordelen welk advies geschikt is.
# De app moet het aantal antwoorden 'altijd' tellen, het aantal antwoorden 'vaak' tellen en het aantal antwoorden 'regelmatig' tellen.

# Het verbeterde advies werkt alsvolgt:
# Als gemiddelde score gelijk aan 2 of lager OF
# meer dan de helft van de vragen is beantwoord met 'altijd' of 'vaak' :
# Advies is 'zorgelijk'

# Anders Als gemiddelde score gelijk aan 3 of lager OF
# meer dan de helft van de vragen is beantwoord met 'altijd', 'vaak' of 'regelmatig'
# Advies is 'twijfelachtig'
# Anders:
# Advies is 'geruststellend'