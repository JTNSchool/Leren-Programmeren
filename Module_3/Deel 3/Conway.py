getal = "111221"
Streak = 0
LastCijfer = None
Newcijfer = ""

for cijfer in getal:
    if LastCijfer != cijfer:
        if LastCijfer != None:
            Newcijfer = str(Newcijfer) + str(Streak) + str(LastCijfer)
        Streak = 1
        LastCijfer = cijfer
    else:
        Streak += 1

Newcijfer = str(Newcijfer) + str(Streak) + str(cijfer)
getal = Newcijfer
print(getal)