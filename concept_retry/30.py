import sys

sys.stdin = open('input.txt', 'r')
ip = sys.stdin.readline

n = int(ip())
a = list(map(int, ip().split()))
q = int(ip())
b = list(map(int, ip().split()))

for target in b:
    s, e, idx = 0, n-1, -1
    while s <= e:
        mid = (s + e) // 2
        if a[mid] == target:
            idx = mid
            break
        elif a[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    print(idx, end=' ')
