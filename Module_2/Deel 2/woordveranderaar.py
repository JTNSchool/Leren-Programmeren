# Het maakt dan bijvoorbeeld van dit stukje tekst:

# In het hart van de grot zagen ze Draganthor, met zijn glinsterende schubben en vurige ogen. 
# De draak brulde en spuwde een vlammenzee die hen bedreigde, maar Rurik beschermde hen met een krachtig schild van magie.

# Dit stukje tekst:

# Bij de ingang van de grot zagen ze Draganthor, met zijn glinsterende teennagels en waterende ogen. 
# De geit brulde en spuwde een golf van water die hen bedreigde, maar Rurik beschermde hen met een krachtig zwemvliezen van plastic.

# Het programma vraagt eerst om een stukje tekst en vervolgens geeft deze de hertaling terug.
# Je verzint zelf minimaal 5 woorden die hertaalt moeten worden, 
# Je kan chatGPT gebruiken om je stukjes tekst te genereren om je hertaal machine te testen.
import time

txt = input("Vertel een verhaal: \n").split(" ")

Worden = {
    "jij": "u",
    "terwijl": "tijdens",
    "accu": "batterij",
    "vlug": "snel",
    "blij": "vrolijk"
}

for word in txt:
    if word in Worden:
        a = Worden[word]
    else:
        a = word
    print(a, end=' ', flush=True)

#Op een blije dag bracht jij met een vlugge tred, een nieuwe accu naar een dorp. Zonder vertraging installeerde je het, bracht licht en vreugde, terwijl het dorp een feest vierde.
