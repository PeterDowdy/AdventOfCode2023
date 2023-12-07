import collections
import itertools
import functools
import re


data = {}



def parse_input(input):
    hands = {}
    for l in input.splitlines():
        hands[l.split(' ')[0]] = int(l.split(' ')[1])
    return hands

with open("day7.txt") as f:
    data = parse_input(f.read())

hand_score = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}

def get_hand_power(hand):
    hand_ctr = collections.Counter(hand)
    if len(hand_ctr.keys()) == 1:
        return 6 # five of a kind
    if len(hand_ctr.keys()) == 2 and ( len([v for v in hand_ctr.values() if v == 4]) == 1):
        return 5 # four of a kind
    if len(hand_ctr.keys()) == 2 and ( len([v for v in hand_ctr.values() if v == 3]) == 1) and ( len([v for v in hand_ctr.values() if v == 2]) == 1):
        return 4 # full house
    if len(hand_ctr.keys()) == 3 and ( len([v for v in hand_ctr.values() if v == 3]) == 1) and ( len([v for v in hand_ctr.values() if v == 1]) == 2):
        return 3 #three of a kind
    if len(hand_ctr.keys()) == 3 and( len([v for v in hand_ctr.values() if v == 2]) == 2) and ( len([v for v in hand_ctr.values() if v == 1]) == 1):
        return 2 # two pair
    if len(hand_ctr.keys()) == 4 and ( len([v for v in hand_ctr.values() if v == 2]) == 1) and ( len([v for v in hand_ctr.values() if v == 1]) == 3):
        return 1 # one pair
    if len(hand_ctr.keys()) == 5:
        return 0 # one pair

def compare_hands(hand_a,hand_b):
    if get_hand_power(hand_a) > get_hand_power(hand_b):
        return hand_a
    if get_hand_power(hand_b) > get_hand_power(hand_a):
        return hand_b
    
    for n in range(0,5):
        if hand_score[hand_a[n]] > hand_score[hand_b[n]]:
            return hand_a
        
        if hand_score[hand_b[n]] > hand_score[hand_a[n]]:
            return hand_b
    
    raise Exception('wat')

sorted_hands = []
for h in data:
    stop = False
    score = get_hand_power(h)
    if not sorted_hands:
        sorted_hands.append((score,h))
    else:
        for n in range(0,len(sorted_hands)):
            if compare_hands(sorted_hands[n][1],h) == h:
                sorted_hands = sorted_hands[:n] + [(score,h)] + sorted_hands[n:]
                stop = True
                break
            
        if not stop:
            sorted_hands.append((score,h))

score = 0

rank = len(sorted_hands)
for n in sorted_hands:
    score += data[n[1]]*rank
    rank -= 1


print(score)