from heapq import heappush, heappop, nlargest
from collections import defaultdict

booth_db = {}


class Booth:
    def __init__(self, dur, cap):
        self.duration = dur
        self.capacity = cap
        self.finish = 0
        self.cnt_wait = 0
        self.pq_wait = []
        self.wait_status = defaultdict(int)

    def add_waiting(self, c, p):
        self.cnt_wait += c
        self.wait_status[p] += c
        heappush(self.pq_wait, -p)

    def update(self, tick):
        while self.finish <= tick and self.cnt_wait:
            enter_cnt = min(self.cnt_wait, self.capacity)
            self.cnt_wait -= enter_cnt
            self.finish += self.duration
            while enter_cnt:
                _p = -self.pq_wait[0]
                _c = self.wait_status[_p]
                _cnt = min(enter_cnt, _c)
                self.wait_status[_p] -= _cnt
                enter_cnt -= _cnt
                if self.wait_status[_p] == 0:
                    heappop(self.pq_wait)

    def __str__(self):
        return f"wait status: {self.wait_status} \n" \
               f"pq: {self.pq_wait}"


def init(boothN: int, bidArr: [int], duration: [int], capacity: [int]):
    global booth_db

    booth_db.clear()
    for i in range(boothN):
        booth_db[bidArr[i]] = Booth(duration[i], capacity[i])


def add(tick: int, bid: int, guestNum: int, priority: int):
    global booth_db
    booth = booth_db[bid]

    booth.update(tick - 1)
    booth.add_waiting(guestNum, priority)
    booth.finish = max(booth.finish, tick)
    booth.update(tick)

    return -booth.pq_wait[0] if booth.cnt_wait else 0


def search(tick: int, findCnt: int, bidArr: [int], numResult: [int]):
    wait_cnt_list = []
    for bid, booth in booth_db.items():
        booth.update(tick)
        wait_cnt_list.append((booth.cnt_wait, bid))

    numResult[:findCnt], bidArr[:findCnt] = zip(*nlargest(findCnt, wait_cnt_list))
