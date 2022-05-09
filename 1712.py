a, b, c = map(int, input().split())

# a: 고정비용
# b: 가변 비용 / 1대
# c: 노트북 가격

# 시간제한: 0.35초 -> 시간 문제

if c == b:
    print(-1)
else:
    n = a//(c-b)
    n += 1

    if (a+b*n >= c*n):
        print(-1)
    else:
        print(n)
