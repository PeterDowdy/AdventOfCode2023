import collections
import itertools
import functools


data = []


def parse_input(input):
    return [x.strip() for x in input.splitlines()]


with open("day1.txt") as f:
    data = parse_input(f.read().strip())

items = []
for r in data:
    first_num = next(iter([x for x in r if x.isdigit()]))
    last_num = next(iter([x for x in r[::-1] if x.isdigit()]))
    items.append(int(first_num + last_num))


print(sum(items))
