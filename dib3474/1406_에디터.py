import sys

s = sys.stdin.readline().strip('\n')

M = int(sys.stdin.readline())

left = []
right = []

for i in s:
    left.append(i)

for i in range(M):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'P':
        left.append(cmd[1])
    elif cmd[0] == 'L':
        if len(left) != 0:
            right.append(left.pop())
    elif cmd[0] == 'D':
        if len(right) != 0:
            left.append(right.pop())
    elif cmd[0] == 'B':
        if len(left) != 0:
            left.pop()

while(len(left)):
    right.append(left.pop())

while(len(right)):
    print(right.pop(), end="")
