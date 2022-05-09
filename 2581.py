m = int(input())
n = int(input())

sum = 0
prime_numbers = []
for num in range(m, n+1):
    if num == 2:
        sum += num
        prime_numbers.append(num)
    else:
        for i in range(2, num):
            if num % i == 0:
                # 소수 아님
                break
            if i == num-1:
                sum += num
                prime_numbers.append(num)

if(prime_numbers):
    print(sum)
    print(min(prime_numbers))
else:
    print(-1)
