n = int(input())

sum = 1
i = 1

while(n != 1):
    sum += 6*i
    if sum >= n:
        break
    i += 1

if n == 1:
    print(1)
else:
    print(i+1)
