def solution(n, arr1, arr2):
    answer = []
    board = [' ', '#']
    for i, j in zip(arr1, arr2):
        line = ''
        result = str(bin(i | j)[2:])
        if len(result) < n:
            result = '0' * (n - len(result)) + result
        for c in result:
            line += board[int(c)]
        answer.append(line)

    # answer = []
    # for i, j in zip(arr1, arr2):
    #     a12 = str(bin(i|j)[2:])
    #     a12 = a12.rjust(n, '0')
    #     a12 = a12.replace('1', '#')
    #     a12 = a12.replace('0', ' ')
    #     answer.append(a12)

    return answer


print(*solution(5, [9, 20, 28, 18, 11],	[30, 1, 21, 17, 28]), sep='\n')
print(*solution(6, [46, 33, 33, 22, 31, 50],
      [27, 56, 19, 14, 14, 10]), sep='\n')
