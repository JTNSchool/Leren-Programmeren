import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import JOURNEY_IN_DAYS

#schrijf je test hier
test("Dagen check", 11, JOURNEY_IN_DAYS)
report()

if __name__ == "__main__":
    report()