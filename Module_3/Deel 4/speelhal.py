from help import *

RECEIPT_TEXT = '***** SPEELHAL ENTREE VOOR {personen:2} PERSONEN *****'
RESTART_TEXT = '\nBestelprocedure gestopt door invoerfout!\nHerstart de bestelprocedure!'
MAX_TICKETS = 30
MAX_VR_VIP_SEAT_TIME = 45
VR_VIP_SEAT_PRICE_PERIOD = 5

TICKET_PRICE = 7.50
VR_VIP_SEAT_PERIOD_PRICE = 0.37
COLA_PRICE = 2.10
POPCORN_PRICE = 2.89
VAT_CODE_H = 'H'
VAT_CODE_L = 'L'

# ***************** INPUT *****************
print("SPEELHAL-ENTREE-KASSA")

# --> Vereenvoudig hier de code m.b.v. de help.py function: input_yes_no() (zie tip 1)
answer = input_yes_no("Wilt u bestellen?(J/N)\n")

# --> Vereenvoudig hier de conditie met de 'in'-operator (zie tip 2)
if answer in NO_OPTIONS:
  exit('Nu geen interesse? Tot ziens!')
else:
  print('Ik ga u nu vragen wat en hoeveel u wilt...')

# --> Vereenvoudig hier de code m.b.v. de help.py function: input_int() (zie tip 3)
nr_tickets = input_int("Hoeveel personen?\n")


# --> Vereenvoudig hier de code m.b.v. de help.py function: input_yes_no() (zie tip 1)
answer = input("Ook VR-VIP seats?(J/N)\n")
if not (answer == 'J' or answer == 'j' or answer == 'N' or answer == 'n'):
  print('Alleen een optie uit: J of j of N of n')
  exit()

# --> Vereenvoudig hier de conditie met de 'in'-operator (zie tip 2)
# --> Vereenvoudig vervolgens de code door de uitkomst van de conditie toe te kennen aan: vr_vip_ordered (tip 4)
if answer == 'J' or answer == 'j':
  vr_vip_ordered = True
else:
  vr_vip_ordered = False

# --> Vereenvoudig hier de conditie (zie tip 5)
if vr_vip_ordered == True:
  # --> Vereenvoudig hier de code m.b.v. de help.py function: input_int() (zie tip 3)
  try:
    min = 0
    max = nr_tickets
    answer = input("hoeveel VR-VIP seats?\n")
    nr_vr_vip_seats = int(answer)
    if nr_vr_vip_seats < min:
      print(f'Minimum is: {min}')
      exit(RESTART_TEXT)
    elif nr_vr_vip_seats > max:
      print(f'Maximum is: {max}')
      exit(RESTART_TEXT)
  except:
    print(f'Geen geldig getal: {answer}')
    exit(RESTART_TEXT)
  # --> Vereenvoudig hier de code m.b.v. de help.py function: input_int() (zie tip 3)
  try:
    min = 5
    max = MAX_VR_VIP_SEAT_TIME
    answer = input("hoeveel minuten in de VR-VIP-seats?\n")
    vr_vip_seat_time = int(answer)
    if vr_vip_seat_time < min:
      print(f'Minimum is: {min}')
      exit(RESTART_TEXT)
    elif vr_vip_seat_time:
      print(f'Maximum is:time > max: {max}')
      exit(RESTART_TEXT)
  except:
    print(f'Geen geldig getal: {answer}')
    exit(RESTART_TEXT)
else:
  nr_vr_vip_seats = 0
  vr_vip_seat_time = 0

# --> Vereenvoudig hier de code m.b.v. de help.py function: input_int() (zie tip 3)
try:
  min = 0
  max = nr_tickets
  answer = input("Hoeveel cola?\n")
  nr_cola = int(answer)
  if nr_cola < min:
    print(f'Minimum is: {min}')
    exit(RESTART_TEXT)
  elif nr_cola > max:
    print(f'Maximum is: {max}')
    exit(RESTART_TEXT)
except:
  print(f'Geen geldig getal: {answer}')
  exit(RESTART_TEXT)

# --> Vereenvoudig hier de code m.b.v. de help.py function: input_int() (zie tip 3)
try:
  min = 0
  max = nr_tickets
  answer = input("Hoeveel popcorn?\n")
  nr_popcorn = int(answer)
  if nr_cola < min:
    print(f'Minimum is: {min}')
    exit(RESTART_TEXT)
  elif nr_cola > max:
    print(f'Maximum is: {max}')
    exit(RESTART_TEXT)
