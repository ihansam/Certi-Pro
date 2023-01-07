import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')
inp = sys.stdin.readline


def get_cth_element(pq, c):
    valid_numbers = []
    while len(valid_numbers) < c:
        num = heappop(pq)
        if abs(num) in valid:
            if valid_numbers and valid_numbers[-1] == num:
                continue
            valid_numbers.append(num)
    print(abs(valid_numbers[-1]))
    for num in valid_numbers:
        heappush(pq, num)


pq_max = []
pq_min = []
valid = set()

for T in range(int(inp())):
    pq_max.clear()
    pq_min.clear()
    valid.clear()
    for Q in range(int(inp())):
        query = inp().split()
        cmd = query[0]
        x = int(query[1])
        if cmd == 'insert':
            if x not in valid:
                valid.add(x)
                heappush(pq_max, -x)
                heappush(pq_min, x)
        elif cmd == 'erase':
            if x in valid:
                valid.remove(x)
        elif cmd == 'update':
            y = int(query[2])
            if y not in valid and x in valid:
                valid.remove(x)
                valid.add(y)
                heappush(pq_max, -y)
                heappush(pq_min, y)
        elif len(valid) == 0:
            print("empty")
        elif cmd == 'front':
            c = int(query[1])
            if c <= len(valid)/2:
                get_cth_element(pq_min, c)
            elif c >= len(valid):
                get_cth_element(pq_max, 1)
            else:
                get_cth_element(pq_max, len(valid)+1-c)
        else:
            c = int(query[1])
            if c <= len(valid)/2:
                get_cth_element(pq_max, c)
            elif c >= len(valid):
                get_cth_element(pq_min, 1)
            else:
                get_cth_element(pq_min, len(valid)+1-c)
