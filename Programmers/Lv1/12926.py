def solution(s, n):
    answer = ''
    cap_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_alpha = 'abcdefghijklmnopqrstuvwxyz'

    for i in s:
        if i.islower():
            idx = small_alpha.index(i)
            if idx + n < 26:
                answer += small_alpha[idx + n]
            else:
                answer += small_alpha[(idx + n) % 26]

        elif i.isupper():
            idx = cap_alpha.index(i)
            if idx + n < 26:
                answer += cap_alpha[idx + n]
            else:
                answer += cap_alpha[(idx + n) % 26]
        else:  # 공백일 경우
            answer += i
    return answer


print(solution('AB', 1))  # 'BC'
print(solution('z', 1))  # 'a'
print(solution('a B z', 4))  # 'e F d'
