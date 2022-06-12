def solution(p):
    answer = [0 for i in range(len(p))]
    n = len(p)
    for i in range(0, n):
        min_num = (min(p[i:]))
        for j in range(i, n):
            if p[j] == min_num:
                break
        if i != j:
            tmp = p[j]
            p[j] = p[i]
            p[i] = tmp
            answer[i] += 1
            answer[j] += 1
    print(p)
    print(answer)
    return answer


# solution([2, 5, 3, 1, 4])
# solution([5, 4, 3, 2, 1])
