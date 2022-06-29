# 시험 감독

import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

answer = n
for i in range(n):
    a[i] -= b
    if a[i] > 0:
        answer += math.ceil(a[i]/c)
print(answer)