except:
  print(f'Geen geldig getal: {answer}')
  exit(RESTART_TEXT)

# --> Vereenvoudig hier de code m.b.v. de help.py function: input_yes_no() (zie tip 1)
answer = input("Wilt u een factuur met BTW specificatie?(J/N)\n")
if not (answer == 'J' or answer == 'j' or answer == 'N' or answer == 'n'):
  print('Alleen een optie uit: J of j of N of n')
  exit(RESTART_TEXT)

# --> Vereenvoudig hier de conditie met de 'in'-operator (zie tip 2)
# --> Vereenvoudig vervolgens de code door de uitkomst van de conditie toe te kennen aan: vr_vip_ordered (tip 4)
if answer == 'J' or answer == 'j':
  vat_invoice = True
else:
  vat_invoice = False

# --> Vereenvoudig hier de conditie (zie tip 5)
if vat_invoice == True:
   company_name = input('Op welke bedrijfsnaam komt de factuur?\n').trim()
   if len(company_name) == 0:
     company_name = '........... (zelf invullen)'

# ***************** CALCULATION *****************
total_tickets = round(nr_tickets * TICKET_PRICE,2)
vr_vip_seat_price = vr_vip_seat_time / VR_VIP_SEAT_PRICE_PERIOD * VR_VIP_SEAT_PERIOD_PRICE
total_vr_vip_seats = round(nr_vr_vip_seats * vr_vip_seat_price, 2)
total_cola = round(nr_cola * COLA_PRICE, 2)
total_popcorn = round(nr_popcorn * POPCORN_PRICE, 2)
total_all = total_tickets + total_vr_vip_seats + total_cola + total_popcorn

# --> Vereenvoudig hier de conditie (zie tip 5)
if vat_invoice == True:
# --> Vereenvoudig hier de code met de help.py function: get_vat_from_amount_incl() (zie tip 6)
  vat_perc_H = 21 # voor VAT_CODE_H
  total_tickets_vat = round(total_tickets / (100 + vat_perc_H) * vat_perc_H, 2)
  total_vr_vip_seats_vat = round(total_vr_vip_seats / (100 + vat_perc_H) * vat_perc_H, 2)

  vat_perc_L = 9  # voor VAT_CODE_L
  total_cola_ex_vat = round(total_cola / (100 + vat_perc_H) * vat_perc_L, 2)
  total_popcorn_ex_vat = round(total_popcorn / (100 + vat_perc_H) * vat_perc_L, 2)

  total_vat_H = total_tickets_vat + total_vr_vip_seats_vat
  total_vat_L = total_cola_ex_vat + total_popcorn_ex_vat
  total_vat = total_vat_H + total_vat_L

# ***************** OUTPUT *****************
receipt_text = RECEIPT_TEXT.format(personen = nr_tickets)
print(receipt_text+'\n')
if vat_invoice:
  print(f'Factuur voor: {company_name}')
else:
  print(f'Kassabon')\
  
print('-'*len(receipt_text))
print(f'Tickets                   {nr_tickets:2} x {TICKET_PRICE:2.2f} = {total_tickets:6.2f}')
print(f'VR-vip-seats  {vr_vip_seat_time:3} minuten {nr_vr_vip_seats:2} x {vr_vip_seat_price:2.2f} = {total_vr_vip_seats:6.2f}')
print(f'Cola                      {nr_cola:2} x {COLA_PRICE:2.2f} = {total_cola:6.2f}')
print(f'Popcorn                   {nr_popcorn:2} x {POPCORN_PRICE:2.2f} = {total_popcorn:6.2f}')
print('.'*len(receipt_text))
print(f'Totaal:                               {total_all:6.2f}')

print()
# --> Verbeter hier de code met de help.py function: get_vat_perc() en gebruikmakend van de vat codes: VAT_CODE_H en VAT_CODE_L (zie tip 7)
if vat_invoice:
  print(f'BTW Hoog                          {vat_perc_H:2}% {total_vat_H:6.2f}')
  print(f'BTW Laag                          {vat_perc_L:2}% {total_vat_L:6.2f}')
print('='*len(receipt_text))
print('Bedankt voor de bestelling, veel plezier!')
# --> Verwijder na succesvolle testen alle refactor instructies uit de code