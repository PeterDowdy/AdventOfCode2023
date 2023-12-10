import collections
import itertools
import functools
import re

def parse_input(input):
    return[[int(x) for x in y.split(' ')] for y in input.splitlines()]

with open("day9.txt") as f:
    series = parse_input(f.read())

def get_next(series):
    deltas = []
    current_induction = series
    while any(x!=0 for x in current_induction):
        deltas.append([current_induction[n]-current_induction[n-1] for n in range(1,len(current_induction))])
        current_induction = deltas[-1]
    
    addition = 0
    for d in deltas:
        addition += d[-1]
    
    return addition+series[-1]

extrapolated = [get_next(x) for x in series]
print(sum(extrapolated))