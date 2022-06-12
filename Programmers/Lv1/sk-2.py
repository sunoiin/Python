def solution(periods, payments, estimates):
    answer = [0, 0]
    n = len(periods)  # 고객 수
    vip_current = []
    vip_next = []

    for i in range(n):
        # print(periods[i], sum(payments[i]))
        if periods[i] < 24:
            vip_current.append(False)
        elif periods[i] < 60:
            if sum(payments[i]) >= 900000:
                vip_current.append(True)
            else:
                vip_current.append(False)
        else:
            if sum(payments[i]) >= 600000:
                vip_current.append(True)
            else:
                vip_current.append(False)

    for i in range(n):
        new_payments = sum(payments[i][1:])+estimates[i]
        new_period = periods[i]+1
        print(new_period, new_payments)
        if new_period < 24:
            vip_next.append(False)
        elif new_period < 60:
            if new_payments >= 900000:
                vip_next.append(True)
            else:
                vip_next.append(False)
        else:
            if new_payments >= 600000:
                vip_next.append(True)
            else:
                vip_next.append(False)

    print(vip_current)
    print(vip_next)

    for i in range(n):
        if vip_current[i] == False and vip_next[i] == True:
            answer[0] += 1
        elif vip_current[i] == True and vip_next[i] == False:
            answer[1] += 1

    return answer


print(solution(
    [20, 23, 24],
    [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
        [100000, 100000, 100000, 100000, 100000, 100000,
            100000, 100000, 100000, 100000, 100000, 100000],
     [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]],
    [100000, 100000, 100000]))
