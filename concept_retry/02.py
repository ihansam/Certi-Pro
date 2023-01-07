import sys
from heapq import nlargest

sys.stdin = open('input.txt', 'r')
inp = sys.stdin.readline

db = dict()

for _ in range(int(inp())):
    q = inp().split()
    cmd = q[0]
    if cmd == 'register':
        db[int(q[1])] = list(map(int, q[2:]))
    elif cmd == 'cancel':
        pid = int(q[1])
        if pid in db:
            del db[pid]
    elif cmd == 'update':
        pid, flag, x = map(int, q[1:])
        if pid in db:
            db[pid][flag+1] = x
    elif cmd == 'hire_min':
        target = min(db.items(), key=lambda x: (x[1][0], x[0]))[0]
        print(target)
        del db[target]
    else:
        # O(n * k)
        # for _ in range(3):
        #     target = max(db.items(), key=lambda x: (sum(x[1][1:]), x[0]))[0]
        #     print(target, end=' ')
        #     del db[target]

        # nlargest: O(k) 크기 공간에 원소를 n번 push/pop 해서 k 개의 최대 값을 뽑음
        # => O(n * log(k))
        target = nlargest(3, db.items(), key=lambda x: (sum(x[1][1:]), x[0]))
        for k, v in target:
            print(k, end=' ')
            del db[k]
        print()
