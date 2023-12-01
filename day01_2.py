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
    buf = ""
    n = 0
    for n in range(len(r)):
        if r[n].isdigit():
            buf += r[n]
        else:
            for k, v in {
                "zero": "0",
                "one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": " 9",
            }.items():
                if r[n:].startswith(k):
                    buf += v
    first_num = next(iter([x for x in buf if x.isdigit()]))
    last_num = next(iter([x for x in buf[::-1] if x.isdigit()]))
    items.append(int(first_num + last_num))


print(sum(items))
