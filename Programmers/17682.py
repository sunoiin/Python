def solution(dartResult):
    stack = []
    num = ''
    area = {'S': 1, 'D': 2, 'T': 3}
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            num += dartResult[i]
        else:
            if dartResult[i] in area:
                stack.append(int(dartResult[i]) ** area[dartResult[i]])
                if dartResult[i] == '*':
                    stack[-1] = 2 * stack[-1]
                    if len(stack) > 1:
                        stack[-2] = 2 * stack[-2]
                elif dartResult[i] == '#':
                    stack[-1] = -stack[-1]
                print(dartResult[i], stack)
            print(num, stack)
            num = ''
    answer = sum(stack)
    return answer
