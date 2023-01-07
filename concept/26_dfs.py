import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

w, h = map(int, inp().split())
arr = [list(inp().rstrip()) for _ in range(h)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def dfs(x, y):
    cnt = 1
    arr[x][y] = '.'
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<h and 0<=ny<w and arr[nx][ny] == '*':
            cnt += dfs(nx, ny)
    return cnt


ans = 0
for i in range(h):
    for j in range(w):
        if arr[i][j] == '*':
            ans = max(ans, dfs(i, j))
print(ans)
