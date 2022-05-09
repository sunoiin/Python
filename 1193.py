n = int(input())

sum = 0
i = 1
while(True):
    sum += i
    if sum >= n:
        break
    i += 1

diff = sum-n
if (i % 2 == 0):
    x = diff+1
    y = i-diff
else:
    y = diff+1
    x = i-diff

print(f"{y}/{x}")
