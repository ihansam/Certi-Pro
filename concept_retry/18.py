import sys
from heapq import heappush, heappop
from collections import defaultdict

sys.stdin = open('input.txt', 'r')
inp = sys.stdin.readline

min_pq = []
max_pq = []
db = defaultdict(int)


def make_tofu(worth, cnt):
    heappush(min_pq, worth)
    heappush(max_pq, -worth)
    db[worth] += cnt
    print(db[worth])


def crush_tofu(worth, cnt):
    db[worth] -= min(cnt, db[worth])
    print(db[worth])


def cell_tofu(flag, cnt):
    pq = max_pq if flag else min_pq
    total_worth = 0
    while cnt and pq:
        worth = heappop(pq) * (-1 if flag else 1)
        if not db[worth]:
            continue
        cell = min(cnt, db[worth])
        db[worth] -= cell
        if db[worth]:       # 남았으면 힙에 다시 넣어줘야
            heappush(pq, worth * (-1 if flag else 1))
        cnt -= cell
        total_worth += cell * worth
    print(total_worth)


for _ in range(int(inp())):
    cmd, arg1, arg2 = map(int, inp().split())
    if cmd == 1:
        make_tofu(arg1, arg2)
    elif cmd == 2:
        crush_tofu(arg1, arg2)
    else:
        cell_tofu(arg1, arg2)
