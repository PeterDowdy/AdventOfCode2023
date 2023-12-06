import collections
import itertools
import functools
import re


data = []


def get_token(lines, token):
    ctr = 0
    buf = []
    while not lines[ctr].startswith(token):
        ctr += 1
    ctr += 1
    while lines[ctr] and ctr < len(lines)-1:
        buf.append([int(x) for x in lines[ctr].split(" ")])
        ctr += 1
    
    return buf


def parse_input(input):
    lines = input.splitlines()
    seeds = [int(x) for x in lines[0].split(": ")[-1].split(" ")]
    a = get_token(lines, "seed-to-soil")
    b = get_token(lines, "soil-to-fertilizer")
    c = get_token(lines, "fertilizer-to-water")
    d = get_token(lines, "water-to-light")
    e = get_token(lines, "light-to-temperature")
    f = get_token(lines, "temperature-to-humidity")
    g = get_token(lines, "humidity-to-location")
    
    return seeds, a,b,c,d,e,f,g

with open("day5.txt") as f:
    seeds, seed_to_soil,soil_to_fertilizer,fertilizer_to_water,water_to_light,light_to_temperature,temperature_to_humidity,humidity_to_location = parse_input(f.read().strip())


def split_seed_range(s_s,s_r,s,r):
    if s_s+s_r <= s or s_s >= (s+r):
        return None, []
    new_start = max(s,s_s)
    new_end = min(s+r,s_s+s_r)
    splits = []
    match = ((new_start),new_end-new_start)
    if s_s < s and ((s_s+s_r) >= s):
        splits.append((s_s,s-s_s))
    if (s_s+s_r) > (s+r) and (s_s <= (s+r)):
        splits.append((s+r,(s_s+s_r)-(s+r)))
    return match, splits

seed_ranges = []
for n in range(0,len(seeds),2):
    seed_ranges.append((seeds[n],seeds[n+1]))

names = iter([ "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location"])

for map in seed_to_soil,soil_to_fertilizer,fertilizer_to_water,water_to_light,light_to_temperature,temperature_to_humidity,humidity_to_location:
    print(next(names))
    unprocessed = seed_ranges

    found = []
    while unprocessed:
        this_found = []
        s_s,s_r = unprocessed.pop(0)
        for d,s,r in map:
            match,splits = split_seed_range(s_s,s_r,s,r)
            if not match and not splits:
                continue
            this_found.append((d+match[0]-s,match[1]))
            unprocessed.extend(splits)
            break
        if not this_found:
            this_found.append((s_s,s_r))
        found.extend(this_found)
        
    seed_ranges = found

print(min(a for a,_ in seed_ranges))