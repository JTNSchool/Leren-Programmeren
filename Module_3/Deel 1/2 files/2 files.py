from functie import InfLoopTotStop

dict = InfLoopTotStop()
txt = ""
for persoon in dict:
    txt = txt + f"{dict[persoon]['Name']}, die in {dict[persoon]['city']} woont, is {dict[persoon]['Age']} jaar\n"
print(txt)