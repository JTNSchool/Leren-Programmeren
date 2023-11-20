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
for i in range(7):
    print(f"Kaart {i}: {AlleKaarten[0]}")
    AlleKaarten.pop(0)

print(f"Deck ({len(AlleKaarten)} kaarten): {AlleKaarten}")