import sys
sys.stdin = open('input.txt')
inp = sys.stdin.readline

n, m, q = map(int, inp().split())
memo = list(inp().rstrip())
curs = 0
for i in range(q):
    query = inp().rstrip()
    # print(query)
    if query.startswith('erase'):
        if 0 <= curs < len(memo):
            del memo[curs]
            curs -= 1
    elif query.startswith('insert'):
        memo.insert(curs, query.split()[-1])
        curs += 1
    elif query.startswith('move'):
        r, c = query.split()[1:]
        curs = int(r) * m + int(c)
        if curs >= len(memo):
            curs = len(memo)
            print("*")
        else:
            print(memo[curs])
        curs -= 1
    # print(''.join(memo))
