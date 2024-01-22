# Een hoofdletter mag niet op de twee middelste posities staan.
# De speciale tekens mogen niet op de eerste of laatste positie staan.
# Op de eerste 3 posities mag geen cijfer staan.

import random

CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = CAPS.lower()
SPECIAL = "@#$%&_?"
NUMBERS = "0123456789"

SPECIALCHARS = 3
AmountCijfers = random.randint(4, 7)
AmountHoofdLetter = random.randint(2, 6)
AmountLetter = 8 + (7-AmountCijfers) + (6-AmountHoofdLetter)


CurrentPassword = []

for i in range(SPECIALCHARS):
   CurrentPassword.append(random.choice(SPECIAL))
for i in range(AmountCijfers):
   CurrentPassword.append(random.choice(NUMBERS))
for i in range(AmountHoofdLetter):
   CurrentPassword.append(random.choice(CAPS))
for i in range(AmountLetter):
   CurrentPassword.append(random.choice(LOWER))

Poging = 0
while True:
    Poging += 1
    random.shuffle(CurrentPassword)
    if CurrentPassword[11] not in CAPS and CurrentPassword[12] not in CAPS and CurrentPassword[0] not in SPECIAL and CurrentPassword[23] not in SPECIAL:
        good = 0
        for i in range(3):
            if CurrentPassword[i] not in NUMBERS:
                good += 1
        if good == 3:
            WWstring = ""
            for symbol in CurrentPassword:
                WWstring = WWstring + symbol
            print(Poging, WWstring)
            break