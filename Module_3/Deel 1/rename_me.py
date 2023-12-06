def KanDelenDoorTwee(Getal:int) -> bool: #Kan delen door 2 true anders false
    return Getal % 2 == 0

def DraaiZinOm(Zin:str) -> str: #reversed zin 
    GesplitZin = Zin.split()
    ZinOmdraaier = GesplitZin[::-1]
    OmgeDraaidZin = ' '.join(ZinOmdraaier)
    return OmgeDraaidZin

def AantalLetters(Zin:str) -> int: #Aantal letters
    LetterLijst = set(Zin)
    AaatalLettersInZin = len(LetterLijst)
    return AaatalLettersInZin

def GemiddeldeLetters(Zin:str) -> float: #gemiddelde letters per woord
    GesplitteZin = Zin.split()
    Letters = 0
    for word in GesplitteZin:
        Letters += len(word)

    GemiddeldeLetterPerWoord = Letters / len(Zin)
    return GemiddeldeLetterPerWoord

def KeerSom(Getal1:int, Getal2:int=10) -> None: #Keer som als arg-2 niet er is dan zet het naar 10
    for Getal in range(1, Getal2+1):
        Antwoord = Getal * Getal1
        print(f'{Getal} x {Getal1} = {Antwoord}')