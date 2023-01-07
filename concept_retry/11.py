import sys
from collections import defaultdict

sys.stdin = open('input.txt')
inp = sys.stdin.readline

prefix = set()
word_cnt = defaultdict(int)     # 좀 느린 대신 예외처리 안 해도 됨

for _ in range(int(inp())):
    word = inp().rstrip()
    word_cnt[word] += 1
    res = ""
    pf = ""
    for c in word:
        pf += c
        if (not res) and (pf not in prefix):
            res = pf
        prefix.add(pf)
    if not res:
        res = word
        if word_cnt[word] > 1:
            res += str(word_cnt[word])
    print(res)
