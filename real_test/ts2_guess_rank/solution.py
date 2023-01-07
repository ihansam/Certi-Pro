global remains
candidate = [None] * 4


def get_id_of(x, query):
    global remains, candidate
    if candidate[x]:
        s, e = candidate[x]
    else:
        s, e = 0, len(remains)
    while e - s > 5:
        mid = max((s+e)//2, s+5)
        ret = query((mid-s), remains[s:mid], 0)
        if ret == x:
            e = mid
        else:
            if x < ret < 4:
                candidate[ret] = (s, mid)
            s = mid
    for i in range(s, e):
        if query(len(remains)-1, remains[:i] + remains[i+1:], 0) != x:
            return remains[i]


def getRank(retRank: [int], query) -> None:
    global remains, candidate

    remains = list(range(1000))
    candidate = [None] * 4
    min_id = []
    for rank in range(4):
        min_id.append(get_id_of(rank, query))
        retRank[min_id[rank]] = rank
        remains.remove(min_id[rank])
    for x in remains:
        retRank[x] = query(5, min_id + [x], 1)


import sys
# from solution import getRank

N = 1000

ansRank = [0 for _ in range(N)]
isused = [0 for _ in range(N)]

MAXQUERY = 1000000

okay = False
querycount = 0


def query(K: int, sub: [int], opt: int):
    global querycount, okay

    if not okay or K < 5 or K > N or (opt != 0 and opt != 1) or querycount >= MAXQUERY:
        okay = False
        return -1

    querycount += 1

    if opt == 0:
        ret = N - 1
        for k in range(K):
            if sub[k] < 0 or sub[k] >= N or isused[sub[k]] == querycount:
                okay = False
                return -1

            isused[sub[k]] = querycount

            if ret > ansRank[sub[k]]:
                ret = ansRank[sub[k]]
        return ret
    else:
        ret = 0
        for k in range(K):
            if sub[k] < 0 or sub[k] >= N or isused[sub[k]] == querycount:
                okay = False
                return -1

            isused[sub[k]] = querycount

            if ret < ansRank[sub[k]]:
                ret = ansRank[sub[k]]
        return ret


callcount = 0
retRank = [0 for _ in range(N)]


def run():
    global N, okay, querycount, callcount

    okay = True

    for c in range(10):
        limit = 1200

        inputs = iter(sys.stdin.readline().split())
        for i in range(N):
            ansRank[i] = int(next(inputs))

        querycount = 0

        for i in range(N):
            isused[i] = 0

        if okay:
            getRank(retRank, query)

        if limit < querycount:
            okay = False

        if okay:
            for i in range(N):
                if ansRank[i] != retRank[i]:
                    okay = False

        callcount += querycount

    return okay


def main():
    global callcount

    sys.stdin = open('input.txt', 'r')
    TC, MARK = map(int, sys.stdin.readline().split())

    totalcount = 0
    for testcase in range(1, TC + 1):
        callcount = 0

        score = MARK if run() else 0
        # print("#%d %d %d" % (testcase, score, callcount), flush=True)
        print("#%d %d" % (testcase, score), flush=True)
        totalcount += callcount

    # print("totalcount = %d, average = %.3lf" % (totalcount, (totalcount / (TC * 10))))


if __name__ == '__main__':
    main()
    # was 259697 => 258736
