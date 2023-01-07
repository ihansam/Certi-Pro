import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
ip = sys.stdin.readline

C, R = map(int, ip().split())
m = [list(ip().rstrip()) for _ in range(R)]
sc, sr = map(int, ip().split())
d = ((0, 1), (1, 0), (-1, 0), (0, -1))
q = deque()
q.append((sr-1, sc-1))
m[sr-1][sc-1] = 3

while q:
    r, c = q.popleft()
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if (0 <= nr < R) and (0 <= nc < C) and m[nr][nc] == '1':
            q.append((nr, nc))
            m[nr][nc] = m[r][c] + 1

mx, nd = 0, 0
for l in m:
    for c in l:
        if c == '1':
            nd += 1
        elif c == '0':
            continue
        else:
            mx = max(mx, c)

print(f"{mx}\n{nd}")

