import collections
import itertools
import functools
import re

def parse_input(input):
    return[[int(x) for x in y.split(' ')] for y in input.splitlines()]

with open("day9.txt") as f:
    series = parse_input(f.read())

def get_prev(series):
    deltas = []
    current_induction = series
    while any(x!=0 for x in current_induction):
        deltas.append([current_induction[n]-current_induction[n-1] for n in range(1,len(current_induction))])
        current_induction = deltas[-1]
    
    deltas = [series]+deltas

    deltas[-1] = [0]+deltas[-1]
    for n in range(len(deltas)-1,0,-1):
        deltas[n-1] = [deltas[n-1][0]-deltas[n][0]] + deltas[n-1]

    return deltas[0][0]

extrapolated = [get_prev(x) for x in series]
print(sum(extrapolated))