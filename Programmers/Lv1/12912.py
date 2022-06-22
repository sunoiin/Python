def solution(a, b):
    # a와 b가 같은 경우는 둘 중 아무 수나 리턴한다.
    if a == b:
        return a
    # a가 더 클 경우 swap 해준다.
    if b < a:
        a, b = b, a

    answer = sum(range(a, b+1))
    return answer


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
print(solution(-5000000, 3000000))
