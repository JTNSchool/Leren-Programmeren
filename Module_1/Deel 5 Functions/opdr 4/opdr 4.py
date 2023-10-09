from test_lib import test, report

def GetalChecker(nr1, nr2):
    if nr1 > nr2:
        txt = f"Maximum: {nr1} en minimum: {nr2}"
    elif nr2 > nr1:
        txt = f"Maximum: {nr2} en minimum: {nr1}"
    else:
        txt = "Beide getallen zijn even groot"
    return txt


a = 5
b = 5

verwacht = "Beide getallen zijn even groot"
resultaat = GetalChecker(a, b)
test("Gelijk", verwacht, resultaat)

a = 5
b = 6

verwacht = f"Maximum: {b} en minimum: {a}"
resultaat = GetalChecker(a, b)
test("B groter", verwacht, resultaat)


a = 6
b = 5

verwacht = f"Maximum: {a} en minimum: {b}"
resultaat = GetalChecker(a, b)
test("A groter", verwacht, resultaat)


report()