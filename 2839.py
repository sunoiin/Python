n = int(input())

# a: 3kg 봉지
# b: 5kg 봉지

b = n//5
a = n-b*5
while (True):
    if b == 0 or a % 3 == 0:
        break
    b -= 1
    a = n-b*5
a = a//3

if a*3+b*5 == n:
    # print(f"3kg:{a}, 5kg:{b}")
    print(a+b)
else:
    print(-1)
