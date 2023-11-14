def GetAwnser(txt):
    while True:
        getal = input(txt)
        try:
            getal = int(getal)
            return getal
        except ValueError:
            print(f"{getal} is geen getal")


HVLlijst = GetAwnser("Hoeveel lijsten moeten er geshowed worden? ")
Legnte = GetAwnser("Hoelang moeten de lijsten zijn? ")


for i in range(HVLlijst + 1):
    lijst = list(range(Legnte))
    result = []
    for getal in lijst:
        getal = getal * i
        result.append(getal)
    print(result)

#----------------------

# def GetAwnser(txt):
#     while True:
#         getal = input(txt)
#         try: getal = int(getal); return getal
#         except ValueError: print(f"{getal} is geen getal")
# HVLlijst, Legnte = GetAwnser("Hoeveel lijsten moeten er geshowed worden? "), GetAwnser("Hoelang moeten de lijsten zijn? ")
# for i in range(HVLlijst + 1):
#     lijst, result = list(range(Legnte)), []
#     for getal in lijst: getal = getal * i; result.append(getal)
#     print(result)