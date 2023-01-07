import sys
from queue import PriorityQueue

sys.stdin = open('input.txt')
inp = sys.stdin.readline


def get_cth_element(pq, c):
    valid_numbers = []
    while len(valid_numbers) < c:
        num = pq.get()
        if abs(num) in valid:
            if valid_numbers and valid_numbers[-1] == num:
                continue
            valid_numbers.append(num)
    print(abs(valid_numbers[-1]))
    for num in valid_numbers:
        pq.put(num)


valid = set()

for T in range(int(inp())):
    pq_max = PriorityQueue()
    pq_min = PriorityQueue()
    valid.clear()
    for Q in range(int(inp())):
        query = inp().split()
        cmd = query[0]
        x = int(query[1])
        if cmd == 'insert':
            if x not in valid:
                valid.add(x)
                pq_min.put(x)
                pq_max.put(-x)
        elif cmd == 'erase':
            if x in valid:
                valid.remove(x)
        elif cmd == 'update':
            y = int(query[2])
            if y not in valid and x in valid:
                valid.remove(x)
                valid.add(y)
                pq_min.put(y)
                pq_max.put(-y)
        elif len(valid) == 0:
            print("empty")
        else:
            c = int(query[1])
            c = min(c, len(valid))
            if cmd == 'front':
                get_cth_element(pq_min, c)
            else:
                get_cth_element(pq_max, c)
