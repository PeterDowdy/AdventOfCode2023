import collections
import itertools
import functools
import re

def parse_input(input):
    lines = input.splitlines()
    instruction_set = lines[0]
    routes = {}
    for l in lines[2:]:
        if len(l) < 2:
            continue
        src,dst = l.split(" = ")
        routes[src] = dst.replace('(','').replace(')','').split(', ')
    return instruction_set,routes

with open("day8.txt") as f:
    instruction_set, routes = parse_input(f.read())

cur = 'AAA'
num_steps = 0
inst_cycle = itertools.cycle(instruction_set)
while cur != 'ZZZ':
    num_steps += 1
    cur = routes[cur][0 if next(inst_cycle) == 'L' else 1]

print(num_steps)