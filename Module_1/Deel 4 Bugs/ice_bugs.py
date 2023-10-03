def convertToEuroText(amount):
    txt = f"€{(amount)}".replace(".", ",")
    return txt

SMALL_PRICE = 1.25
MEDIUM_PRICE = 2.10

amount1 = int(input(f'Hoeveel ijsjes van {convertToEuroText(SMALL_PRICE)} wil je bestellen? '))
amount2 = int(input(f'En hoeveel ijsjes van {convertToEuroText(MEDIUM_PRICE)} wil je bestellen? '))
totalPrice = float(amount1 * SMALL_PRICE) + float(amount2 * MEDIUM_PRICE)

print(f'Dat is dan {convertToEuroText(totalPrice)} totaal')