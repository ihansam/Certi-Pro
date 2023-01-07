import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline
MAX = 10001


def is_parent(x, y):
    if x == 0:
        return 1
    while y:
        if y == x:
            return 1
        y = parent[y]
    return 0


def get_a(x):
    ret = 0
    while x:
        ret += 1
        x = parent[x]
    return ret


def get_b(x):
    ret = 0
    for y in child[x]:
        ret = max(ret, get_b(y) + 1)
    return ret


parent = [0] + [-1] * MAX
child = [set() for _ in range(MAX)]

for _ in range(int(inp())):
    qry = inp().split()
    cmd = qry[0]
    if cmd == 'add':
        x, y = map(int, qry[1:])
        parent[x] = y
        child[y].add(x)
    elif cmd == 'remove':
        x = int(qry[1])
        if x == 0 or parent[x] == -1:
            continue
        child[parent[x]] |= child[x]
        child[parent[x]].remove(x)
        for c in child[x]:
            parent[c] = parent[x]
        parent[x] = -1
    elif cmd == 'move':
        x, y = map(int, qry[1:])
        if parent[x] == -1 or parent[y] == -1 or x == y:
            continue
        if is_parent(x, y):
            continue
        child[parent[x]].remove(x)
        parent[x] = y
        child[y].add(x)
    else:
        x = int(qry[1])
        print(get_a(x), get_b(x))
