def NaamEnLeeftijd(aantal):
    Name = input("Vul u naam in: ")
    WoonPlaats = input("Vu in Waar u woont: ")
    while True:
        Age = input("Vul u leeftijd in: ")
        try:
            Age = int(Age)
            break
        except ValueError:
            print(f"{Age} is not a integer")

    return {aantal: {"Name": Name, "Age": Age, "city": WoonPlaats}}

def InfLoopTotStop():
    dict = {}
    while True:
        dict.update(NaamEnLeeftijd(len(dict)))
        inp = input("Wil je nog een naam toe voegen? ").lower()
        if inp not in ("ja", "yes", "j", "y"):
            return dict
