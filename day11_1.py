import collections
import itertools
import functools
import re

def parse_input(input):
    galaxies = {}
    galaxy_ctr = 0
    cells = {}
    lines = input.splitlines()
    buf = ""
    for l in lines:
        if all(x == '.' for x in l):
            buf += "\n".join([l,l]) + "\n"
        else:
            buf += l + "\n"

    lines = buf.strip().splitlines()

    cur = 0
    while True:
        if cur >= len(lines[0]):
            break
        if all(l[cur] == '.' for l in lines):
            lines = [l[:cur]+'.'+l[cur:] for l in lines]
            cur += 1
        cur += 1


    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                galaxy_ctr += 1
                galaxies[galaxy_ctr] = (x,y)
            cells[(x,y)] = lines[y][x]
    return cells, galaxies

with open("day11.txt") as f:
    cells, galaxies = parse_input(f.read())

def print_grid(grid):
    min_x,min_y=0,0
    max_x,max_y=max(x for x,_ in grid),max(y for _,y in grid)
    buf = ""
    for y in range(min_y,max_y+1):
        for x in range(min_x,max_x+1):
            buf += grid[(x,y)]
        buf += "\n"
    print(buf)


shortest_paths = 0
paths = set()
for k in galaxies.values():
    for k_ in galaxies.values():
        if k==k_:
            continue
        if (k_,k) in paths:
            continue
        x,y=k
        x_,y_=k_
        dist = abs(y_-y)+abs(x_-x)
        shortest_paths+=dist
        paths.add((k,k_))

print(shortest_paths)
