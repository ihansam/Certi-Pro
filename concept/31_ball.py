import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline


def is_possible(target):
    bucket = 1
    idx = 0
    part_sum = 0
    while idx < n and bucket <= m:
        part_sum += ball[idx]
        if part_sum > target:
            bucket += 1
            part_sum = 0
        else:
            idx += 1
    return bucket <= m


n, m = map(int, inp().split())
ball = list(map(int, inp().split()))

s, e = max(ball), sum(ball)
ans = 0

while s <= e:
    mid = (s + e) // 2
    possible = is_possible(mid)
    if possible:
        e = mid - 1
        ans = mid
    else:
        s = mid + 1

print(ans)
