def solution(n):
    answer = ''
    watermelon = '수박'

    # 첫번째 방법
    while (len(answer) < n):
        answer += watermelon
    if len(answer) == n + 1:
        answer = answer[:-1]

    # 두번째 방법
    # answer = watermelon * n
    # answer = answer[:n]

    return answer


print(solution(3))  # 수박수
print(solution(4))  # 수박수박
