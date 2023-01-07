import sys
from collections import defaultdict
from heapq import heappop, heappush

sys.stdin = open('input.txt')
inp = sys.stdin.readline


class Player:
    sum, avg, cnt = 0, 0, 0

    def update(self, dsum, dcnt):
        self.sum += dsum
        self.cnt += dcnt
        self.avg = 0 if self.cnt == 0 else round(self.sum / self.cnt)

    def __repr__(self):
        return f"({self.sum}, {self.avg}, {self.cnt})"


n, m = map(int, inp().split())
scout_db = [defaultdict(int) for _ in range(n+1)]
player_db = [Player() for _ in range(m+1)]
maxsum, minsum, maxavg, minavg = [], [], [], []


def push(pid):
    heappush(maxsum, (-player_db[pid].sum, -pid))
    heappush(minsum, (player_db[pid].sum, pid))
    heappush(maxavg, (-player_db[pid].avg, -pid))
    heappush(minavg, (player_db[pid].avg, pid))


for i in range(1, m+1):
    push(i)

for _ in range(int(inp())):
    query = inp().split()
    cmd = query[0]
    if cmd == 'EVAL':
        sid, pid, score = map(int, query[1:])
        if pid in scout_db[sid]:
            player_db[pid].update(score - scout_db[sid][pid], 0)
        else:
            player_db[pid].update(score, 1)
            scout_db[sid][pid] = score
            push(pid)
    elif cmd == 'CLEAR':
        sid = int(query[1])
        for pid, score in scout_db[sid].items():
            player_db[pid].update(-score, -1)
            push(pid)
        scout_db[sid].clear()
    elif cmd == 'SUM':
        pq = maxsum if int(query[1]) else minsum
        while abs(pq[0][0]) != player_db[abs(pq[0][1])].sum:
            heappop(pq)
        print(abs(pq[0][1]))
    else:
        pq = maxavg if int(query[1]) else minavg
        while abs(pq[0][0]) != player_db[abs(pq[0][1])].avg:
            heappop(pq)
        print(abs(pq[0][1]))
