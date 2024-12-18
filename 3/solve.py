import sys, os
sys.path.append(os.path.abspath(".."))
from utils import solve

import re

def f1(lines):
    total = 0
    for line in lines:
        for m in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line):
            print(m)
            a, b = m
            total += int(a) * int(b)
    print(total)

def f2(lines):
    total = 0
    enabled = True
    for line in lines:
        for m in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\)|don't\(\))", line):
            a, b, do = m
            if do:
                if do == "do()":
                    enabled = True
                else:
                    enabled = False
            else:
                if enabled:
                    total += int(a) * int(b)
    print(total)

solve(f1, f2)
