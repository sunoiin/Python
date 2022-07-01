def solution(x):
    sum_digits = 0
    for i in str(x):
        sum_digits += int(i)
    if x % sum_digits == 0:
        return True
    else:
        return False


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))
