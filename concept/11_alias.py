import sys
from collections import defaultdict

sys.stdin = open('input.txt')
inp = sys.stdin.readline

# db = {}
prefix = set()
word_cnt = defaultdict(int)

for _ in range(int(inp())):
    word = inp().strip()
    sub = ""
    res = ""
    for c in word:
        sub += c
        if sub not in prefix:
            if res == "":
                res = sub
            prefix.add(sub)
    word_cnt[word] += 1
    # if word in word_cnt:
    #     word_cnt[word] += 1
    # else:
    #     word_cnt[word] = 1
    if res:
        print(res)
    else:
        if word_cnt[word] > 1:
            print(word, word_cnt[word], sep='')
        else:
            print(word)

    # s = inp().strip()
    # found = False
    # for i in range(len(s)):
    #     prefix = s[:i+1]
    #     if prefix not in db.keys():
    #         db[prefix] = 0
    #         if not found:
    #             print(prefix)
    #             found = True
    # db[s] += 1
    # if not found:
    #     if db[s] == 1:
    #         print(s)
    #     else:
    #         print(f"{s}{db[s]}")
