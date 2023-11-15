clock = -1
txt = "AM"

while clock < 24:
    clock += 1
    if clock > 12:
        txt = "PM"
        tclock = clock - 12
    else:
        tclock = clock
    print(f"{tclock} {txt}")