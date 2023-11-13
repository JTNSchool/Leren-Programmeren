def GetAwnser():
    while True:
        getal = input("Vul een getal in ")
        try:
            getal = int(getal)
            return getal
        except ValueError:
            print(f"{getal} is geen getal")




getal = GetAwnser()
for num in range(1, 11):
    print(f"{num} x {getal} = {num * getal}")
