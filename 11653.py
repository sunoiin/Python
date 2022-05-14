n = int(input())

# while(n != 1):
#     for i in range(2, n+1):
#         if n == i:
#             break
#         if n % i == 0:
#             print(i)
#             n //= i
#             break
#     if n == i:
#         print(i)
#         break

for i in range(2, n+1):
    while n % i == 0:
        print(i)
        n /= i
