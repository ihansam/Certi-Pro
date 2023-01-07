import sys
from collections import deque

sys.stdin = open('input.txt')
inp = sys.stdin.readline

n, m, q = map(int, inp().split())
memo = [deque() for _ in range(n)]
cnt = 0
cursor = 0

for c in inp().rstrip():
    memo[cnt//m].append(c)
    cnt += 1

for _ in range(q):
    query = inp().rstrip().split()
    cmd = query[0]
    if cmd == 'insert':
        r, c = cursor // m, cursor % m
        memo[r].insert(c, query[1])
        while len(memo[r]) > m:
            memo[r+1].appendleft(memo[r].pop())
            r += 1
        cursor += 1
        cnt += 1
    elif cmd == 'erase':
        if not cursor:
            continue
        cursor -= 1
        cnt -= 1
        r, c = cursor // m, cursor % m
        del memo[r][c]
        while memo[r+1]:
            memo[r].append(memo[r+1].popleft())
            r += 1
    else:
        r, c = map(int, query[1:])
        cursor = min(cnt, r * m + c)
        print('*' if cursor == cnt else memo[r][c])
