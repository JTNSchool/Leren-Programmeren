import math
from test_lib import test, report

def calculate_cilinder_content(diameter, hoogte):
    Pi = math.pi
    Inhoud = (diameter/ 2) * (diameter/ 2) * Pi * hoogte
    return Inhoud

def Round_To_Number5(num, afrond):
    return round(num * 100 / afrond) * afrond / 100


AFROND = 5
Expect = 251.3
dia = float(8)
Hoogte = float(5)
test("1", Expect, round(calculate_cilinder_content(dia, Hoogte), 1))

Expect = 665.2
dia = float(11)
Hoogte = float(7)
test("1", Expect, round(calculate_cilinder_content(dia, Hoogte), 1))

Expect = 1781.3
dia = float(18)
Hoogte = float(7)
test("1", Expect, round(calculate_cilinder_content(dia, Hoogte), 1))

Expect = 353.4
dia = float(15)
Hoogte = float(2)
test("1", Expect, round(calculate_cilinder_content(dia, Hoogte), 1))

Expect = 0.0
dia = float(0)
Hoogte = float(6)
test("1", Expect, round(calculate_cilinder_content(dia, Hoogte), 1))
report()

print('''
      OPDRACHT 2
      ''')


Expect = 76.60
ant = Round_To_Number5(76.61, AFROND)
test("2", Expect, ant)

Expect = 28.80
ant = Round_To_Number5(28.82, AFROND)
test("2", Expect, ant)

Expect = 2.25
ant = Round_To_Number5(2.23, AFROND)
test("2", Expect, ant)

Expect = 31.05
ant = Round_To_Number5(31.06, AFROND)
test("2", Expect, ant)

Expect = 14.90
ant = Round_To_Number5(14.88, AFROND)
test("2", Expect, ant)

report()