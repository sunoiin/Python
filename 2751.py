import sys

n = int(sys.stdin.readline())
num = list()

for _ in range(n):
    num.append(int(sys.stdin.readline().rstrip()))

num.sort()
# num = sorted(num)

for i in num:
    print(i)
