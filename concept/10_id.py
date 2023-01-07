import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

db = {}
logins = 0

for _ in range(int(inp())):
    cmd, arg = inp().split()
    if cmd == '1':
        print(int(arg in db.keys()))
    elif cmd == '2':
        print(int(arg in db and db[arg]))
    elif cmd == '3':
        if arg not in db.keys():
            db[arg] = 0
        print(len(db))
    elif cmd == '4':
        if arg in db.keys():
            logins -= db[arg]
            del db[arg]
        print(len(db))
    elif cmd == '5':
        if arg in db.keys() and not db[arg]:
            db[arg] = 1
            logins += 1
        print(logins)
    elif cmd == '6':
        if arg in db.keys() and db[arg]:
            db[arg] = 0
            logins -= 1
        print(logins)
