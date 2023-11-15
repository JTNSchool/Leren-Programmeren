latestGetal = 50
TotalCount = 0
loop = 0
txt = ""
while TotalCount < 1000:
    loop += 1
    latestGetal += 1
    TotalCount += latestGetal
    if TotalCount < 1000:
        txt = txt + f"{latestGetal} + "
    else:
        txt = txt + f"{latestGetal}"
    msg = f"{loop}. {txt} = {TotalCount}"
    print(msg)
print("1K reached")