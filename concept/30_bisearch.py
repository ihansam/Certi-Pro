import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline


def lower_bound(x):     # x보다 크거나 같은 가장 작은 값
    s, e = 0, n-1
    while s <= e:
        mid = (s+e)//2
        if arr[mid] >= x:
            e = mid - 1
        else:
            s = mid + 1
    return arr[s] if s < n else -1


def b_search(x):
    s, e = 0, n-1
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            e = mid - 1
        else:
            s = mid + 1
    return -1


n = int(inp())
arr = list(map(int, inp().split()))
q = int(inp())
barr = list(map(int, inp().split()))

for x in barr:
    print(b_search(x), end=' ')
