from itertools import permutations

# 소수 판별 함수. 소수일 경우 True / 소수가 아닐 경우 False


def isPrime(num):
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0

    made_numbers = set()
    for i in range(1, len(numbers) + 1):
        # 종이 조각의 문자별 집합을 구해서 join시켜 하나의 문자열로 만들고, int형으로 변환한다.
        # set 자료형을 썼기 때문에 합집합으로 추가해주면, 중복은 자동 처리 됨.
        made_numbers |= set(
            map(int, map(''.join, set(permutations(numbers, i)))))

    # 0~1 범위는 소수에 포함되지 않으므로 차집합으로 제외해주기
    made_numbers -= set([0, 1])

    for i in made_numbers:
        if isPrime(int(i)):
            answer += 1

    return answer


print(solution('17'))  # 3
print(solution('011'))  # 2
