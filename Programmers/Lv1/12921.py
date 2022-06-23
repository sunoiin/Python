def solution(n):
    answer = 0
    for x in range(2, n+1):
        isPrioty = True
        for j in range(2, int(x ** 0.5) + 1):
            if x % j == 0:
                isPrioty = False
                break
        if isPrioty == True:
            answer += 1
    return answer
