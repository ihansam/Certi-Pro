import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

ans = 0
t = [5, 3, 4, 1, 2, 0]

n = int(inp())
dices = [[0 for _ in range(7)] for _ in range(n)]
di = []
for _ in range(n):
    di = list(map(int, inp().split()))
    for i, d in enumerate(di):
        dices[_][d] = di[t[i]]

for num in range(1, 7):
    res = 0
    bottom = num
    for dice in dices:
        top = dice[bottom]
        for i in [6, 5, 4]:
            if i not in (top, bottom):
                res += i
                break
        bottom = top
    ans = max(ans, res)
print(ans)
