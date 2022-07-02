# S = input()

def reverse(S):
    answer = []

    # 0으로 뒤집기
    cnt = 0
    if S.count('0') == len(S):
        answer.append(cnt)
    else:
        for i in range(len(S)):
            if S[i] == '1' and i == len(S)-1:
                cnt += 1
                break
            if S[i] == '1' and S[i+1] == '0':
                cnt += 1
        answer.append(cnt)

    # 1로 뒤집기
    cnt = 0
    if S.count('1') == len(S):
        answer.append(cnt)
    else:
        for i in range(len(S)):
            if S[i] == '0' and i == len(S)-1:
                cnt += 1
                break
            if S[i] == '0' and S[i+1] == '1':
                cnt += 1
        answer.append(cnt)

    return min(answer)


print(reverse('0001100'))  # 1
print(reverse('11111'))  # 0
print(reverse('00000001'))  # 1
print(reverse('11001100110011000001'))  # 4
print(reverse('11101101'))  # 2
