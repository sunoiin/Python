def solution(n):
    answer = 0

    while (n > 0):
        answer += n % 10
        n //= 10

    return answer


print(solution(123))  # 6
print(solution(987))  # 24
print(solution(123456789))  # 45
