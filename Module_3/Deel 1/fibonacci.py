lijst = [0, 1]

def CreateNumber(i, list):
    return list[i] + list[i+1]

for i in range(20):
    lijst.append(CreateNumber(i, lijst))
    print(lijst)