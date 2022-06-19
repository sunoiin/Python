def solution(dartResult):
    stack = []
    num = ''
    area = {'S': 1, 'D': 2, 'T': 3}
    for i in range(len(dartResult)):
        # 숫자가 나오면 숫자를 변수 num에 저장
        if dartResult[i].isdigit():
            num += dartResult[i]
        # 숫자가 아닌 문자일 때
        else:
            # 문자가 S/D/T라면 숫자를 거듭제곱하여 stack에 추가
            if dartResult[i] in area:
                stack.append(int(num) ** area[dartResult[i]])

            # 문자가 */#라면 그 전까지의 점수들을 상에 맞게 처리
            if dartResult[i] == '*':
                stack[-1] = 2 * stack[-1]
                if len(stack) > 1:
                    stack[-2] = 2 * stack[-2]
            elif dartResult[i] == '#':
                stack[-1] = -stack[-1]
            print(dartResult[i], stack)

            # 숫자를 초기화
            num = ''

    answer = sum(stack)
    return answer


print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# print(solution('1S*2T*3S'))
# print(solution('1D#2S*3S'))
# print(solution('1T2D3D#'))
# print(solution('1D2S3T*'))
