import sys

sys.stdin = open('input.txt')
inp = sys.stdin.readline

member = set()
logins = set()

for _ in range(int(inp())):
    cmd, arg = inp().split()
    if cmd == '1':
        print(int(arg in member))
    elif cmd == '2':
        print(int(arg in logins))
    elif cmd == '3':
        member |= {arg}
        print(len(member))
    elif cmd == '4':
        member -= {arg}
        logins -= {arg}
        print(len(member))
    elif cmd == '5':
        if arg in member:
            logins |= {arg}
        print(len(logins))
    elif cmd == '6':
        logins -= {arg}
        print(len(logins))
