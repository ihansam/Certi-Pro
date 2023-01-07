from typing import List
from collections import deque, defaultdict
from heapq import heappush, heappop, nlargest

global n
adj_graph = []
dis_graph = []
cafe_list = []
score_db = defaultdict(int)
best_db = defaultdict(int)


def bfs(begin: int):
    global dis_graph
    q = deque()
    q.append((begin, 0))
    dis_graph[begin][begin] = -1
    while q:
        node, dis = q.popleft()
        for nxt in adj_graph[node]:
            if dis_graph[begin][nxt]:
                continue
            q.append((nxt, dis+1))
            dis_graph[begin][nxt] = dis + 1


def init(N: int, M: int, roads: List[List[int]]) -> None:
    global n, adj_graph, dis_graph, cafe_list, score_db, best_db
    n = N
    adj_graph = [[] for _ in range(n+1)]
    for i in range(M):
        t1, t2 = roads[i]
        adj_graph[t1].append(t2)
        adj_graph[t2].append(t1)
    dis_graph = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        bfs(i)
    cafe_list = [[] for _ in range(n+1)]
    score_db.clear()
    best_db.clear()


def addCafe(townID: int, name: str) -> None:
    cafe_list[townID].append(name)


def addScore(name: str, score: int) -> None:
    score_db[name] += score
    new_score = score_db[name]
    for i in range(len(name)):
        for j in range(i+1, len(name)+1):
            sub_str = name[i:j]
            best_db[sub_str] = max(best_db[sub_str], new_score)


def getBestScore(sub: str) -> int:
    return best_db[sub]


def getTop3Score(townID: int, step: int) -> int:
    # candidates = []
    # ret = 0
    # cnt = 0
    #
    # for tid in range(1, n+1):
    #     distance = dis_graph[townID][tid]
    #     if distance and distance <= step:
    #         for cafe in cafe_list[tid]:
    #             heappush(candidates, -score_db[cafe])
    #
    # while cnt < 3 and candidates:
    #     ret -= heappop(candidates)
    #     cnt += 1
    #
    # return ret
    distance = [-1] * (n+1)
    distance[townID] = 0
    q = deque([townID])
    candidate = []
    while q:
        tid = q.popleft()
        dis = distance[tid]
        candidate += [score_db[cafe] for cafe in cafe_list[tid]]
        if dis == step:
            continue
        for adj in adj_graph[tid]:
            if distance[adj] == -1:
                q.append(adj)
                distance[adj] = dis + 1

    return sum(nlargest(3, candidate))
