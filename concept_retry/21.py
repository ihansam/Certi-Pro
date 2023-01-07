import sys
from heapq import heappop, heappush
from collections import defaultdict

sys.stdin = open('input.txt')
inp = sys.stdin.readline


class Player:
    def __init__(self, pname):
        self.cnt = 0
        self.sum = 0
        self.avg = 0
        self.name = pname

    def update_score(self, dcnt, score):
        self.cnt += dcnt
        self.sum += score
        self.avg = round(self.sum / self.cnt, 1) if self.cnt else 0


def heap_push(pid):
    p_sum = player_db[pid].sum
    p_avg = player_db[pid].avg
    heappush(sum_min, (p_sum, pid))
    heappush(sum_max, (-p_sum, -pid))
    heappush(avg_min, (p_avg, pid))
    heappush(avg_max, (-p_avg, -pid))


n, m = map(int, inp().split())
player_list = inp().split()
player_list.sort()
pname_db = {pname: pid for pid, pname in enumerate(player_list)}
player_db = [Player(pname) for pname in player_list]

sum_min, sum_max, avg_min, avg_max = [], [], [], []
score_board = dict()

for pid in range(m):
    heap_push(pid)

for _ in range(int(inp())):
    query = inp().split()
    cmd, args = query[0], query[1:]
    if cmd == 'EVAL':
        sid, pname, score = int(args[0]), args[1], int(args[2])
        pid = pname_db[pname]
        if sid not in score_board:
            score_board[sid] = defaultdict(int)
        old = score_board[sid][pid]
        player_db[pid].update_score(int(old == 0), score - old)
        score_board[sid][pid] = score
        heap_push(pid)
    elif cmd == 'CLEAR':
        sid = int(args[0])
        for pid, score in score_board[sid].items():
            player_db[pid].update_score(-1, -score)
            heap_push(pid)
        score_board[sid].clear()
    else:
        flag = int(args[0])
        if cmd == 'SUM':
            pq = sum_max if flag else sum_min
            while abs(pq[0][0]) != player_db[abs(pq[0][1])].sum:
                heappop(pq)
        else:
            pq = avg_max if flag else avg_min
            while abs(pq[0][0]) != player_db[abs(pq[0][1])].avg:
                heappop(pq)
        print(player_db[abs(pq[0][1])].name)
