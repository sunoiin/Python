def solution(n):
    answer = ''
    n_array = ['1', '2', '4']

    while n > 0:
        # '0'이 존재하지 않으므로, 무조건 일의자리 수가 존재함.
        n = n-1
        answer += n_array[n % 3]
        n //= 3

    return answer[::-1]

# 10: 41
# 11: 32
# 12: 33
# 13: 111
