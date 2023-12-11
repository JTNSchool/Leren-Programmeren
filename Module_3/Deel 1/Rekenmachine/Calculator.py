import functions

choice = None
uitkomst = None
Loop = True
while Loop:
    choice, uitkomst, txt = functions.WhatToDo(choice, uitkomst)
    print(txt, "\n")
    print("----------------------------------------------")
    if choice == "i":
        Loop = False