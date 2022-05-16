n = int(input())
min = abs(n-9*len(str(n)))

# for i in range(min, n+1):
#     sum = i+(i//1000000 % 10)+(i//100000 % 10)+(i//10000 % 10) + \
#         (i//1000 % 10)+(i//100 % 10)+(i//10 % 10)+(i % 10)
#     if n == sum:
#         print(i)
#         break
#     if n == i:
#         print(0)
#         break
#     i += 1

result = 0
for i in range(min, n+1):
    a = list(map(int, str(i)))
    result = i+sum(a)
    if result == n:
        print(i)
        break

if result != n:
    print(0)
