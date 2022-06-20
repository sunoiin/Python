def solution(str1, str2):
    answer = 0
    # 교집합 크기 / 합집합 크기

    str1 = str1.upper()
    str2 = str2.upper()
    print(str1, str2)

    str1_pair = []
    str2_pair = []

    # str1 글자 쌍
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():  # 앞뒤 글자가 영어일 때만
            str1_pair.append(str1[i]+str1[i+1])

    # str2 글자 쌍
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_pair.append(str2[i]+str2[i+1])

    print('str1_pair', str1_pair)
    print('str2_pair', str2_pair)

    # A, B 모두 공집합 -> J(A, B) = 1 return
    if len(str1_pair + str2_pair) == 0:
        return 65536

    intersection = []
    # union_cnt = len(str1_pair)
    for i in str1_pair:
        if i in str2_pair:
            intersection.append(i)
            str2_pair.remove(i)
    print(intersection)

    # print(inter_cnt, union_cnt)
    # print(inter_cnt / union_cnt * 65536)

    answer *= 65536

    return answer


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
