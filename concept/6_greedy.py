import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

ans = []
l = [list(map(int, inp().split())) for _ in range(int(inp()))]
l.sort(key=lambda x: x[2])
time = 0
for n, s, e in l:
    if s >= time:
        ans.append(n)
        time = e
print(len(ans))
print(*ans)
