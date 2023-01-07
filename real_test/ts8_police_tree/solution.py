from heapq import heappush, heappop
from typing import List
from collections import deque

adj_graph = []
next_town = []
global curr_time, curr_location
case_db = []


class Case:
    pq = []

    def __init__(self, time, cid, tid, pri):
        self.time = time
        self.town_id = tid
        self.closed = False
        heappush(Case.pq, (-pri, cid))


def _init_town_table(n):
    global next_town
    next_town = [[-1]*n for _ in range(n)]
    for begin in range(n):
        candidates = adj_graph[begin]
        visited = next_town[begin]
        visited[begin] = begin
        for candi in candidates:
            q = deque([candi])
            visited[candi] = candi
            while q:
                cur = q.popleft()
                for nxt in adj_graph[cur]:
                    if visited[nxt] == -1:
                        q.append(nxt)
                        visited[nxt] = candi


def _update(t):
    global curr_time, curr_location
    while curr_time < t:
        while Case.pq and case_db[Case.pq[0][1]].closed:
            heappop(Case.pq)
        if not Case.pq:
            curr_time = t
            return
        case = case_db[Case.pq[0][1]]
        destination = case.town_id
        if curr_location == destination:
            heappop(Case.pq)
            case.closed = True
        else:
            curr_location = next_town[curr_location][destination]
        curr_time += 1


def init(N: int, parent: List[int]) -> None:
    global adj_graph, curr_time, curr_location, case_db

    adj_graph = [[] for _ in range(N)]
    for _node, _parent in enumerate(parent[1:N], 1):
        adj_graph[_node].append(_parent)
        adj_graph[_parent].append(_node)

    _init_town_table(N)
    curr_time = 0
    curr_location = 0
    case_db.clear()
    Case.pq.clear()


def occur(timeStamp: int, caseID: int, townNum: int, prior: int) -> None:
    _update(timeStamp)
    case_db.append(Case(timeStamp, caseID, townNum, prior))


def cancel(timeStamp: int, caseID: int) -> None:
    _update(timeStamp)
    case = case_db[caseID]
    case.closed = True


def position(timeStamp: int) -> int:
    _update(timeStamp)
    return curr_location
