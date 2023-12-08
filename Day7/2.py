from collections import Counter
from functools import cmp_to_key

def type(hand):
    counter = Counter(hand)
    joker_count = counter.pop('J', 0)
    lst = counter.most_common(2)
    counts = [count + (joker_count if i == 0 else 0) for i, (card, count) in enumerate(lst)]
    return (
        7 if len(lst) <= 1 or counts[0] == 5 else
        6 if counts[0] == 4 else
        5 if counts == [3, 2] else
        4 if counts[0] == 3 else
        3 if counts == [2, 2] else
        2 if counts[0] == 2 else
        1
    )

def card_order(card):
    ordering = {card: i for i, card in enumerate('J23456789TQKA')}
    return ordering[card]

def compare_hands(h1, h2):
    t1, t2 = type(h1[0]), type(h2[0])
    return -1 if t1 < t2 else 1 if t1 > t2 else next((c1 - c2 for c1, c2 in zip(map(card_order, h1[0]), map(card_order, h2[0])) if c1 != c2), 0)

with open("day7.txt") as file:
    lines = [line.strip() for line in file]

hands = [tuple(line.split()) for line in lines]
hands.sort(key=cmp_to_key(compare_hands))

total_score = sum((i + 1) * int(hand[1]) for i, hand in enumerate(hands))
print(total_score)
