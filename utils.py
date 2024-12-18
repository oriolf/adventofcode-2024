import sys

def solve(f1, f2):
    n = sys.argv[1]
    lines = [s.strip() for s in sys.stdin]
    if n == "1":
        f1(lines)
    else:
        f2(lines)
