import sys
from heapq import nlargest

sys.stdin = open('input.txt')
inp = sys.stdin.readline

d = {}

for _ in range(int(inp())):
    cmd = inp().split()
    q = cmd[0]
    param = list(map(int, cmd[1:]))
    if q == 'register':
        pid, sal, c, j, p = param
        d[pid] = [c, j, p, sal]
    elif q == 'cancel':
        if param[0] in d.keys():
            del d[param[0]]
    elif q == 'update':
        pid, idx, x = param
        if pid in d.keys():
            d[pid][idx] = x
    elif q == 'hire_min':
        pid = min(d.items(), key=lambda x: (x[1][3], x[0]))[0]
        print(pid)
        del d[pid]
    else:
        res = nlargest(3, d.items(), key=lambda x: (sum(x[1][:-1]), x[0]))
        for r in res:
            print(r[0], end=' ')
            del d[r[0]]
        print()
