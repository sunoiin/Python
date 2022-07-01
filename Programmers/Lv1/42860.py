def solution(name):
    answer = 0
    # 'A' 65 'Z' 90

    # 모든 경우의 수를 배열에 담아서 최소값 return
    result = []
    s_len = len(name)

    # 오른쪽으로 쭉 가는 경우
    cnt = 0
    for i in range(s_len):
        cnt += min(ord(name[i])-65, 91-ord(name[i]))
        if name[i+1:] == 'A'*(s_len-i-1):  # 남은 문자가 전부 A이면 중단
            break
        cnt += 1
    print(name, cnt)
    result.append(cnt)

    # 왼쪽으로 쭉 가는 경우
    cnt = 0
    left_name = name[0]+name[::-1][:-1]
    for i in range(s_len):
        cnt += min(ord(left_name[i])-65, 91-ord(left_name[i]))
        if left_name[i+1:] == 'A'*(s_len-i-1):  # 남은 문자가 전부 A이면 중단
            break
        cnt += 1
    print(left_name, cnt)
    result.append(cnt)

    # 오른쪽으로 갔다가 왼쪽으로 가는 경우
#     rev_name = name[::-1]
#     print(name)
#     for i in range(2, s_len):
#         print(name[:i], rev_name[-(i-1):], rev_name[:(s_len-i)])

    print(result)
    answer = min(result)
    return answer


"JEROEN"
