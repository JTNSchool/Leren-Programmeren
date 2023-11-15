aantal = 0
while True:
    aantal += 1
    a = input("? ").lower()
    if a == "quit":
        print(f"je hebt {aantal} vragen beantwoord")
        break