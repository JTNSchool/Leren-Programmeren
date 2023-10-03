import random

#selecteer 2 random nummers
num1 = random.randint(1,10)
num2 = random.randint(5,15)

#vraag om een antwoord
number = input(f'Weet jij wat {num1} + {num2} is? ') 

#geef reactie op het antwoord
try:
    number = int(number)

    if number == num1 + num2:
        print('Dat is juist')
    else:
        print('Nee dat klopt niet')
except ValueError:
    print('Dat is geen nummer!')

