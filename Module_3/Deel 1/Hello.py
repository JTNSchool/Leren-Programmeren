def Greetingz(num):
    txt = ""
    for i in range(1, num+1):
        txt = txt + "Hello from function town " + str(i) + "!\n"
    return txt

print(Greetingz(int(input("Hoeveel Hellos wilt u? "))))