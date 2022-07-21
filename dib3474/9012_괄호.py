import sys

n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline().strip('\n')
    stack = 0
    flag = 1
    for x in line:
        if x == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            flag = 0
            break

    flag = 1 if stack == 0 else 0

    if flag:
        print("YES")
    else:
        print("NO")
