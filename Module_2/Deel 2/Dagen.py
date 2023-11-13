
Dagen = ("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag")

DagLijst = ""

for dag in Dagen:
    DagLijst = DagLijst + dag + ", "
print(f"Alle dagen van de week zijn: {DagLijst}")

DagLijst = ""
for i in range(5):  
    DagLijst = DagLijst + Dagen[i] + ", "
print(f"Alle werkdagen van de week zijn: {DagLijst}")

DagLijst = ""
for i in range(2):  
    DagLijst = DagLijst + Dagen[i + 5] + ", "
print(f"Alle weekenddagen van de week zijn: {DagLijst}")

DagLijst = ""
for i in range(7):  
    DagLijst = DagLijst + Dagen[6 - i] + ", "
print(f"Alle alle dagen reversed van de week zijn: {DagLijst}")

DagLijst = ""
for i in range(5):  
    DagLijst = DagLijst + Dagen[4 - i] + ", "
print(f"Alle weekdagen reversed van de week zijn: {DagLijst}")

DagLijst = ""
for i in range(2):  
    DagLijst = DagLijst + Dagen[6 -i] + ", "
print(f"Alle weekenddagen reversed van de week zijn: {DagLijst}")