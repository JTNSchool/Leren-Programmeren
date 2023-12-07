from collections import Counter
import math, random

def CheckVoorArgs(getallen:list, controlegetal1:int, controlegetal2:int) -> dict:
    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}

    if not str(controlegetal1).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal1}

    if not str(controlegetal2).isnumeric():
        return {"Tweede controlle getal incorrect.":controlegetal2}

def AantalGetallen(getallen):
    return len(getallen)

def SomGetallen(getallen):
    return sum(getallen)

def gemiddelde(som, aantal):
    return som / aantal

def GrootsteGetal(getallen): 
    return max(getallen)
    
def KleinsteGetal(getallen): 
    return min(getallen)
    
def EersteGetal(getallen):
    return getallen[0]
    
def KleinDelen(kleinste_getal, controlegetal1):
    return kleinste_getal / controlegetal1

def GrootDelen(grootste_getal, controlegetal2):
    return grootste_getal / controlegetal2

def UniekGetalNaarAantalUniek(getallen):
    UniekList = list(set(getallen))
    UniekList = len(UniekList)
    return UniekList

def VerschilControleUniek(Uniek, controlegetal):
    return abs(Uniek - controlegetal)

def SorteerLijst(getallen):
    return sorted(getallen)

def SoorteerUniekLijst(getallen):
    unieke_getallen = list(set(getallen))
    return sorted(unieke_getallen)

def AantalUniek(getallen):
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer
        print("Dit kan fout gaan Line 58")
    return telling_elementen

def DeelbaarDoorControle(unieke_getallen, controlegetal1):
    deelbaar1 = []
    for getal in unieke_getallen:
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    return sorted(deelbaar1)

def KomtVoorInLijst(getallen, controlegetal1, controlegetal2):
    return controlegetal1 in getallen and controlegetal2 in getallen

def PositiesControlleGetal(getallen, controlegetal1):
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)
    return posities

def StandaardafwijkingBerekenen(getallen, gemiddelde, aantal):
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking

def RandomGetal(getallen, aantal):
    return getallen[random.randint(0,aantal-1)]

def VerschilRandomControle(random_getal, controlegetal2):
    return abs(random_getal - controlegetal2)

def CreateDictAlleVars(getallen, controlegetal1, controlegetal2):
    AlleVars = {}
    AlleVars.update({"aantal": AantalGetallen(getallen)})
    AlleVars.update({"som": SomGetallen(getallen)})
    AlleVars.update({"gemiddelde": gemiddelde(AlleVars['som'], AlleVars['aantal'])})
    AlleVars.update({"grootste_getal": GrootsteGetal(getallen)})
    AlleVars.update({"kleinste_getal": KleinsteGetal(getallen)})
    AlleVars.update({"delen1": KleinDelen(AlleVars['kleinste_getal'], controlegetal1)})
    AlleVars.update({"delen2": GrootDelen(AlleVars['grootste_getal'], controlegetal2)})
    AlleVars.update({"aantal_unieke_elementen": UniekGetalNaarAantalUniek(getallen)})
    AlleVars.update({"gesorteerde_lijst": SorteerLijst(getallen)})
    AlleVars.update({"gesorteerde_lijst_uniek": SoorteerUniekLijst(getallen)})
    AlleVars.update({"verschil1": VerschilControleUniek(AlleVars['aantal_unieke_elementen'], controlegetal1)})
    AlleVars.update({"verschil2": VerschilControleUniek(AlleVars['aantal_unieke_elementen'], controlegetal2)})

    AlleVars.update({"eerste_getal": EersteGetal(getallen)})
    AlleVars.update({"telling_elementen": SorteerLijst(getallen)})
    AlleVars.update({"deelbaar1": DeelbaarDoorControle(AlleVars['gesorteerde_lijst_uniek'], controlegetal1)})
    AlleVars.update({"deelbaar2": DeelbaarDoorControle(AlleVars['gesorteerde_lijst_uniek'], controlegetal2)})
    AlleVars.update({"komtvoor": KomtVoorInLijst(getallen, controlegetal1, controlegetal2)})
    AlleVars.update({"posities": PositiesControlleGetal(getallen, controlegetal1)})
    AlleVars.update({"standaardafwijking": StandaardafwijkingBerekenen(getallen, AlleVars['gemiddelde'], AlleVars['aantal'])})
    AlleVars.update({"getallen": 0})
    AlleVars.update({"random_getal": RandomGetal(getallen, AlleVars['aantal'])})
    AlleVars.update({"schudlijst": getallen})
    random.shuffle(AlleVars['schudlijst'])
    return AlleVars

def resultaten(getallenlijst, controlegetal1, controlegetal2):
    check = CheckVoorArgs(getallenlijst, controlegetal1, controlegetal2)
    AlleVars = CreateDictAlleVars(getallenlijst, controlegetal1, controlegetal2)
    resultaten = {
        "Aantal getallen": AlleVars['aantal'],
        "Gemiddelde": AlleVars['gemiddelde'],
        "Som": AlleVars['som'],
        "Grootste getal": AlleVars['grootste_getal'],
        "Kleinste getal": AlleVars['kleinste_getal'],
        "Eerste getal": AlleVars['eerste_getal'],
        f"{AlleVars['kleinste_getal']} / {controlegetal1}": AlleVars['delen1'],
        f"{AlleVars['grootste_getal']} / {controlegetal2}": AlleVars['delen2'],
        "Aantal unieke elementen": AlleVars['aantal_unieke_elementen'],
        f"Het verschil tussen {AlleVars['aantal_unieke_elementen']} & {controlegetal1}": AlleVars['verschil1'],
        "Gesorteerde lijst getallen": AlleVars['gesorteerde_lijst'],
        "Gesorteerde lijst unieke getallen": AlleVars['gesorteerde_lijst_uniek'],
        "Telling van elementen": AlleVars['telling_elementen'],
        f"Deelbaar door {controlegetal1} (op volgorde)": AlleVars['deelbaar1'],
        f"Deelbaar door {controlegetal2} (op volgorde)": AlleVars['deelbaar2'],
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": AlleVars['komtvoor'],
        f"{controlegetal1} komt voor op positie(s)": AlleVars['posities'],
        "Standaardafwijking": AlleVars['standaardafwijking'],
        "Geshufflede lijst": AlleVars['schudlijst'],
        "Willekeurige getal uit de lijst": AlleVars['random_getal'],
        f"Het verschil tussen {AlleVars['random_getal']} & {controlegetal2}": AlleVars['verschil2'],
    }

    return resultaten


# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = resultaten(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")