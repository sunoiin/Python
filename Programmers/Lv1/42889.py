def solution(N, stages):
    answer = []
    dict_stage = dict()

    for i in range(1, N+1):
        if max(stages) < i:
            dict_stage[i] = 0
            continue
        n_try = 0
        n_fail = 0
        for stage in stages:
            if stage == i:
                n_try += 1
                n_fail += 1
            elif stage > i:
                n_try += 1
        dict_stage[i] = n_fail/n_try
    # print(dict_stage)
    sorted_dict = sorted(dict_stage.items(),
                         key=lambda item: item[1], reverse=True)
    # print(sorted_dict)

    answer = [i[0] for i in sorted_dict]

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
