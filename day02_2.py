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

power = 0

ctr = 0
for g in data:
    ctr += 1
    valid = True
    mins = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for round in g:
        for k in round:
            if round[k] > mins[k]:
                mins[k] = round[k]
    power += mins['red']*mins['green']*mins['blue']

print([power])