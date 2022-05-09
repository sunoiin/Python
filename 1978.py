import sys


n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

cnt = 0
for num in numbers:
    prime_number = True
    if num < 2:
        continue
    else:
        for i in range(2, num-1):
            if num % i == 0:
                prime_number = False
                break
    if prime_number == True:
        cnt += 1
print(cnt)
