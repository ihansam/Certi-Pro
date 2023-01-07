import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

# db = dict()     # string: sid
# score_db = [0]  # sid: score
#
# for _ in range(int(inp())):
#     query = inp().split()
#     string, score = query[0].lower(), int(query[1])
#     sid = db.get(string, 0)
#     if sid:
#         score_db[sid] = max(score_db[sid], score)
#     else:
#         sid = len(db) + 1
#         db[string] = sid
#         score_db.append(score)
#     print(sid, score_db[sid])

db = {}     # string: [sid, score]  # 모든 데이터 한 DB에 때려 박는 이 방법이 메모리 엑세스를 한 번 덜 해서 더 빠른 듯
for _ in range(int(inp())):
    query = inp().split()
    key = query[0].lower()
    score = int(query[1])
    if key in db.keys():
        db[key][1] = max(db[key][1], score)
    else:
        db[key] = [len(db) + 1, score]
    print(*db[key])
