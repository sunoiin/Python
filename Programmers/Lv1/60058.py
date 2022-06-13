def solution(p):
    answer = ""

    new_p = p
    while(True):
        if new_p == "":
            return
        u = ""
        for i in new_p:
            u += i
            if u.count("(") == u.count(")"):
                break
        v = new_p[len(u):]

        print("u", u, "v", v)

        stack = ""
        for j in u:
            stack += j
            if len(stack) >= 2:
                if stack[-2] == "(" and i == ")":
                    stack.pop()
                    stack.pop()
        print("stack", stack)

        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
        if stack == "":
            print(u, "올바른 괄호 문자열 맞음")
            answer += u
            new_p = v
        else:
            print(u, "올바른 괄호 문자열 아님")
            new_p = v

    return answer


# print(solution("(()())()"))
print(solution(")("))
# print(solution("()))((()"))
