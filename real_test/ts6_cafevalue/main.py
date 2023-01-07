import sys
from solution import init, addCafe, addScore, getBestScore, getTop3Score

CMD_INIT = 1
CMD_ADD_CAFE = 2
CMD_ADD_SCORE = 3
CMD_BEST = 4
CMD_TOP_3 = 5


def run():
    numQuery = int(sys.stdin.readline())
    isCorrect = False
    roads = [[0, 0] for _ in range(50)]

    for q in range(numQuery):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == CMD_INIT:
            N = int(next(inputs))
            M = int(next(inputs))
            for i in range(M):
                roads[i][0] = int(next(inputs))
                roads[i][1] = int(next(inputs))
            init(N, M, roads)
            isCorrect = True

        elif cmd == CMD_ADD_CAFE:
            townID = int(next(inputs))
            name = next(inputs)
            addCafe(townID, name)

        elif cmd == CMD_ADD_SCORE:
            name = next(inputs)
            score = int(next(inputs))
            addScore(name, score)

        elif cmd == CMD_BEST:
            sub = next(inputs)
            userAns = getBestScore(sub)
            ans = int(next(inputs))
            if userAns != ans:
                isCorrect = False

        elif cmd == CMD_TOP_3:
            townID = int(next(inputs))
            step = int(next(inputs))
            userAns = getTop3Score(townID, step)
            ans = int(next(inputs))
            if userAns != ans:
                isCorrect = False

    return isCorrect


if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    input = sys.stdin.readline
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)