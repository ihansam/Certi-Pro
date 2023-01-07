import sys
sys.stdin = open('input.txt')
ip = sys.stdin.readline

a = [list(map(int, ip().split())) for _ in range(9)]
z = []
ru = [[0] * 10 for _ in range(9)]
cu = [[0] * 10 for _ in range(9)]
bu = [[[0] * 10 for _ in range(3)] for _ in range(3)]

for i in range(9):
    for j in range(9):
        n = a[i][j]
        if n:
            ru[i][n], cu[j][n], bu[i//3][j//3][n] = 1, 1, 1
        else:
            z.append((i, j))


def dfs(d):
    if d == len(z):
        for l in a:
            print(*l)
        return 1
    r, c = z[d]
    for n in range(1, 10):
        if ru[r][n] or cu[c][n] or bu[r//3][c//3][n]:
            continue
        a[r][c] = n
        ru[r][n], cu[c][n], bu[r // 3][c // 3][n] = 1, 1, 1
        if dfs(d+1):
            return 1
        a[r][c] = 0
        ru[r][n], cu[c][n], bu[r // 3][c // 3][n] = 0, 0, 0
    return 0


dfs(0)
