import collections
import itertools
import functools
import re

def parse_input(input):
    map = {}
    lines = input.splitlines()
    for y in range(0,len(lines)):
        for x in range(0,len(lines[y])):
            map[(x,y)]=lines[y][x]

    return map

with open("day10.txt") as f:
    pipes = parse_input(f.read())

start = [k for k,v in pipes.items() if v == 'S'][0]

left_path = [start]
right_path = [start]

def get_neighbours(pos):
    x,y = pos
    return [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]

def get_connection(start,finish):
    x,y = start
    if finish not in pipes:
        return False
    if (x-1,y) == finish and pipes[finish]in('-','F','L') and pipes[start] in ('-','7','J','S'):
        return True    
    if (x,y-1) == finish and pipes[finish] in ('|','F','7') and pipes[start] in ('|','J','L','S'):
        return True
    if (x+1,y) == finish and pipes[finish] in ('-','7','J') and pipes[start] in ('-','F','L','S'):
        return True
    if (x,y+1) == finish and pipes[finish] in ('|','J','L') and pipes[start] in ('|','F','7','S'):
        return True
    return False

def get_connections(pos, neighbours):
    return [n for n in neighbours if get_connection(pos,n)]

neighbours = get_neighbours(start)

connections = get_connections(start,neighbours)

l = [start,connections[0]]
r = [start,connections[1]]

while(True):
    this_l = l[-1]
    next_l = [x for x in get_connections(this_l,get_neighbours(this_l)) if x not in l and x not in r]
    this_r = r[-1]
    next_r = [x for x in get_connections(this_r,get_neighbours(this_r)) if x not in r and x not in l]
    if next_l:
        l += next_l
    if next_r:
        r += next_r
    if not next_l and not next_r:
        break

loop_tiles = l+r

min_x,min_y = (min([x for x,y in loop_tiles]),min([y for x,y in loop_tiles]))
max_x,max_y = (max([x for x,y in loop_tiles]),max([y for x,y in loop_tiles]))

candidates = []
bad = set()
good = []

for y in range(min_y,max_y):
    for x in range(min_x,max_x):
        if (x,y) not in loop_tiles:
            candidates.append({(x,y)})

while True:
    next_candidates = []
    for c in candidates:
        neighbours = set()
        for member in c:
            neighbours.update(set([x for x in get_neighbours(member) if x not in loop_tiles and x not in c and x in pipes]))
        c.update(neighbours)
        if any(x for x in get_neighbours(member) if x not in pipes):
            bad.update(c)
        elif any(x<min_x or x>max_x or y<min_y or y>max_y for x,y in c):
            bad.update(c)
        elif any(n in bad for n in c):
            bad.update(c)
        elif not neighbours:
            good.append(c)
        else:
            next_candidates.append(c)
    candidates = []
    for n_c in next_candidates:
        if n_c not in candidates:
            candidates.append(n_c)
    if not candidates:
        break

final_set = set()

for g in good:
    connects = True
    for s in g:
        if not all(x in loop_tiles or x in g for x in get_neighbours(s)):
            connects = False
            break
    if connects:
        final_set.update(g)

inside = set()

for s in sorted(final_set):
    out = True
    this_x, y = s
    last_turn = ''
    for x in range(min_x-1,max_x+1):
        if (x,y) not in pipes:
           continue
        if ((x,y) in loop_tiles and (pipes[(x,y)] == '|' or last_turn+pipes[(x,y)] in ('FJ','L7'))
            ):
            out = not out
            last_turn = ''
        elif (x,y) in loop_tiles and pipes[(x,y)] in 'FJL7':
            last_turn = pipes[(x,y)]
        elif (x,y) == (this_x,y):
            if not out:
                inside.add((x,y))
            break

print(len(inside))
