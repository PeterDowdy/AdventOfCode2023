import collections
import itertools
import functools
import re


data = []



def parse_input(input):
    lines = input.splitlines()
    
    times =[int(x.strip()) for x in lines[0].split(':')[-1].strip().split(' ') if x]
    distance =[int(x.strip()) for x in lines[1].split(':')[-1].strip().split(' ') if x]

    return [(x,y) for x,y in zip(times,distance)]

with open("day6_2.txt") as f:
    races = parse_input(f.read())

def does_it_win(time_accelerator,time,distance):
    return (time-(time_accelerator))*time_accelerator > distance

options = []

for t,d in races:
    start_ctr = 1
    end_ctr=t-1
    should_continue = True
    while should_continue:
        should_continue = False
        if not does_it_win(start_ctr,t,d):
            start_ctr += 1
            should_continue = True
        if not does_it_win(end_ctr,t,d):
            end_ctr -= 1
            should_continue = True
    options.append(1+end_ctr-start_ctr)

score = 1
for o in options:
    score *= o

print(score)
        