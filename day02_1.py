import collections
import itertools
import functools


data = []


def parse_input(input):
    all_games = []
    for n in input.splitlines():
        g = []
        tok = n.split(": ")[-1]
        games = tok.split("; ")
        for game in games:
            parts = game.split(", ")
            g.append({k.split(" ")[1]:int(k.split(" ")[0]) for k in parts})
        all_games.append(g)
    return all_games
        


with open("day2.txt") as f:
    data = parse_input(f.read().strip())

pieces = {
    'red': 12,
    'green': 13,
    'blue': 14
}

possible = 0

ctr = 0
for g in data:
    ctr += 1
    valid = True
    for round in g:
        if any(pieces[k] < round[k] for k in ('red','green','blue') if k in round):
            valid = False
    if valid:
        possible += ctr

print(possible)