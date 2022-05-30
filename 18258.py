from collections import deque
from sys import stdin

queue = deque()
N = int(stdin.readline())

for _ in range(N):
    order = list(stdin.readline().split())

    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        print(0 if queue else 1)
    elif order[0] == 'front':
        print(queue[0] if queue else -1)
    elif order[0] == 'back':
        print(queue[-1] if queue else -1)
