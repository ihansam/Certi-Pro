import sys

sys.stdin = open('input.txt', 'r')
inp = sys.stdin.readline

db = []

for _ in range(int(inp())):
    q = inp().split()
    cmd, arg = int(q[0]), q[1]
    if cmd == 1:
        db.append(arg.lower())
    elif cmd == 2:
        if arg == '0':
            db.sort()
        elif arg == '1':
            db.sort(reverse=True)
        else:
            db.sort(key=lambda x: (len(x), x))
        print(*db[:3])
    else:
        db[0] = f"{db[0]}{arg.lower()}"[:15]        # 15자 안넘어도 슬라이싱 됨
        print(db[0])
