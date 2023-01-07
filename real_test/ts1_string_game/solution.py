from collections import deque

data = deque()
global rev
db = [0] * (27**4)


def get_key(string: str):
    ret = 0
    for i in range(len(string)):
        ret *= 27
        ret += (ord(string[i]) - 96)
    return ret


def update_db(val):
    global db, rev, data

    sub_str = ""
    idx = 0 if rev else -1
    for i in range(4):
        if i >= len(data) or i < -len(data):
            break
        if rev:
            sub_str += data[idx]
            idx += 1
        else:
            sub_str = data[idx] + sub_str
            idx -= 1
        db[get_key(sub_str)] += val


def init(mStr: str):
    global data, rev, db

    rev = False
    db = [0] * (27**4)
    data.clear()

    for c in mStr:
        data.append(c)
        update_db(1)


def pushBack(mWord: str):
    global data, rev

    if rev:
        for c in mWord:
            data.appendleft(c)
            update_db(1)
    else:
        for c in mWord:
            data.append(c)
            update_db(1)


def popBack(k: int):
    global data, rev

    if rev:
        while k:
            update_db(-1)
            data.popleft()
            k -= 1
    else:
        while k:
            update_db(-1)
            data.pop()
            k -= 1


def reverseStr():
    global rev
    rev = not rev


def getCount(mWord: str) -> int:
    if rev:
        return db[get_key(mWord[::-1])]
    else:
        return db[get_key(mWord)]


import sys

CMD_INIT = 1
CMD_APPEND = 2
CMD_popBack = 3
CMD_reverseStr = 4
CMD_COUNT = 5


def run():
    query_cnt = int(sys.stdin.readline())
    correct = False

    for q in range(query_cnt):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == CMD_INIT:
            mStr = next(inputs)
            init(mStr)
            correct = True

        elif cmd == CMD_APPEND:
            mWord = next(inputs)
            if correct:
                pushBack(mWord)

        elif cmd == CMD_popBack:
            k = int(next(inputs))
            if correct:
                popBack(k)

        elif cmd == CMD_reverseStr:
            if correct:
                reverseStr()

        elif cmd == CMD_COUNT:
            mWord = next(inputs)
            ret = -1
            if correct:
                ret = getCount(mWord)

            ans = int(next(inputs))
            if ret != ans:
                correct = False

    return correct


def main():
    # sys.stdin = open('sample_input.txt', 'r')
    TC, MARK = map(int, sys.stdin.readline().split())

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)


if __name__ == '__main__':
    # import time
    # s = time.process_time()
    # for _ in range(5):
    main()
    # e = time.process_time()
    # print(f"{(e - s)*1000}ms")
