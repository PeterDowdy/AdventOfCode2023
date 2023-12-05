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

def map_seed(seed, map):
    for d,s,r in map:
        if s <= seed and s + r >= seed:
            return d+(seed-s)
    return seed

mapped_seeds = []

for seed in seeds:
    seed_ctr = seed
    seed_ctr = map_seed(seed_ctr,seed_to_soil)
    seed_ctr = map_seed(seed_ctr,soil_to_fertilizer)
    seed_ctr = map_seed(seed_ctr,fertilizer_to_water)
    seed_ctr = map_seed(seed_ctr,water_to_light)
    seed_ctr = map_seed(seed_ctr,light_to_temperature)
    seed_ctr = map_seed(seed_ctr,temperature_to_humidity)
    seed_ctr = map_seed(seed_ctr,humidity_to_location)
    mapped_seeds.append(seed_ctr)

print(min(mapped_seeds))