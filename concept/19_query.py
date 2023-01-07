import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')
inp = sys.stdin.readline

info = [0] * 100001
minpq, maxpq = [], []


def get_3(pq):
    valid = []
    while pq and len(valid) < 3:
        score, _id = heappop(pq)
        if abs(score) != info[abs(_id)]:
            continue
        if valid and valid[-1][1] == _id:
            continue
        valid.append((score, _id))
    if len(valid) == 3:
        print(abs(valid[2][1]))
    else:
        print(-1)
    for v in valid:
        heappush(pq, v)


for _ in range(int(inp())):
    query = list(map(int, inp().split()))
    cmd = query[0]
    if cmd == 1:
        _id, score = query[1:]
        heappush(minpq, (score, _id))
        heappush(maxpq, (-score, -_id))
        info[_id] = score
    elif cmd == 2:
        info[query[1]] = 0
    elif cmd == 3:
        get_3(minpq)
    else:
        get_3(maxpq)
