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

def serialize_map():
    buf = ""
    
    for y in range(min_y, max_y+1):
        for x in range(min_x,max_x+1):
            buf += rocks[(x,y)]
        buf += "\n"
    return buf

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

def tilt_south():
    movement = True
    while movement:
        movement = False
        for k in sorted(rocks.keys(), key=lambda x: (x[1],x[0]),reverse=True):
            v = rocks[k]
            if v != 'O':
                continue
            x,y = k
            down = (x,y+1)
            if down not in rocks:
                continue
            if rocks[down] == '.':
                rocks[down] = 'O'
                rocks[k] = '.'
                movement = True


def tilt_east():
    movement = True
    while movement:
        movement = False
        for k in sorted(rocks.keys()):
            v = rocks[k]
            if v != 'O':
                continue
            x,y = k
            east = (x+1,y)
            if east not in rocks:
                continue
            if rocks[east] == '.':
                rocks[east] = 'O'
                rocks[k] = '.'
                movement = True


def tilt_west():
    movement = True
    while movement:
        movement = False
        for k in sorted(rocks.keys(),reverse=True):
            v = rocks[k]
            if v != 'O':
                continue
            x,y = k
            west = (x-1,y)
            if west not in rocks:
                continue
            if rocks[west] == '.':
                rocks[west] = 'O'
                rocks[k] = '.'
                movement = True

cycle = 0
transitions = {}
moves = [(0,serialize_map())]
while cycle < 1000000000:
    if cycle % 100000 == 0:
        print(cycle/1000000000)
    s_m = serialize_map()
    tilt_north()
    tilt_west()
    tilt_south()
    tilt_east()
    cycle += 1
    if any(x == serialize_map() for _,x in moves):
        cycle_gap = cycle-[n for n,x in moves if x == serialize_map()][0]
        cycle += cycle_gap*((1000000000-cycle)//cycle_gap)
    else:
        moves.append((cycle,serialize_map()))
print(serialize_map())

total_score = 0
cur_score = max_y+1
for n in range(min_y,max_y+1):
    total_score += cur_score*len([1 for k,v in rocks.items() if k[1] == n and v == 'O'])
    cur_score -= 1

print(total_score)