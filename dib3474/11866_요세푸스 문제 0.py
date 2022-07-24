import sys

N, K = map(int, sys.stdin.readline().split())

q = []
for i in range(1, N+1):
    q.append(i)

print("<", end="")
for i in range(N-1):
    for j in range(K-1):
        q.append(q.pop(0))
    print(f"{q.pop(0)}, ", end="")
print(f"{q.pop(0)}>")
