def solution(expression):
    answer = 0

    # 숫자/연산자 를 원소로 포함하는 리스트 생성하기
    list_expression = []
    num = ''
    for c in expression:
        if c.isdecimal():
            num += c
        else:
            list_expression.append(num)
            list_expression.append(c)
            num = ''
    list_expression.append(num)

    # * > +,- 순서로 계산

    # +,- > * 순서로 계산

    print(list_expression)

    # 결과가 음수라면 절댓값으로 제출
    return answer


print(solution("100-200*300-500+20"))  # 60420
print(solution("50*6-3*2"))  # 300
