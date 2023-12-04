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

for c,lhs,rhs in data:
    score = 0
    for n in rhs:
        if n in lhs:
            score = score*2 if score else 1
    
    total += score

print(total)