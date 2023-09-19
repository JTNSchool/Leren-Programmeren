# Stel: je gaat met 3 vrienden (dus met zijn vieren) een dag naar de speelhal: ‘de Speelhal-dag’

# Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag.
# Jullie willen ook met zijn allen voor 45 minuten in de VIP-VR-GameSeat.
# De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten. Jij trakteert dus betaal je alles.

# Maak een programma speelhal.py voor deze berekening.


personen = 4
toegang = 7.45

VIPVR = 0.37
tijd = 45

print((personen * toegang) + (tijd / 5 * VIPVR * personen))