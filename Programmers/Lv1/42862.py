def solution(n, lost, reserve):
    net_lost = set(lost)-set(reserve)
    net_reserve = set(reserve)-set(lost)
    answer = n-len(net_lost)

    for lost in net_lost:
        if (lost-1) in net_reserve:
            net_reserve.remove(lost-1)
            answer += 1
        elif (lost+1) in net_reserve:
            net_reserve.remove(lost+1)
            answer += 1
    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
