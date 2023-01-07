import sys
# 순열만 visit 이 필요하다. 조합/중복조합은 for문 범위가 마지막 숫자 다음이다.
inp = sys.stdin.readline
n, m = map(int, inp().split())
visit = [0] * 7
res = [0] * 5


def dfs(d, l):
    if d == n:
        print(*res[:n])
        return
    for i in range(l if m == 2 else 1, 7):
        if m == 3 and visit[i]:
            continue
        visit[i] = 1
        res[d] = i
        dfs(d+1, i)
        visit[i] = 0


dfs(0, 1)


# # 중복순열
# def nPIk(n, k):
#     def dfs(d):
#         if d == k:
#             print(*res[:k])
#             return
#         for i in range(1, n+1):
#             res[d] = i
#             dfs(d+1)
#     dfs(0)
#
#
# # 중복조합
# def nHk(n, k):
#     def dfs(d, l):
#         if d == k:
#             print(*res[:k])
#             return
#         for i in range(l, n+1):
#             res[d] = i
#             dfs(d+1, i)
#     dfs(0, 1)



