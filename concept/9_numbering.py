import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

db = {}
for _ in range(int(inp())):
    query = inp().split()
    key = query[0].lower()
    score = int(query[1])
    if key in db.keys():
        db[key][1] = max(db[key][1], score)
    else:
        db[key] = [len(db) + 1, score]
    print(*db[key])
