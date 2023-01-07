import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')
inp = sys.stdin.readline


def push_pq(num):
    heappush(min_pq, num)
    heappush(max_pq, -num)


for T in range(int(inp())):
    num_list = set()
    min_pq = []
    max_pq = []

    for Q in range(int(inp())):
        q = inp().split()
        cmd, arg = q[0], list(map(int, q[1:]))
        x = arg[0]
        if cmd == 'insert':
            if x not in num_list:
                num_list.add(x)
                push_pq(x)
        elif cmd == 'erase':
            if x in num_list:           # Lazy Update
                num_list.remove(x)
        elif cmd == 'update':
            y = arg[1]
            if (x in num_list) and (y not in num_list):
                num_list.remove(x)
                num_list.add(y)
                push_pq(y)
        elif not num_list:
            print("empty")
        else:
            if cmd == 'front':
                pq = min_pq
            else:
                pq = max_pq
            valid = []
            while len(valid) < x and pq:
                item = heappop(pq)
                if abs(item) in num_list:
                    if valid and valid[-1] == item:     # 항상 중복된 유효한 값이 pq에 들어올 수 있음에 유의!
                        continue
                    valid.append(item)
            print(abs(valid[-1]))
            for item in valid:
                heappush(pq, item)
