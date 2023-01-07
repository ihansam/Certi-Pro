import sys

sys.stdin = open('input.txt')
ip = sys.stdin.readline

n, m = map(int, ip().split())
a = list(map(int, ip().split()))
ans, s, e = 0, max(a), sum(a)


def isp(t):
    bk, acm= 1, 0
    for cur in a:
        if acm + cur > t:
            acm = cur
            bk += 1
            if bk > m:
                return 0
        else:
            acm += cur
    return 1


while s <= e:
    mid = (s + e) // 2
    psb = isp(mid)
    if psb:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
print(ans)
