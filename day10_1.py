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

print(max([len(l)-1,len(r)-1]))