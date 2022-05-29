import math
from sys import stdin

N = list(map(int, stdin.readline().rstrip()))
count = [0 for _ in range(10)]

for i in N:
    count[i] += 1

six_nine = math.ceil((count[6]+count[9])/2)
if max(count) == count[6] or max(count) == count[9]:
    count[6] = six_nine
    count[9] = six_nine

print(max(count))
