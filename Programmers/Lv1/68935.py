def solution(n):
    ternary = ""

    # while(True):
    #     remainder = n % 3
    #     n //= 3
    #     ternary = str(remainder) + ternary
    #     if n == 0:
    #         break

    # 3진법을 뒤집어서 10진법으로 바꿔야 하므로, 애초에 뒤집은 3진법을 바로 구하자
    while(n):
        remainder = n % 3
        n //= 3
        ternary += str(remainder)

    answer = int(ternary, 3)
    # ---- 아래 코드를 위 한줄로 대체 가능 ----
    # j = 1
    # for i in ternary:
    #     answer += j * int(i)
    #     j *= 3

    return answer


print(solution(45))  # 7
print(solution(125))  # 229
