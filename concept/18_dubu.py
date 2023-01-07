import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')
inp = sys.stdin.readline


def cell(pq, count, is_max):
    value = 0
    cell_worth = 0
    while count and pq:
        cell_worth = -heappop(pq) if is_max else heappop(pq)
        dubu_count = db[cell_worth]
        if not dubu_count:
            continue
        cell_dubu_cnt = min(dubu_count, count)
        db[cell_worth] -= cell_dubu_cnt
        count -= cell_dubu_cnt
        value += cell_dubu_cnt * cell_worth
    print(value)
    if cell_worth and db[cell_worth]:
        heappush(pq, -cell_worth if is_max else cell_worth)


db = {}
minpq, maxpq = [], []

for _ in range(int(inp())):
    cmd, worth, cnt = list(map(int, inp().split()))
    if cmd == 1:
        if worth not in db:
            db[worth] = 0
        if not db[worth]:
            heappush(minpq, worth)
            heappush(maxpq, -worth)
        db[worth] += cnt
        print(db[worth])
    elif cmd == 2:
        if worth in db:
            db[worth] = max(0, db[worth] - cnt)
            print(db[worth])
        else:
            print(0)
    else:
        if worth:
            cell(maxpq, cnt, True)
        else:
            cell(minpq, cnt, False)
