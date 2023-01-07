import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

db = {}     # id: login
logins = 0

for _ in range(int(inp())):
    cmd, key = inp().split()
    if cmd == '1':
        print(int(key in db))
    elif cmd == '2':
        print(db.get(key, 0))
    elif cmd == '3':
        if key not in db:
            db[key] = 0
        print(len(db))
    elif cmd == '4':
        if key in db:
            logins -= db[key]
            del db[key]
        print(len(db))
    elif cmd == '5':
        if key in db and not db[key]:
            db[key] = 1
            logins += 1
        print(logins)
    else:
        if key in db and db[key]:
            db[key] = 0
            logins -= 1
        print(logins)
