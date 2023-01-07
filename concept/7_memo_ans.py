import sys
from collections import deque

sys.stdin = open('input.txt')
inp = sys.stdin.readline

n, m, q = map(int, inp().split())

db = [deque() for _ in range(n)]
cnt = 0
cur = 0

for char in inp().strip():
    db[cnt//m].append(char)
    cnt += 1

for _ in range(q):
    query = inp().split()
    if query[0] == 'insert':
        r, c = cur // m, cur % m
        db[r].insert(c, query[1])
        while len(db[r]) > m:
            db[r+1].appendleft(db[r].pop())
            r += 1
        cur += 1
        cnt += 1
    elif query[0] == 'erase':
        if not cur:
            continue
        cur -= 1
        cnt -= 1
        r, c = cur // m, cur % m
        del db[r][c]
        while db[r+1]:
            db[r].append(db[r+1].popleft())
            r += 1
    else:
        r, c = map(int, query[1:])
        cur = min(cnt, r * m + c)
        print('*' if cur == cnt else db[r][c])
