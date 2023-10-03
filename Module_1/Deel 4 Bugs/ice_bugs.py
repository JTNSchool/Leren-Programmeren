def convertToEuroText(amount):
    txt = f"€{(amount)}".replace(".", ",")
    return txt

SMALL_PRICE = 1.25
MEDIUM_PRICE = 2.10

amount = input(f'Hoeveel ijsjes van {convertToEuroText(SMALL_PRICE)} wil je bestellen? ')
amount = input(f'En hoeveel ijsjes van {convertToEuroText(MEDIUM_PRICE)} wil je bestellen? ')
totalPrice = int(amount * SMALL_PRICE) + int(amount * MEDIUM_PRICE)

print(f'Dat is dan {totalPrice} totaal'.format(convertToEuroText(totalPrice)))