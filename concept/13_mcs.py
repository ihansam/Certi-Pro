import sys
from collections import defaultdict

sys.stdin = open('input.txt')
inp = sys.stdin.readline

t = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
db = defaultdict(int)

k = int(inp())
s = inp().strip()

cnt = [0] * 4

for i, c in enumerate(s):
    cnt[t[c]] += 1
    if i >= k:
        cnt[t[s[i-k]]] -= 1
    key = tuple(cnt)
    db[key] += 1

print(max(db.values()))
