def solution(expression):
    answer = []

    # 부호와 숫자를 분리하여 리스트 생성
    exp_split = ['+']  # 계산상 편의를 위해 맨 앞에 + 붙여주기
    num = ''
    for c in expression:
        if c.isdecimal():
            num += c
        else:
            exp_split.append(num)
            exp_split.append(c)
            num = ''
    exp_split.append(num)
    # print(exp_split)

    # * > +,-
    stack = []
    for i in range(len(exp_split)):
        if exp_split[i-1] == '*':
            stack.pop()
            left_num = stack.pop()
            stack.append(str(int(left_num) * int(exp_split[i])))
        else:
            stack.append(exp_split[i])
    # print(stack)

    result = 0
    for i in range(len(stack)):
        if stack[i-1] == '+':
            result += int(stack[i])
        elif stack[i-1] == '-':
            result -= int(stack[i])
    answer.append(abs(result))

    # +,- > *
    stack = []
    for i in range(1, len(exp_split)):
        if i == 1:
            stack.append(exp_split[i])
            continue

        if exp_split[i-1] == '+':
            stack.pop()
            left_num = stack.pop()
            stack.append(str(int(left_num) + int(exp_split[i])))
        elif exp_split[i-1] == '-':
            stack.pop()
            left_num = stack.pop()
            stack.append(str(int(left_num) - int(exp_split[i])))
        else:
            stack.append(exp_split[i])
    # print(stack)

    result = 1
    for i in range(len(stack)):
        if stack[i] == '*':
            continue
        result *= int(stack[i])
    answer.append(abs(result))
    # print(result)

    # + > * > -

    stack = []
    for i in range(len(exp_split)):
        if i < 2:
            stack.append(exp_split[i])
            continue

        if exp_split[i-1] == '+':
            stack.pop()
            left_num = stack.pop()
            stack.append(str(int(left_num) + int(exp_split[i])))
        else:
            stack.append(exp_split[i])
    # print(stack)

    new_stack = []
    for i in range(len(stack)):
        if stack[i-1] == '*':
            new_stack.pop()
            left_num = new_stack.pop()
            new_stack.append(str(int(left_num) * int(stack[i])))
        else:
            new_stack.append(stack[i])
    # print(new_stack)

    result = 0
    for i in range(len(new_stack)):
        if new_stack[i-1] == '+':
            result += int(new_stack[i])
        elif new_stack[i-1] == '-':
            result -= int(new_stack[i])
    answer.append(abs(result))

    # - > * > +

    stack = []
    for i in range(len(exp_split)):
        if i < 2:
            stack.append(exp_split[i])
            continue

        if exp_split[i-1] == '-':
            stack.pop()
            left_num = stack.pop()
            stack.append(str(int(left_num) - int(exp_split[i])))
        else:
            stack.append(exp_split[i])
    print(stack)

    new_stack = []
    for i in range(len(stack)):
        if stack[i-1] == '*':
            new_stack.pop()
            left_num = new_stack.pop()
            new_stack.append(str(int(left_num) * int(stack[i])))
        else:
            new_stack.append(stack[i])
    # print(new_stack)

    result = 0
    for i in range(len(new_stack)):
        if new_stack[i-1] == '+':
            result += int(new_stack[i])
    answer.append(abs(result))

    return max(answer)


print(solution('100-200*300-500+20'))
print(solution('50*6-3*2'))
