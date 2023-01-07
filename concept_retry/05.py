import sys

sys.stdin = open('input.txt', 'r')
inp = sys.stdin.readline

dice = []
# t = [5, 3, 4, 1, 2, 0]

for _ in range(int(inp())):
    # di = list(map(int, inp().split()))
    # die = [0] * 7
    # for i, d in enumerate(di):
    #     die[d] = di[t[i]]
    # dice.append(die)

    a, b, c, d, e, f = list(map(int, inp().split()))
    die = [0] * 7
    # die[a], die[b], die[c], die[d], die[e], die[f] = f, d, e, b, c, a
    for x, y in ((a, f), (b, d), (c, e)):
        die[x], die[y] = y, x
    dice.append(die)

ans = 0
for n in range(1, 7):
    part_sum = 0
    bottom = n
    for die in dice:
        top = die[bottom]
        for t in (6, 5, 4):
            if t not in (top, bottom):
                part_sum += t
                break
        bottom = top
    ans = max(ans, part_sum)

print(ans)
