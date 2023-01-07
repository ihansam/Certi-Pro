import sys

sys.stdin = open('input.txt', 'r')
inp = sys.stdin.readline

# conference = []
# for _ in range(int(inp())):
#     conference.append(list(map(int, inp().split())))

# list comprehension 이 훨씬 빠름
conference = [list(map(int, inp().split())) for _ in range(int(inp()))]
conference.sort(key=lambda x: x[2])

ans = []
end = 0
for cid, s, e in conference:
    if s >= end:
        ans.append(cid)
        end = e

print(len(ans))
print(*ans)
