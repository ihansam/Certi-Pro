import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

l = []

for _ in range(int(inp())):
    cmd, arg = inp().split()
    if cmd == '1':
        l.append(arg.lower())
    elif cmd == '2':
        if arg == '0':
            l.sort()
        elif arg == '1':
            l.sort(reverse=True)
        else:
            l.sort(key=lambda x: (len(x), x))
        print(*l[:3])
    else:
        l[0] += arg.lower()
        l[0] = l[0][:15]    # if 없어도 됨
        print(l[0])
