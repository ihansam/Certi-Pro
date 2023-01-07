import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

N = int(inp())
A = [inp().rstrip() for _ in range(N)]

db = [[] for _ in range(2**4)]


def hf(arr, x, y):
    ret = 0
    for i in range(2):
        for j in range(2):
            ret *= 2
            ret += (arr[x+i][y+j] == '+')
    return ret


def check(x, y):
    try:
        for i in range(m):
            if A[x+i][y:y+m] != B[i]:
                return 0
        return 1
    except IndexError:
        return 0


for i in range(N-3):
    for j in range(N-3):
        db[hf(A, i, j)].append((i, j))

for _ in range(int(inp())):
    m = int(inp())
    B = [inp().rstrip() for _ in range(m)]

    key = hf(B, 0, 0)
    cnt = 0
    for x, y in db[key]:
        cnt += check(x, y)
    print(cnt)