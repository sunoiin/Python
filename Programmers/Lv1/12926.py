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

#     s = list(s)
#     for i in range(len(s)):
#         if s[i].isupper():
#             s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
#         elif s[i].islower():
#             s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

#     return "".join(s)


print(solution('AB', 1))  # 'BC'
print(solution('z', 1))  # 'a'
print(solution('a B z', 4))  # 'e F d'
