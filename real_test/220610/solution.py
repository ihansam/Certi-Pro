from typing import List
from collections import deque, defaultdict

n = 0
mmap = []
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
db = defaultdict(list)


def encode(lst):
    ret = 0
    for l in lst:
        ret *= 10
        ret += l
    return ret


def decode(num):
    return list(map(int, list(str(num))))


def _gen_db(lst, sx, sy, d):
    dp = deque([lst[0]])
    for i in range(1, 5):
        item = dp[-1] * 10 + lst[i]
        dp.append(item)
        db[item].append((sx, sy, d))
    for i in range(1, len(lst)):
        sx += dx[d]
        sy += dy[d]
        for j in range(2, len(dp)):
            item = dp[j] % (10**j)
            dp[j] = item
            db[item].append((sx, sy, d))
        try:
            item = dp[-1] * 10 + lst[i + 4]
            dp.append(item)
            db[item].append((sx, sy, d))
        except:
            pass
        dp.popleft()


def init(N:int, mMap:List[List[int]]) -> None:
    global n, mmap, db
    n = N
    mmap = [mMap[i][:n] for i in range(n)]
    db.clear()
    for i in range(n):
        _gen_db(mmap[i], i, 0, 1)
        _gen_db([mmap[j][i] for j in range(n)], 0, i, 0)


def _get_candi_list(M, mStructure):
    global n, db
    ret = []
    structure = mStructure[:M]
    tg = max(structure) + 1
    rg = 6 - tg + min(structure)
    candi = [tg - item for item in structure]
    while rg:
        rg -= 1
        key = encode(candi)
        for cd in db[key]:
            ret.append((key, cd))
        rev_key = encode(candi[::-1])
        if key != rev_key:
            for cd in db[rev_key]:
                ret.append((rev_key, cd))
        for i in range(M):
            candi[i] += 1
    return ret


def numberOfCandidate(M:int, mStructure:List[int]) -> int:
    global n
    if M == 1:
        return n * n
    return len(_get_candi_list(M, mStructure))


def _bfs(structure, candidate, h):
    global n, mmap
    x, y, d = candidate
    copied_map = [[item for item in line] for line in mmap]
    for i in range(len(structure)):
        copied_map[x][y] += structure[i]
        x += dx[d]
        y += dy[d]

    q = deque([])
    start_pos = []
    for i in range(n):
        start_pos.append((0, i))
        start_pos.append((n-1, i))
        if i == 0 or i == n-1:
            continue
        start_pos.append((i, 0))
        start_pos.append((i, n-1))
    for sx, sy in start_pos:
        if not (0 < copied_map[sx][sy] < h):
            continue
        copied_map[sx][sy] = 0
        q.append((sx, sy))
        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if not (0 <= nx < n) or not (0 <= ny < n):
                    continue
                if not (0 < copied_map[nx][ny] < h):
                    continue
                copied_map[nx][ny] = 0
                q.append((nx, ny))

    ret = 0
    for i in range(n):
        for j in range(n):
            if not copied_map[i][j]:
                continue
            ret += 1

    return ret


def maxArea(M:int, mStructure:List[int], mSeaLevel:int) -> int:
    global db
    ret = -1
    structure = mStructure[:M]
    if M == 1:
        candies = []
        k = mStructure[0]
        for i in range(n):
            for j in range(n):
                candies.append((k, (i, j, 0)))
    else:
        candies = _get_candi_list(M, structure)
    for candi in candies:
        ret = max(ret, _bfs(decode(candi[0]), candi[1], mSeaLevel))
    return ret
