from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons("Voor hoeveel personen wilt u het recept? ") # replace this with better input

# ----- CALCULATIONS ----
# calculate factor 
Factor = nr_persons / 4
# calculate amount_eggs
Egg = round_piece(Factor * AMOUNT_EGGS)
# calculate amount_milk
Milk = (Factor * AMOUNT_MILK)
# calculate amount_salt
Salt = (Factor * AMOUNT_SALT)
# calculate amount_pepper
Pepper = (Factor * AMOUNT_PEPPER)
# calculate amount_oil
Oil = (Factor * AMOUNT_OIL)
# calculate amount_onions
Onion = round_piece(Factor * AMOUNT_ONIONS)
# calculate amount_garlics
Garlic = round_piece(Factor * AMOUNT_GARLICS)
# calculate amount_spinach
Spinach = (Factor * AMOUNT_SPINACH)
# calculate amount_paprikas
Paprika = round_piece(Factor * AMOUNT_PAPRIKAS)
# calculate amount_cheese
Cheese = (Factor * AMOUNT_CHEESE)
# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} {str_single_plural(nr_persons, TXT_PERSONS)}:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions

print(f'''
* {Egg} {str_single_plural(Egg, TXT_EGGS)} 
* {str_amount_fraction(Milk)} {str_units(Milk, TXT_CUPS)} {str_single_plural(Milk, TXT_MILK)} ({unit2ml(round_quarter(Milk), TXT_CUPS)} ml)
* {str_amount_fraction(Salt)} {str_units(Salt,TXT_TEASPOONS)} {str_single_plural(Salt, TXT_SALT)} ({ml2gram(unit2ml(round_quarter(Salt), TXT_TEASPOONS), GRAM_PER_ML_SALT)} gram)
* {str_amount_fraction(Pepper)} {str_units(Pepper,TXT_TEASPOONS)} {str_single_plural(Pepper, TXT_PEPPER)} ({ml2gram(unit2ml(round_quarter(Pepper), TXT_TEASPOONS), GRAM_PER_ML_PEPPER)} gram)
* {str_amount_fraction(Oil)} {str_units(Oil,TXT_SPOONS)} {str_single_plural(Oil, TXT_OIL)} ({unit2ml(round_quarter(Oil), TXT_SPOONS)} ml)
* {Onion} {str_single_plural(Onion, TXT_ONIONS)}
* {Garlic} {str_single_plural(Garlic, TXT_GARLICS)}
* {Paprika} {str_single_plural(Paprika, TXT_PAPRIKAS)}
* {str_amount_fraction(Spinach)} {str_units(Spinach,TXT_CUPS)} {str_single_plural(Spinach, TXT_SPINACH)} ({ml2gram(unit2ml(round_quarter(Spinach), TXT_CUPS), GRAM_PER_ML_SPINACH)} gram)
* {str_amount_fraction(Cheese)} {str_units(Cheese,TXT_CUPS)} {str_single_plural(Cheese, TXT_CHEESE)} ({ml2gram(unit2ml(round_quarter(Cheese), TXT_CUPS), GRAM_PER_ML_CHEESE)} gram)
''')
print('-----------------------------------------------')