import sys
ip = sys.stdin.readline
n = int(ip())
res = [0] * n


def is_bad(l):
    for i in range(1, l//2+1):
        if res[l-2*i:l-i] == res[l-i:l]:
            return 1
    return 0


def dfs(d):
    if d == n:
        print(*res, sep='')
        return 1
    for i in range(1, 4):
        res[d] = i
        if is_bad(d+1):
            continue
        if dfs(d+1):
            return 1
    return 0


dfs(0)
