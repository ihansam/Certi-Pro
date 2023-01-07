import sys
from collections import defaultdict

sys.stdin = open('input.txt')
ip = sys.stdin.readline

p = [-1]
c = defaultdict(set)


def is_sibling(a, node):
    while node:
        if a == node:
            return 1
        node = p[node]
    return 0


def ga(node):
    if not node:
        return 0
    return 1 + ga(p[node])


def gb(node):
    if not c[node]:
        return 0
    ret = 0
    for chd in c[node]:
        ret = max(ret, 1 + gb(chd))
    return ret


for _ in range(int(ip())):
    q = ip().split()
    cmd, x = q[0], int(q[1])
    if cmd == 'add':
        y = int(q[2])
        p.append(y)
        c[y].add(x)
    elif cmd == 'remove':
        if x >= len(p) or p[x] < 0:
            continue
        for child in c[x]:
            p[child] = p[x]
            c[p[x]].add(child)
        c[p[x]].remove(x)
        c[x].clear()
        p[x] = -2
    elif cmd == 'move':
        y = int(q[2])
        if x >= len(p) or y >= len(p) or p[x] < 0 or p[y] == -2 or is_sibling(x, y):
            continue
        c[p[x]].remove(x)
        p[x] = y
        c[y].add(x)
    else:
        print(ga(x), gb(x))
    # print(q)
    #     print(p)
    #     print(c)
