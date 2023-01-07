import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

db = set()
for _ in range(int(inp())):
    string = inp().rstrip()
    if string in db:
        db.remove(string)
        # db -= {string}    # 좀 더 느리긴 한데 예외처리를 안해도 됨
    else:
        db.add(string)
        # db |= {string}
print(len(db))
