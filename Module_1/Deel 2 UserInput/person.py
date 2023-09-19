# Maak een programma person.py dat de gebruiker om zijn naam, adres, postcode en woonplaats vraagt met duidelijke prompts.

# Laat het programma daarna een adreskaart (met lijntjes) tonen in de terminal:

#  ----------------------------------------------------
# |  Naam      : Fabian van Zandt                
# |  Adres     : Koekenbakkersplein 23           
# |  Postcode  : 2834 EF                         
# |  Woonplaats: Houten                          
#  ----------------------------------------------------

# Test het programma grondig. Maak daarvan screenshots.

# Commmit en push person.py

# Lever hier het programma + screenshot in.



naam = input("Wat is je voor en achternaam? ")
straat = input("Welke straat woon je? ")
Huisnummer = int(input("Welk huisnummer woon je? "))
Postcode = input("Wat is je postcode? ")
WoonPlaats = input("In welke stad/dorp woon je? ")


print("----------------------------------------------------")
print(f"|  Naam      : {naam}")
print(f"|  Adres     : {straat} {Huisnummer}")
print(f"|  Postcode  : {Postcode}")
print(f"|  Woonplaats: {WoonPlaats}")
print("----------------------------------------------------")