from typing import List
from heapq import heappush, heappop

global n
buddies = []
location = []
order_db = []
pq = []
my = 0
total = 1
distance = 2
DIS_OFFSET = 20
CNT_OFFSET = 42


def init(N: int, px: List[int], py: List[int]) -> None:
    global buddies, location, order_db, pq, n

    buddies = [[] for _ in range(N)]
    location.clear()
    for i in range(N):
        location.append((px[i], py[i]))
    order_db = [{} for _ in range(N)]
    pq = [[] for _ in range(N)]
    n = N


def push_pq(uid, cid):
    _data = order_db[uid][cid]
    heappush(pq[uid], ((3000-_data[total]) << CNT_OFFSET) | (_data[distance] << DIS_OFFSET) | cid)
    # heappush(pq[uid], (-_data[total], _data[distance], cid))


def addCafe(cid: int, x: int, y: int) -> None:
    for uid in range(n):
        ux, uy = location[uid]
        order_db[uid][cid] = [0, 0, abs(x - ux) + abs(y - uy)]
        push_pq(uid, cid)


def eraseCafe(cid: int) -> None:
    for uid in range(n):
        del order_db[uid][cid]


def order(uid: int, cid: int) -> None:
    order_db[uid][cid][my] += 1
    order_db[uid][cid][total] += 1
    push_pq(uid, cid)
    for bid in buddies[uid]:
        order_db[bid][cid][total] += 1
        push_pq(bid, cid)


def beBuddy(tid: int, uid: int) -> None:
    buddies[uid].append(tid)
    buddies[tid].append(uid)

    for cid in order_db[uid].keys():
        my_cnt = order_db[uid][cid][my]
        bd_cnt = order_db[tid][cid][my]
        if my_cnt:
            order_db[tid][cid][total] += my_cnt
            push_pq(tid, cid)
        if bd_cnt:
            order_db[uid][cid][total] += bd_cnt
            push_pq(uid, cid)


def recommend(uid: int) -> int:
    valid = []
    while len(valid) < 10:
        _data = heappop(pq[uid])
        cnt, dis, cid = 3000 - (_data >> CNT_OFFSET),\
                        (_data >> DIS_OFFSET) & 0b1111111111111111111111,\
                        _data & 0b11111111111111111111
        # cnt, dis, cid = heappop(pq[uid])
        # if cid in order_db[uid] and order_db[uid][cid][total] == abs(cnt):
        if cid in order_db[uid] and order_db[uid][cid][total] == cnt:
            valid.append(cid)
    for cid in valid:
        push_pq(uid, cid)

    return valid[-1]
