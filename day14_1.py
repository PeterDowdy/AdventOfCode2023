import collections
import itertools
import functools
import re

def parse_input(input):
    rocks = {}
    lines = input.splitlines()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            rocks[(x,y)] = lines[y][x]
    return rocks

with open("day14.txt") as f:
    rocks = parse_input(f.read())
min_x,max_x,min_y,max_y = min(x for x,_ in rocks), max(x for x,_ in rocks), min(y for _,y in rocks), max(y for _,y in rocks)

def print_map():
    buf = ""
    
    for y in range(min_y, max_y+1):
        for x in range(min_x,max_x+1):
            buf += rocks[(x,y)]
        buf += "\n"
    print(buf)

def tilt_north():
    movement = True
    while movement:
        movement = False
        for k in sorted(rocks.keys(), key=lambda x: (x[1],x[0])):
            v = rocks[k]
            if v != 'O':
                continue
            x,y = k
            up = (x,y-1)
            if up not in rocks:
                continue
            if rocks[up] == '.':
                rocks[up] = 'O'
                rocks[k] = '.'
                movement = True

tilt_north()
print_map()

total_score = 0
cur_score = max_y+1
for n in range(min_y,max_y+1):
    total_score += cur_score*len([1 for k,v in rocks.items() if k[1] == n and v == 'O'])
    cur_score -= 1

print(total_score)