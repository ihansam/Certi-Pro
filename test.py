def solution(data):
    left, right = data
    l_score, r_score = 0, 0

    for l, r in zip(left, right):
        print(l, r)
