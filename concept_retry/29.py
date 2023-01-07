import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt', 'r')
ip = sys.stdin.readline

n, k = map(int, ip().split())
code = [list(ip().rstrip()) for _ in range(n)]
s, e = map(int, ip().split())
s -= 1
e -= 1
g = defaultdict(list)
v = [-1] * n


def is_ham(s1, s2):
    ret = 0
    for c1, c2 in zip(code[s1], code[s2]):
        ret += (c1 != c2)
        if ret > 1:
            return 0
    return ret


for i in range(n):
    for j in range(i+1, n):
        if is_ham(i, j):
            g[i].append(j)
            g[j].append(i)

q = deque([s])
v[s] = s
while q:
    cur = q.popleft()
    for nxt in g[cur]:
        if v[nxt] != -1:
            continue
        v[nxt] = cur
        if nxt == e:
            q.clear()
        else:
            q.append(nxt)

if v[e] == -1:
    print(-1)
else:
    res = [e+1]
    cur = e
    while cur != v[cur]:
        cur = v[cur]
        res.append(cur+1)
    print(*reversed(res))
