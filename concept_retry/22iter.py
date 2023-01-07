import sys
from itertools import permutations as p, product as P, combinations_with_replacement as h
# from itertools import permutations, combinations, product, combinations_with_replacement

ip = sys.stdin.readline
n, m = map(int, ip().split())
r = range(1, 7)

if m == 1:
    C = P(r, repeat=n)
elif m == 2:
    C = h(r, n)
else:
    C = p(r, n)

for c in C:
    print(*c)

# case = permutations(range(1, n+1), k)
# case = combinations(range(1, n+1), k)
# case = product(range(1, n+1), repeat=k)
# case = combinations_with_replacement(range(1, n+1), k)

# for c in case:
#     print(*c)
