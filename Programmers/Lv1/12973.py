# 짝지어 제거하기

def solution(s):
    # 문자열의 길이가 홀수일경우 짝지어 제거하기 불가능, 바로 return
    if len(s) % 2 != 0:
        return 0

    stack = []

    for i in s:
        # stack이 비었을 경우 현재 문자를 추가한다.
        if len(stack) == 0:
            stack.append(i)
        # stack이 비어있지 않고, 마지막 문자가 현재 문자와 같을 경우 stack에서 제거한다.
        elif stack[-1] == i:
            stack.pop()
        # stack에 문자가 있지만 현재 문자와 같지 않을 경우 현재 문자를 추가한다.
        else:
            stack.append(i)

    # 문자열의 반복이 끝나고 stack이 비어있을 경우, 짝지어 제거하기 성공
    if len(stack) == 0:
        return 1
    # stack이 비어있지 않을 경우 짝지어 제거하기 실패
    else:
        return 0


print(solution('baabaa'))
print(solution('cdcd'))
