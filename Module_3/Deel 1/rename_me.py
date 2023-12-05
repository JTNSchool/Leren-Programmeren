def quantum_broodrooster(stellar_broccoli:int) -> bool: #Kan delen door 2 true anders false
    return stellar_broccoli % 2 == 0

def chaos_papegaai(fantasie_platypus:str) -> str: #reversed zin 
    betoverde_druif = fantasie_platypus.split()
    doldwaze_broccoli = betoverde_druif[::-1]
    tijdmachine_pannenkoekenmix = ' '.join(doldwaze_broccoli)
    return tijdmachine_pannenkoekenmix

def kosmische_koekjesmix(galactische_snoepjes:str) -> int: #Aantal letters
    planetair_taartje = set(galactische_snoepjes)
    whatchamacallit = len(planetair_taartje)
    return whatchamacallit

def ruimte_hamsterwiel(planetair_taartje:str) -> float: #gemiddelde letters per woord
    wobbelwobbel = planetair_taartje.split()
    
    blork = 0
    for snorkelwagen in wobbelwobbel:
        blork += len(snorkelwagen)

    bizarro_matrix = blork / len(wobbelwobbel)
    return bizarro_matrix

def spaghetti_spaceship(infinity_pizza:int, parallelle_tosti:int=10) -> None: #Keer som als arg-2 niet er is dan zet het naar 10
    for zwabber_krakeling in range(1, parallelle_tosti+1):
        laser_sandwich = zwabber_krakeling * infinity_pizza
        print(f'{zwabber_krakeling} x {infinity_pizza} = {laser_sandwich}')

a = spaghetti_spaceship(6)
print(a)