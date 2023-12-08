from collections import Counter
from functools import cmp_to_key

def evaluate_hand(hand):
    counts = Counter(hand).most_common(2)
    count_values = [count[1] for count in counts]
    return (
        7 if count_values[0] == 5 else 
        6 if count_values[0] == 4 else
        5 if count_values == [3, 2] else 
        4 if count_values[0] == 3 else
        3 if count_values == [2, 2] else
        2 if count_values[0] == 2 else
        1
    )

def compare_hands(h1, h2):
    ordering = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}
    t1, t2 = evaluate_hand(h1[0]), evaluate_hand(h2[0])
    return -1 if t1 < t2 else 1 if t1 > t2 else \
           next((ordering[c1] - ordering[c2] for c1, c2 in zip(h1[0], h2[0]) if ordering[c1] != ordering[c2]), 0)

with open("day7.txt") as file:
    lines = file.read().splitlines()

hands = [tuple(line.split()) for line in lines]
hands.sort(key=cmp_to_key(compare_hands))

total_score = sum((i + 1) * int(hand[1]) for i, hand in enumerate(hands))
print(total_score)
