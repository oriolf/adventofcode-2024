import sys, os
sys.path.append(os.path.abspath(".."))
from utils import solve

def f1(lines):
    print("1")
    print(lines)

def f2(lines):
    print("2")
    print(lines)

solve(f1, f2)
