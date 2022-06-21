def solution(str1, str2):
    answer = 0
    # 교집합 크기 / 합집합 크기

    # 대문자와 소문자의 차이는 무시 -> 모두 대문자로 변환
    str1 = str1.upper()
    str2 = str2.upper()

    # str1 글자 쌍 리스트
    A_pair = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():  # 앞뒤 글자가 영어일 때만 리스트에 추가 (공백, 숫자, 특수문자 무시)
            A_pair.append(str1[i]+str1[i+1])

    # str2 글자 쌍 리스트
    B_pair = []
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            B_pair.append(str2[i]+str2[i+1])

    # A, B 모두 공집합일 경우 -> J(A, B): return 1
    if len(A_pair + B_pair) == 0:
        return 65536

    # 교집합 합집합 리스트 생성
    intersection = []
    A_pair_tmp = A_pair.copy()
    B_pair_tmp = B_pair.copy()

    for i in A_pair:
        if i in B_pair_tmp:
            intersection.append(i)
            B_pair_tmp.remove(i)

    for i in intersection:
        A_pair_tmp.remove(i)

    # 합집합 - 교집합 = 0 일 때: A = B 이므로 return 1
    if len(A_pair_tmp + B_pair_tmp) == 0:
        return 65536

    answer = int(len(intersection) / len(A_pair_tmp +
                 B_pair_tmp + intersection) * 65536)

    return answer


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
