import sys, os
sys.path.append(os.path.abspath(".."))
from utils import solve

def parse_line(line):
    return [int(x) for x in line.split()]

def get_input(lines):
    return [parse_line(line) for line in lines]

def report_safe(report):
    if report[-1] < report[0]:
        report.reverse()
    for i in range(len(report)-1):
        diff = report[i+1]-report[i]
        if diff < 1 or diff > 3:
            return 0
    return 1

def report_safe_2(report):
    if report_safe(report):
        return 1
    for i in range(len(report)):
        if report_safe(report[:i]+report[i+1:]):
            return 1
    return 0


def f1(lines):
    print(sum([report_safe(report) for report in get_input(lines)]))

def f2(lines):
    print(sum([report_safe_2(report) for report in get_input(lines)]))

solve(f1, f2)
