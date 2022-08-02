import sys

stack = []
line = sys.stdin.readline()

flag = 0
for x in line:
    if flag == 0:
        if x == '<':
            while(len(stack)):
                    print(stack.pop(), end="")
            print(x, end="")
            flag = 1
        elif x == ' ' or x == '\n':
                while(len(stack)):
                    print(stack.pop(), end="")
                print(x, end="")
        else:
            stack.append(x)

    elif flag == 1:
        if x == ">":
            while(len(stack)):
                print(stack.pop(0), end="")
            print(x, end="")
            flag = 0
        else:
            stack.append(x)
