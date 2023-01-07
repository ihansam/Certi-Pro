import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

N = int(inp())
A = [inp().rstrip() for _ in range(N)]
K = 2
db = [[] for _ in range(2**(K**2))]


def get_key(arr, x, y):
    ret = 0
    for r in range(x, x+K):
        for c in range(y, y+K):
            ret *= 2
            ret += arr[r][c] == '+'
    return ret


# hash 등록
for x in range(N-3):
    for y in range(N-3):
        db[get_key(A, x, y)].append((x, y))

# query
for Q in range(int(inp())):
    M = int(inp())
    B = [inp().rstrip() for _ in range(M)]
    res = 0
    for cx, cy in db[get_key(B, 0, 0)]:
        same = True
        for i in range(M):
            if A[cx+i][cy:cy+M] != B[i]:
                same = False
                break
        if same:
            res += 1

    print(res)
