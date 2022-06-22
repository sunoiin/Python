def solution(seoul):
    # 'Kim'은 오직 한 번 나타난다.
    x = seoul.index('Kim')
    answer = f'김서방은 {x}에 있다'
    return answer


print(solution(['Jane', 'Kim']))  # '김서방은 1에 있다'
