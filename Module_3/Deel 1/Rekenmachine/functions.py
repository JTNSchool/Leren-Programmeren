def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2



def RequestNumber():
    while True:
        antwoord = input("Vul een getal in: ").strip(" ")
        print(antwoord)
        try:
            antwoord = float(antwoord)
            return antwoord
        except ValueError:
            print("Dit is geen geldig antwoord")


def WhatToDo(choice, uitkomst):
    OldChoice = choice
    OldUitkomst = uitkomst
    if choice == None:
        txt = '''Wat wil je doen?
A) getallen optellen, 
B) getallen aftrekken, 
C) getallen vermenigvuldigen, 
D) getallen delen, 
E) getal ophogen, 
F) getal verlagen, 
G) getal verdubbelen,
H) getal halveren?
'''
        options =  ["a", "b", "c", "d", "e", "f", "g", "h"]
    else:
        txt = f'''Wil je wat met de uitkomst ({uitkomst}) doen?
A) getallen optellen, 
B) getallen aftrekken, 
C) getallen vermenigvuldigen, 
D) getallen delen, 
E) getal ophogen, 
F) getal verlagen, 
G) getal verdubbelen,
H) getal halveren?
I) niets?
'''
        options =  ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    
    choice = input(txt).lower()

    if choice in options:
        if choice == "a":
            if uitkomst == None:
                nr1 = RequestNumber()
            else:
                nr1 = uitkomst
            nr2 = RequestNumber()
            return choice, addition(nr1, nr2), f"{nr1} + {nr2} = {addition(nr1, nr2)}"
        
        elif choice == "b":
            if uitkomst == None:
                nr1 = RequestNumber()
            else:
                nr1 = uitkomst
            nr2 = RequestNumber()
            return choice, subtraction(nr1, nr2), f"{nr1} - {nr2} = {subtraction(nr1, nr2)}"

        elif choice == "c":
            if uitkomst == None:
                nr1 = RequestNumber()
            else:
                nr1 = uitkomst
            nr2 = RequestNumber()
            return choice, multiplication(nr1, nr2), f"{nr1} * {nr2} = {multiplication(nr1, nr2)}"
        
        elif choice == "d":
            if uitkomst == None:
                nr1 = RequestNumber()
            else:
                nr1 = uitkomst
            nr2 = RequestNumber()
            return choice, division(nr1, nr2), f"{nr1} / {nr2} = {division(nr1, nr2)}"
        
        elif choice == "e":
            if uitkomst == None:
                nr1 = RequestNumber()
            else:
                nr1 = uitkomst
            nr2 = 1
            return choice, addition(nr1, nr2), f"{nr1} + {nr2} = {addition(nr1, nr2)}"

        elif choice == "f":
            if uitkomst == None:
                nr1 = RequestNumber()
            else:
                nr1 = uitkomst
            nr2 = 1
            return choice, subtraction(nr1, nr2), f"{nr1} - {nr2} = {subtraction(nr1, nr2)}"
        
        elif choice == "g":
            if uitkomst == None:
                nr1 = RequestNumber()
            else:
                nr1 = uitkomst
            nr2 = 2
            return choice, multiplication(nr1, nr2), f"{nr1} * {nr2} = {multiplication(nr1, nr2)}"
        
        elif choice == "h":
            if uitkomst == None:
                nr1 = RequestNumber()
            else:
                nr1 = uitkomst
            nr2 = 2
            return choice, division(nr1, nr2), f"{nr1} / {nr2} = {division(nr1, nr2)}"
        
        elif choice == "i":
            return choice, uitkomst, f"Goodbye Laatste getal: {uitkomst}"
    else:
        return OldChoice, OldUitkomst, "Dit is geen keuze"