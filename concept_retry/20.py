import sys
from heapq import heappop, heappush
from collections import defaultdict

sys.stdin = open('input.txt')
inp = sys.stdin.readline


class Player:
    def __init__(self):
        self.cnt = 0
        self.sum = 0
        self.avg = 0

    def update_score(self, dcnt, score):
        self.cnt += dcnt
        self.sum += score
        self.avg = round(self.sum / self.cnt) if self.cnt else 0


def heap_push(pid):
    p_sum = db[pid].sum
    p_avg = db[pid].avg
    heappush(sum_min, (p_sum, pid))
    heappush(sum_max, (-p_sum, -pid))
    heappush(avg_min, (p_avg, pid))
    heappush(avg_max, (-p_avg, -pid))


n, m = map(int, inp().split())

sum_min, sum_max, avg_min, avg_max = [], [], [], []
db = [Player() for _ in range(m + 1)]
score_board = [defaultdict(int) for _ in range(n+1)]

for pid in range(1, m+1):
    heap_push(pid)


for _ in range(int(inp())):
    query = inp().split()
    cmd, args = query[0], list(map(int, query[1:]))
    if cmd == 'EVAL':
        sid, pid, score = args
        old = score_board[sid][pid]
        db[pid].update_score(int(old == 0), score - old)
        score_board[sid][pid] = score
        heap_push(pid)
    elif cmd == 'CLEAR':
        sid = args[0]
        for pid in range(1, m+1):
            if pid in score_board[sid]:
                db[pid].update_score(-1, -score_board[sid][pid])
                heap_push(pid)
        score_board[sid].clear()
    else:
        flag = args[0]
        if cmd == 'SUM':
            pq = sum_max if flag else sum_min
            while abs(pq[0][0]) != db[abs(pq[0][1])].sum:   # 보기만 할 수도 있음
                heappop(pq)
        else:
            pq = avg_max if flag else avg_min
            while abs(pq[0][0]) != db[abs(pq[0][1])].avg:
                heappop(pq)
        print(abs(pq[0][1]))
