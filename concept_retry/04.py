import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
inp = sys.stdin.readline

# db로 str 쓰면 안된다. 수정할 때마다 새로 복사해 생성함
for T in range(int(inp())):
    log = inp().rstrip()
    left = []               # 초기화하지 않고 그냥 아싸리 새로 생성하는 것이
    right = deque()         # 시간은 빠르고 메모리는 더 차지
    for c in log:
        if c == '-' and left:
            left.pop()
        elif c == '<' and left:
            right.appendleft(left.pop())
        elif c == '>' and right:
            left.append(right.popleft())
        elif c.isalpha() or c.isdigit():
            left.append(c)
    print(''.join(left), end='')    # 리스트 하나씩 출력하는 것보다
    print(''.join(right))           # 스트링 만들어서 출력하는게 더 빠르네?
