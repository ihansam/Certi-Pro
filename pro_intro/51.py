import sys
sys.stdin = open('i.txt', 'r')
ip = sys.stdin.readline

w = int(ip())
remain = list(map(int, ip().split()))
res = [0] * 6
val = [500, 100, 50, 10, 5, 1]
idx = 5

while w and idx > 0:
    must = w % val[idx-1] // val[idx]
    res[idx] += must
    remain[idx] -= must
    w -= must * val[idx]
    maxi = min(remain[idx] // (val[idx-1]//val[idx]) * (val[idx-1]//val[idx]), w // val[idx])
    res[idx] += maxi
    w -= maxi * val[idx]
    idx -= 1
res[0] = w // 500
print(sum(res))
print(*res)
