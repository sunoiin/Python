def solution(n):
    # answer = 0
    # for i in range(1, n + 1):
    #     if n % i == 0:
    #         answer += i

    # 두번째 방법: n//2까지만 약수를 구하고, n을 더해준다.
    answer = n
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            answer += i

    return answer


print(solution(12))  # 28
print(solution(5))  # 6
print(solution(3000))  # 9360
