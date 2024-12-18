import sys, os
sys.path.append(os.path.abspath(".."))
from utils import solve
from collections import Counter

def get_lists(lines):
    l1, l2 = [], []
    for line in lines:
        a, b = line.split()
        l1.append(int(a))
        l2.append(int(b))

    return l1, l2

def f1(lines):
    l1, l2 = get_lists(lines)
    l1.sort()
    l2.sort()
    total = 0
    for i in range(len(l1)):
        total += abs(l1[i]-l2[i])

    print(total)

def f2(lines):
    l1, l2 = get_lists(lines)
    count = Counter(l2)
    total = 0
    for x in l1:
        total += x * count[x]

    print(total)

solve(f1, f2)
