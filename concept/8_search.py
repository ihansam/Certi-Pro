import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

db = set()
for _ in range(int(inp())):
    key = inp().rstrip()
    if key in db:
        db.remove(key)
    else:
        db.add(key)
print(len(db))
