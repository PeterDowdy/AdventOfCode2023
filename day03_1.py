import collections
import itertools
import functools
import re


data = []


def parse_input(input):
    results = []
    this_number = ""
    this_coords = []
    lines = input.splitlines()
    for y in range(0,len(lines)):
        for x in range(0,len(lines[y])):
            c = lines[y][x]
            if c.isdigit():
                this_number += c
                this_coords += [(x,y)]
            elif this_number:
                results.append((int(this_number),this_coords))
                this_number =""
                this_coords = []
        if this_number:
            results.append((int(this_number),this_coords))
            this_number =""
            this_coords = []
    
    return lines,results



with open("day3.txt") as f:
    lines,data = parse_input(f.read().strip())

adj = []

for n,d in data:
    should_add = False
    for x,y in d:
        adjacent = [(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1)]
        for a_x,a_y in adjacent:
            try:
                if (not lines[a_y][a_x].isdigit()) and lines[a_y][a_x] != '.':
                    should_add = True
            except:
                ...
    if should_add:
        adj += [n]

print(sum(adj))
