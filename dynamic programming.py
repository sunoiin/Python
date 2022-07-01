d = [0]*10


def dp(x):
    if x == 1:
        print(x, d)
        return 1
    if x == 2:
        print(x, d)
        return 1
    if d[x] != 0:  # 이미 계산되어 저장된 값을 return
        print(x, d)
        return d[x]
    d[x] = dp(x-1)+dp(x-2)
    print(x, d)
    return d[x]


print(dp(5))
