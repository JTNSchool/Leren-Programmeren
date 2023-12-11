from functie import InfLoopTotStop

dict = InfLoopTotStop()
txt = ""
for persoon in dict:
    txt = txt + f"In {dict[persoon]['city']} woont de {dict[persoon]['Age']} jarige {dict[persoon]['Name']}\n"
print(txt)