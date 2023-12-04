import collections
import itertools
import functools
import re


data = []


def parse_input(input):
    cards = []
    for line in input.splitlines():
        card_num = int(line.split(":")[0].split(" ")[-1])
        lhs = [int(x.strip()) for x in line.split(":")[-1].split("|")[0].split(" ") if x.strip()]
        rhs = [int(x.strip()) for x in line.split(":")[-1].split("|")[1].split(" ") if x.strip()]
        cards.append((card_num,lhs,rhs))
    return cards

total = 0

with open("day4.txt") as f:
    data = parse_input(f.read().strip())


cards = {c: (lhs, rhs) for c, lhs, rhs in data}

resolved_cards = {}
while len(resolved_cards) < len(cards):
    for c,(lhs,rhs) in cards.items():
        if c in resolved_cards:
            continue
        matches = [c+x+1 for x in range(len([1 for n in rhs if n in lhs]))]
        if not matches:
            resolved_cards[c] = 1
        elif all(m in resolved_cards for m in matches):
            resolved_cards[c] = 1+sum(resolved_cards[m] for m in matches)


print(sum(resolved_cards[c] for c in cards))