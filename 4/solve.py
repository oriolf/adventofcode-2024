import sys, os
sys.path.append(os.path.abspath(".."))
from utils import solve

def get_input(lines):
    return [list(line) for line in lines]

def move(m, i, j, l, direction):
    dx, dy = direction
    lst = []
    for n in range(l):
        nx = j+n*dx
        ny = i+n*dy
        if nx < 0 or ny < 0 or nx >= len(m[0]) or ny >= len(m):
            continue
        try:
            lst.append(m[ny][nx])
        except:
            pass
    return lst

def search_xmas(crossword, i, j):
    slices = [
        move(crossword, i, j, 4, (1, 0)),
        move(crossword, i, j, 4, (-1, 0)),
        move(crossword, i, j, 4, (0, 1)),
        move(crossword, i, j, 4, (0, -1)),
        move(crossword, i, j, 4, (1, 1)),
        move(crossword, i, j, 4, (1, -1)),
        move(crossword, i, j, 4, (-1, 1)),
        move(crossword, i, j, 4, (-1, -1)),
    ]
    count = 0
    for n, slc in enumerate(slices):
        if "".join(slc) == "XMAS":
            count += 1
    return count

def search_xmas_2(crossword, i, j):
    slices = [
        move(crossword, i-1, j-1, 3, (1, 1)),
        move(crossword, i+1, j-1, 3, (1, -1)),
    ]
    count = 0
    for n, slc in enumerate(slices):
        s = "".join(slc)
        if s != "MAS" and s != "SAM":
            return False
    return True
1
def f1(lines):
    crossword = get_input(lines)
    count = 0
    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            count += search_xmas(crossword, i, j)
    print(count)

def f2(lines):
    crossword = get_input(lines)
    count = 0
    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            if search_xmas_2(crossword, i, j):
                count += 1
    print(count)

solve(f1, f2)
