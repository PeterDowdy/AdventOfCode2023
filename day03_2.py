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

parts_and_gears = {}

for n,d in data:
    should_add = False
    for x,y in d:
        adjacent = [(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1)]
        for a_x,a_y in adjacent:
            try:
                if lines[a_y][a_x] == '*':
                    if (a_x,a_y) not in parts_and_gears:
                        parts_and_gears[(a_x,a_y)] = []
                    parts_and_gears[(a_x,a_y)].append(n)
            except:
                ...

gear_ratios = 0

for k,v in parts_and_gears.items():
    if len(set(v)) > 1:
        v_l = list(set(v))
        gear_ratios += v_l[0]*v_l[1]

print(gear_ratios)
