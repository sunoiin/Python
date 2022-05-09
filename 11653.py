n = int(input())

# while(True):
#     for i in range(2, n+1):
#         if n % i == 0:
#             print(i)
#             n //= i
#             break
#         if i == n:
#             break


a = True
while(a):
    i = 2
    while(a):
        if n % i == 0:
            print(n, i)
            n //= i
            continue
        i += 1
        if i == n:
            a = False
    if i == n:
        a = False
        break
