import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')
inp = sys.stdin.readline

maxpq, minpq, abspq = [], [], []

for _ in range(int(inp())):
    x = int(inp())
    if not x:
        if minpq:
            print(-heappop(maxpq), heappop(minpq), heappop(abspq)[1])
        else:
            print(-1)
    else:
        heappush(minpq, x)
        heappush(maxpq, -x)
        heappush(abspq, (abs(x), x))    # 튜플을 넣을 수도 있다
