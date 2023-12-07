LatestGetal = 50
TotalCount = 0
lijst = []

while TotalCount < 1000:
    TotalCount += LatestGetal
    lijst.append(LatestGetal)
    txt = ""
    for getal in lijst:
        txt = txt + str(getal) + " "
        if getal != LatestGetal:
           txt = txt + "+ "
    txt = txt + "= " + str(TotalCount)

    LatestGetal += 1
    print(txt)