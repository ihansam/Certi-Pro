import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

n, m = map(int, inp().split())
dice = [1] * (n+1)
visited = [0] * 7


def dfs(x):
    if x > n:
        print(*dice[1:])
        return
    for i in range(1 if m != 2 else dice[x-1], 7):
        if m == 3 and visited[i]:
            continue
        visited[i] = 1
        dice[x] = i
        dfs(x+1)
        visited[i] = 0


dfs(1)
