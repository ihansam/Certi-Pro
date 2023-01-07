### solution.py ###
from collections import defaultdict

word_list = []
idx_list = []
word_dict = set()
word_candidate = defaultdict(list)


def init(N: int, str: list) -> None:
    global word_list, idx_list, word_dict, word_candidate
    word_list = ''.join(str).split('_')
    idx_list.clear()
    idx = 0
    for c in str:
        idx_list.append(idx)
        if c == '_':
            idx += 1
    word_dict.clear()
    word_candidate.clear()


def addDict(word: list) -> None:
    global word_dict, word_candidate
    word_str = ''.join(word)
    word_dict.add(word_str)
    for i, c in enumerate(word):
        word[i] = "*"
        word_candidate[''.join(word)].append(word_str)
        word[i] = c


def removeDict(word: list) -> None:
    global word_dict
    word_str = ''.join(word)
    word_dict -= {word_str}


def correctWord(start: int, end: int) -> int:
    ret = 0
    s, e = idx_list[start], idx_list[end] + 1
    for idx, word in enumerate(word_list[s:e], s):
        if word in word_dict:
            continue
        candidates = []
        split_word = list(word)
        for i, c in enumerate(split_word):
            split_word[i] = "*"
            candidate = ''.join(split_word)
            split_word[i] = c
            if candidate in word_candidate:
                corrected = word_candidate[candidate]
                for corr in corrected:
                    if corr in word_dict:
                        candidates.append(corr)
        if candidates:
            ret += 1
            word_list[idx] = min(candidates)

    return ret


def destroy(result: list) -> None:
    result[:] = list('_'.join(word_list))


### main.py ###
import sys
# from solution import init, addDict, removeDict, correctWord, destroy

ADD = 100
REMOVE = 200
CORRECT = 300


def run():
    len = int(sys.stdin.readline())
    buf_b1 = list(sys.stdin.readline()[0:len])

    init(len, buf_b1)

    cmdCount = int(sys.stdin.readline())

    ret_val = 1

    for i in range(cmdCount):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == ADD:
            buf_s = list(next(inputs))
            addDict(buf_s)

        elif cmd == REMOVE:
            buf_s = list(next(inputs))
            removeDict(buf_s)

        elif cmd == CORRECT:
            start = int(next(inputs))
            end = int(next(inputs))
            ret = correctWord(start, end)
            ans = int(next(inputs))
            if ret != ans:
                ret_val = 0

    buf_b2 = list(0 for _ in range(len + 1))
    destroy(buf_b2)

    buf_b1 = list(sys.stdin.readline())

    for i in range(len):
        if buf_b1[i] != buf_b2[i]:
            ret_val = 0

    return ret_val


if __name__ == '__main__':
    # sys.stdin = open('input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
