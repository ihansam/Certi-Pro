# 재귀가 많이 일어나는 지금 방법은 매우 비효율적임!
import sys
sys.stdin = open('input.txt')
inp = sys.stdin.readline

A = [list(map(int, inp().split())) for _ in range(9)]
row = [[0]*10 for _ in range(9)]    # row[x][i] = 1/0
col = [[0]*10 for _ in range(9)]    # col[y][i] = 1/0
sub = [[0]*10 for _ in range(9)]    # sub[z][i] = 1/0 , z=(x//3)*3+(y//3)

for i in range(9):
    for j in range(9):
        num = A[i][j]
        if num:
            row[i][num] = 1
            col[j][num] = 1
            sub[i//3*3+j//3][num] = 1


def dfs(c):
    if c >= 81:
        for i in range(9):
            print(*A[i])
        return 1
    x, y = c//9, c % 9
    z = x//3*3 + y//3
    if A[x][y]:
        if dfs(c+1):
            return 1
    else:
        for i in range(1, 10):
            if row[x][i] or col[y][i] or sub[z][i]:
                continue
            A[x][y] = i
            row[x][i], col[y][i], sub[z][i] = 1, 1, 1
            if dfs(c+1):
                return 1
            else:
                A[x][y] = 0
                row[x][i], col[y][i], sub[z][i] = 0, 0, 0
        return 0


dfs(0)
