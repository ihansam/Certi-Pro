import sys
from collections import deque
sys.stdin = open('input.txt')
inp = sys.stdin.readline


q = int(inp())
cmds = [list(map(int, inp().split())) for _ in range(q)]

dq = deque()
arr = []

for l in cmds:
    if l[0] == 1:
        c, p, v = l
        if p:
            dq.append(v)
        else:
            dq.insert(0, v)
    elif l[0] == 2:
        c, p, v = l
        mx = 3
        if p:
            idx = len(dq) - 1
            while mx and idx >= 0:
                if dq[idx] >= v:
                    del dq[idx]
                    mx -= 1
                idx -= 1
        else:
            idx = 0
            while mx and idx < len(dq):
                if dq[idx] >= v:
                    del dq[idx]
                    mx -= 1
                else:
                    idx += 1
    elif l[0] == 3:
        v = l[1]
        dq = sorted(dq, key=lambda x: (abs(x-v), x))
    else:
        if l[1]:
            print(*reversed(dq))
        else:
            print(*dq)
