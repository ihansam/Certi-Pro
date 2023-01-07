import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

n = int(inp())
arr = [0] * n


def is_bad(len):
    for i in range(1, len//2+1):
        if arr[len-i:len] == arr[len-2*i:len-i]:
            return 1
    return 0


def dfs(x):
    if x >= n:
        print(*arr, sep='')
        return 1
    for i in range(1, 4):
        arr[x] = i
        if is_bad(x+1):
            continue
        if dfs(x+1):
            return 1
    return 0


dfs(0)
