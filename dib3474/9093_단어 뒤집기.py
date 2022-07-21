import sys
n = int(sys.stdin.readline())

for i in range(n):
    stack = []
    line = sys.stdin.readline()
    for x in line:
        if x == ' ' or x == '\n':
            while(len(stack)):
                print(stack.pop(), end="")
            print(x, end="")
        else:
            stack.append(x)
