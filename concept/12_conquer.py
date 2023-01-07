import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

n, q = map(int, inp().split())
land = {}
cnt = [0] * 4

for i in range(1, q+1):
    p = i % 4
    r, c = map(int, inp().split())
    addr = r * n + c
    if addr not in land:
        land[addr] = p
        cnt[p] += 1
    elif land[addr] == p:
        del land[addr]
        cnt[p] -= 1
    else:
        q = land[addr]
        if cnt[p] < cnt[q]:
            land[addr] = p
            cnt[p] += 1
            cnt[q] -= 1
for c in (1, 2, 3, 0):
    print(cnt[c])
