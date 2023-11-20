boodschappen = {}


while True:
    boodschap = input("Wat wilt u toevoegen aan uw boodschappenlijst? ").lower()
    if boodschap in boodschappen:
        boodschappen[boodschap] += 1
    else:
        boodschappen.update({boodschap: 1})
    door = input("Wilt u meer toevoegen? ").lower()
    if door in ["nee", "n", "no"]:

        print("-----< Boodschappenlijst >-----")
        for i in boodschappen:
            print(f"{boodschappen[i]}x {i}")
        break