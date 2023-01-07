import sys
from itertools import product as p
ip = sys.stdin.readline
n, m = map(int, ip().split())
C = p(range(1, 7), repeat=n)
for c in C:
    if sum(c) == m:
        print(*c)