def solution(s):
    answer = ''

    # Point: 각 단어는 하나 '이상'의 공백 문자로 구분되어 있다. ^^
    # Solution: 공백이 두개 이상일 때, 문자열을 분리해주기 위해서 cnt 변수를 사용한다.

    cnt = 0  # 문자열 내에서 몇번째 문자 인지 표시해주기 위한 변수
    for c in s:
        cnt += 1
        if c == ' ':  # 공백 문자일 경우 answer에 추가하고, cnt를 1로 초기화
            answer += c
            cnt = 0
            continue
        if cnt % 2 == 1:
            answer += c.upper()  # 홀수번째 문자일 경우 대문자로 바꿔서 answer에 추가
        else:
            answer += c.lower()  # 짝수번째 문자일 경우 소문자로 바꿔서 answer에 추가

    return answer


print(solution('try hello world'))  # TrY HeLlO WoRlD
print(solution('TRY HELLO WORLD'))  # TrY HeLlO WoRlD
print(solution('try  hello   world'))  # TrY  HeLlO   WoRlD
print(solution('hI'))  # Hi
