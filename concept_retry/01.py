import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
inp = sys.stdin.readline

db = deque()

for _ in range(int(inp())):
    q = list(map(int, inp().split()))
    cmd, arg = q[:2]
    val = q[-1]
    if cmd == 1:
        if arg:
            db.append(val)
        else:
            db.appendleft(val)
    elif cmd == 2:
        cnt = 0
        pos = -1 if arg else 0
        if arg:
            while cnt < 3 and abs(pos) <= len(db):
                if db[pos] >= val:
                    del db[pos]
                    cnt += 1
                else:
                    pos -= 1
        else:
            while cnt < 3 and pos < len(db):
                if db[pos] >= val:
                    del db[pos]
                    cnt += 1
                else:
                    pos += 1
    elif cmd == 3:
        db = deque(sorted(db, key=lambda x: (abs(arg-x), x)))       # 두 가지 기준으로 정렬하기
    else:
        if arg:
            print(*reversed(db))                                    # 한 칸씩 띄워 출력하기
        else:
            print(*db)
