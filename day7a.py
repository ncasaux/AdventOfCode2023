import aocd


def calculate_ranking(h: str):
    ranked_hand = []
    card_occurrence = []
    for d in cards:
        card_occurrence.append(h.count(d))

    combination = []
    while sum(combination) < 5:
        combination.append(max(card_occurrence))
        card_occurrence.remove(max(card_occurrence))

    card_value = []
    for i in range(5):
        card_value.append(cards.index(h[i]))

    ranked_hand.append((combination, card_value, h))

    return ranked_hand


f = aocd.get_data(day=7, year=2023)
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
rankedHands = []

for currentLine in f.splitlines():
    hand, bid = currentLine.split()
    rankedHands.append((calculate_ranking(hand), int(bid)))

rankedHands.sort()

winning = 0
r: tuple
for index, r in enumerate(rankedHands, start=1):
    winning += index * r[1]

print(f"Total winning is {winning}.")
