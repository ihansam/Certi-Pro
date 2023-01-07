import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

K = int(input())
dna = input().strip()
D = defaultdict(int)
idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

# # string: 3000ms
# for i in range(len(dna)-K+1):
#     sub = ''.join(sorted(dna[i:i+K]))
#     D[sub] += 1

# cnt = [0] * 4
# for i, c in enumerate(dna):
#     cnt[idx[c]] += 1
#     if i >= K:
#         cnt[idx[dna[i-K]]] -= 1
#     # # cnt_tuple: 100ms
#     # D[tuple(cnt)] += 1
#
#     # integer: 90ms
#     key = 0
#     for count in cnt:
#         key *= 1001
#         key += count
#     D[key] += 1

# count 하지 않고 integer key 직접 계산: 80ms
base = {'A': 1001**3, 'C': 1001**2, 'G': 1001, 'T': 1}
key = 0

for i, c in enumerate(dna):
    key += base[c]
    if i >= K:
        key -= base[dna[i-K]]
    D[key] += 1

print(max(D.values()))
