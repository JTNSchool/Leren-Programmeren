def JAofNEE(vraag):
    antwoord = input(vraag + " ").lower()
    if antwoord in ["ja", "nee", "j", "n"]:
        return antwoord
    else:
        print("Error dus NEE")
        print()


if JAofNEE("Is de kaas geel?") == "ja":
    if JAofNEE("Zitten er gaten in?") == "ja":
        if JAofNEE("Is de kaasa belachelijk duur?") == "ja":
            KaasType = "Emmenthaler"
        else:
            KaasType = "Leerdammer"
    else:
        if JAofNEE("Is de kaas zo hard als steen?") == "ja":
            KaasType = "Parmigiano Reggiano"
        else:
            KaasType = "Goudse kaas"
else:
    if JAofNEE("Heeft de kaas blauwe schimmel") == "ja":
        if JAofNEE("Heeft de kaas korst?") == "ja":
            KaasType = "Blue de Rochbaron"
        else:
            KaasType = "Foume d'ambert"
    else:
        if JAofNEE("Heeft de kaas korst") == "ja":
            KaasType = "Camembert"
        else:
            KaasType = "Mozzerella"

print(f"Jou kaas is: {KaasType}")
