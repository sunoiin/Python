# 최대공약수 구하는 함수
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def solution(w, h):
    answer = w*h - (w + h - gcd(w, h))

    return answer


print(solution(12, 8))
print(solution(8, 12))
print(solution(13, 7))
