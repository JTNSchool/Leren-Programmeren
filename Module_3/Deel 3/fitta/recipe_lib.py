import math

UNIT_PIECES = 'piece'
UNIT_SPOONS = 'spoon'
UNIT_TEASPOONS = 'teaspoon'
UNIT_CUPS = 'cup'

TXT_PIECES = '|'
TXT_SPOONS = 'eetlepel|eetlepels'
TXT_TEASPOONS = 'theelepel|theelepels'
TXT_CUPS = 'kopje|kopjes'

# failsafe input of a number of persons
def input_nr_persons(prompt: str) -> int:
  while True:
    try:
      nr_persons = int(input(prompt))
      if nr_persons > 0: 
        return nr_persons
      print('getal moet groter zijn dan 0')
    except:
      print('voer een geldig geheel getal in!')


def round_piece(amount: float) -> int:
  if (amount - round(amount)) > 0:
    return round(amount) + 1
  else:
    return round(amount)

# returns amount rounded to the closest decimals: .00 or .25 or .50 or 0.75 unless amount >= 10
def round_quarter(amount: float) -> float:
  print(amount)
  if amount >= 10:
    return round(amount)
  else:
    return round(amount * 4 + 0.001) / 4

# returns single or plural description of a string 'single desciption|plural description' 
# depending on amount
def str_single_plural(amount: float, txt: str) -> str:
  ChoiceList = txt.split(TXT_PIECES)
  if len(ChoiceList) > 1:
    if amount > 1:
      return ChoiceList[1]
    else:
      return ChoiceList[0]
  else:
    return txt


# returns description of single or plural units
def str_units(amount: float, unit: str) -> str:
  ChoiceList = unit.split(TXT_PIECES)
  if len(ChoiceList) > 1:
    if amount > 1:
      return ChoiceList[1]
    else:
      return ChoiceList[0]
  else:
    return unit


# returns amount in string with 1/4 or 1/2 or 3/4
TXT_FRACTIONS = ('','¼','½','¾')
def str_amount_fraction(amount: float) -> str:  
  amount = round_quarter(amount)
  ints = int(amount)
  quarter = int((amount - ints) / 0.25)
  str_ints = str(ints) if ints > 0 else ''
  return str_ints + TXT_FRACTIONS[quarter]


# units in ml
ML_SPOON = 15 # one spoon contains 15 ml
ML_TEASPOON = 5 # one teaspoon contains 5 ml
ML_CUP = 240 # one cup contains 240 ml

def unit2ml(amount: float, unit: str) -> float:
  if unit == TXT_CUPS:
    value = ML_CUP * amount
  elif unit == TXT_TEASPOONS:
    value = ML_TEASPOON * amount
  elif unit == TXT_SPOONS:
    value = ML_SPOON * amount
  if value - round(value) == 0:
    return round(value)
  return value

# average densities in gram per ml for common ingredients, to calculate weight(gram) from milliliters(ml)
# 1ml of salt weighs 1.2 gram 
GRAM_PER_ML_SALT = 1.2
GRAM_PER_ML_PEPPER = 0.3
GRAM_PER_ML_CHEESE = 0.45
GRAM_PER_ML_SPINACH = 0.15

# returns amount in gram for amount in milliliter based on density (weight per volume)
def ml2gram(amount_ml: float, gram_per_ml: float) -> float:
  Antw = amount_ml * gram_per_ml
  if Antw >= 100 or Antw - round(Antw) == 0:
    return round(amount_ml * gram_per_ml)
  else:
    return round(amount_ml * gram_per_ml, 1)

