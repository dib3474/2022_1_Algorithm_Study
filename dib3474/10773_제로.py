import sys

k = int(sys.stdin.readline())
stack = []
for i in range(k):
    temp = int(sys.stdin.readline())
    if temp == 0 and len(stack) > 0:
        stack.pop()
    else:  
        stack.append(temp)

print(sum(stack))
