import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
ip = sys.stdin.readline

w, h = map(int, ip().split())
m = [list(ip().rstrip()) for _ in range(h)]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
res = 0


def bfs(r, c):
    ret = 0
    q = deque()
    q.append((r, c))
    m[i][j] = '.'
    while q:
        ret += 1
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if (0 <= nr < h) and (0 <= nc < w) and m[nr][nc] == '*':
                q.append((nr, nc))
                m[nr][nc] = '.'
    return ret


for i in range(h):
    for j in range(w):
        if m[i][j] == '.':
            continue
        res = max(bfs(i, j), res)


# def dfs(r, c):
#     m[r][c] = '.'
#     cnt = 0
#     for dr, dc in d:
#         nr, nc = r+dr, c+dc
#         if (0 <= nr < h) and (0 <= nc < w) and m[nr][nc] == '*':
#             cnt += dfs(nr, nc)
#     return cnt + 1
#
#
# for i in range(h):
#     for j in range(w):
#         if m[i][j] == '.':
#             continue
#         res = max(dfs(i, j), res)
#
print(res)
