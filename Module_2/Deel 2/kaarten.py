import random

kleuren = ("harten", "klaveren", "schoppen", "ruiten")
nummer = list(range(2, 11))
kaarten = nummer + ["boer", "vrouw", "heer", "aas"]
AlleKaarten = []

for kleur in kleuren:
    for kaart in kaarten:
        AlleKaarten.append(kleur + " " + str(kaart))
AlleKaarten.append("joker")
AlleKaarten.append("joker")

AlleKaarten = random.sample(AlleKaarten, len(AlleKaarten))
for i in range(1, 8):
    print(f"Kaart {i}: {AlleKaarten[i]}")
    AlleKaarten.pop(i)

print(f"Deck ({len(AlleKaarten)} kaarten): {AlleKaarten}")




#----- KORTER

# import random

# kleuren, nummer, AlleKaarten = ("harten", "klaveren", "schoppen", "ruiten"), list(range(2, 11)), []
# kaarten = nummer + ["boer", "vrouw", "heer", "aas"]

# for kleur in kleuren:
#     for kaart in kaarten: AlleKaarten.append(kleur + " " + str(kaart))
# AlleKaarten.append("joker"); AlleKaarten.append("joker"); AlleKaarten = random.sample(AlleKaarten, 54)

# for i in range(1, 8): print(f"Kaart {i}: {AlleKaarten[i]}"); AlleKaarten.pop(i)
# print(f"Deck (47 kaarten): {AlleKaarten}")