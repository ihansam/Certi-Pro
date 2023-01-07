import sys
from collections import deque

sys.stdin = open('input.txt')
inp = sys.stdin.readline


col, row = map(int, inp().split())
arr = [[int(i) for i in inp().rstrip()] for _ in range(row)]
sy, sx = map(int, inp().split())
dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)

q = deque()
q.append((sx-1, sy-1))
arr[sx-1][sy-1] = 3

while q:
    x, y = q.popleft()
    time = arr[x][y]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < row and 0 <= ny < col and arr[nx][ny] == 1:
            q.append((nx, ny))
            arr[nx][ny] = time + 1

ans = -1
cnt = 0
for line in arr:
    for t in line:
        ans = max(ans, t)
        cnt += (t == 1)
print(ans)
print(cnt)
