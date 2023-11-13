for i in range(1, 25):
    time = None
    if i <= 12:
        time = "AM"
    else:
        time = "PM"
    print(f'{i} {time}')
