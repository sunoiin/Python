# N, K = map(int, input().split())
# people = [i for i in range(1, N+1)]

# remove_people = K-1
# cnt = 0
# print("<", end="")
# while(people):
#     cnt += 1
#     K_cnt = 0
#     while(True):
#         if K_cnt == K-1:
#             break
#         people.append(people[0])
#         people.pop(0)
#         K_cnt += 1
#     if cnt >= N:
#         print(str(people.pop(0)), end="")
#     else:
#         print(str(people.pop(0))+", ", end="")
# print(">")

from collections import deque

N, K = map(int, input().split())
people = deque([i for i in range(1, N+1)])

cnt = 0
print("<", end="")
while(people):
    cnt += 1
    for i in range(K-1):
        people.append(people.popleft())
    if cnt == N:
        print(str(people.popleft()), end="")
    else:
        print(str(people.popleft())+", ", end="")
print(">")
