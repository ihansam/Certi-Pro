import sys
from collections import deque

sys.stdin = open('input.txt')
inp = sys.stdin.readline


def is_hamming(str_a, str_b):
    ret = 0
    for a, b in zip(str_a, str_b):
        if a != b:
            ret += 1
        if ret == 2:
            return 0
    return ret


n, k = map(int, inp().split())
code = [''] + [inp().rstrip() for _ in range(n)]
graph = {i: [] for i in range(1, n+1)}

for i in range(1, n+1):
    for j in range(i+1, n+1):
        dis = is_hamming(code[i], code[j])
        if dis:
            graph[i].append(j)
            graph[j].append(i)

begin, end = map(int, inp().split())

visit = [-1] * (n+1)
q = deque()
q.append(begin)
visit[begin] = begin

done = False
while q and not done:
    curr = q.popleft()
    for next in graph[curr]:
        if visit[next] == -1:
            visit[next] = curr
            if next == end:
                done = True
                break
            q.append(next)
if not done:
    print(-1)
else:
    ans = [end]
    while end != visit[end]:
        end = visit[end]
        ans.append(end)
    print(*ans[::-1])
