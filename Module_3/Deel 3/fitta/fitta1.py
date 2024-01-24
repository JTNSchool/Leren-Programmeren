from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons("Voor hoeveel {personen} wilt u het recept? ") # replace this with better input

# ----- CALCULATIONS ----
# calculate factor 
Factor = nr_persons / 4
# calculate amount_eggs
Egg = round_piece(Factor * AMOUNT_EGGS)
# calculate amount_milk
Milk = round_quarter(Factor * AMOUNT_MILK)
# calculate amount_salt
Salt = round_quarter(Factor * AMOUNT_SALT)
# calculate amount_pepper
Pepper = round_quarter(Factor * AMOUNT_PEPPER)
# calculate amount_oil
Oil = round_quarter(Factor * AMOUNT_OIL)
# calculate amount_onions
Onion = round_piece(Factor * AMOUNT_ONIONS)
# calculate amount_garlics
Garlic = round_piece(Factor * AMOUNT_GARLICS)
# calculate amount_spinach
Spinach = round_quarter(Factor * AMOUNT_SPINACH)
# calculate amount_paprikas
Paprika = round_piece(Factor * AMOUNT_PAPRIKAS)
# calculate amount_cheese
Cheese = round_quarter(Factor * AMOUNT_CHEESE)
# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} {TXT_PERSONS}:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions

print(f'''
* {Egg} {TXT_EGGS}
* {Milk} {TXT_MILK}
* {Salt} {TXT_SALT}
* {Pepper} {TXT_PEPPER}
* {Oil} {TXT_OIL}
* {Onion} {TXT_ONIONS}
* {Garlic} {TXT_GARLICS}
* {Paprika} {TXT_PAPRIKAS}
* {Spinach} {TXT_SPINACH}
* {Cheese} {TXT_CHEESE}
''')

print('-----------------------------------------------')