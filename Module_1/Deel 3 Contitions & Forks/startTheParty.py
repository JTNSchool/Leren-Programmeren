# Maak op de plek van ??? in de if één if statement waarbij alle onderstaande stellingen kloppen.

# Alleen chips is geen feest.
# Een feest met chips, maar zonder drank kan niet beginnen.
# Een feest met gasten kan niet beginnen als er geen chips en geen drank is.

# Let op:  Zorg er voor dat je het goed test. Dit kun je doen door de variabelen op True en/of False te zetten, 
# dit doe je door bijvoorbeeld als je punt 1 wilt testen door gastheer, gasten en drank de waarde False te geven en chips de waarde True, 
# dan het programma “No Party” aan moeten geven.
# Commit en push je programma naar github en lever een screenshot van je code in.

#1 Een feest moet minimaal gasten of een gastheer hebben.

#1 Een gastheer kan een feest geven zonder chips en gasten, maar niet zonder drank.
#1 Het feest kan alleen beginnen als de gastheer er is, tenzij er gasten, chips en drank zijn.

gastheer = True
gasten = False
drank = True
chips = False

if (gasten == True or gastheer == True) and ((gastheer == True and drank == True) or (gasten == True and chips == True and drank == True)):
    print('Start the Party')
else:
    print('No Party')
