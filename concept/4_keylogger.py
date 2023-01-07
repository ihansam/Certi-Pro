import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

# 이 문제에서 str 쓰면 append 할 때 싹 다 복사하기 때문에 시간초과!
for _ in range(int(input())):
    log = input().rstrip()
    lstr = []
    rstr = []
    for cmd in log:
        if cmd == '-':
            if lstr:
                lstr.pop()
        elif cmd == '<':
            if lstr:
                rstr.append(lstr.pop())
        elif cmd == '>':
            if rstr:
                lstr.append(rstr.pop())
        else:
            lstr.append(cmd)
    print(''.join(lstr) + ''.join(rstr[::-1]))
