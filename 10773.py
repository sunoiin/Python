from sys import stdin

k = int(stdin.readline())
num = list()

for i in range(k):
    n = int(stdin.readline())
    if n == 0:
        num.pop()
    else:
        num.append(n)
print(sum(num))
