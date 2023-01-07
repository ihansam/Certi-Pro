import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')
inp = sys.stdin.readline

left, right = [], []

n = int(inp())
mid = int(inp())
print(mid)

for _ in range((n//2)):
    for num in map(int, inp().split()):
        if num < mid:
            heappush(left, -num)
        else:
            heappush(right, num)
    if len(left) > len(right):
        heappush(right, mid)
        mid = -heappop(left)
    elif len(left) < len(right):
        heappush(left, -mid)
        mid = heappop(right)
    print(mid)
