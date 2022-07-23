import sys

N = int(sys.stdin.readline())

Queue = []


for i in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        Queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(Queue) != 0:
            print(Queue.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(Queue))
    elif cmd[0] == 'empty':
        if len(Queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(Queue) != 0:
            print(Queue[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(Queue) != 0:
            print(Queue[-1])
        else:
            print(-1)
