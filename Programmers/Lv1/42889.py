# def solution(N, stages):
#     answer = []
#     dict_stage = dict()

#     for i in range(1, N+1):
#         if max(stages) < i:
#             dict_stage[i] = 0
#             continue
#         n_try = 0
#         n_fail = 0
#         for stage in stages:
#             if stage == i:
#                 n_try += 1
#                 n_fail += 1
#             elif stage > i:
#                 n_try += 1
#         dict_stage[i] = n_fail/n_try
#     # print(dict_stage)
#     sorted_dict = sorted(dict_stage.items(),
#                          key=lambda item: item[1], reverse=True)
#     # print(sorted_dict)

#     answer = [i[0] for i in sorted_dict]

#     return answer

def solution(N, stages):
    answer = []
    fail = []
    info = [0]*(N+2)  # 0~N+1까지의 stage
    for stage in stages:
        info[stage] += 1  # 0~N+1 까지 해당 stage에 있는 사람의 수
    print(info)
    for i in range(N):
        be = sum(info[(i+1):])  # stage를 지나간 유저
        yet = info[i+1]  # stage에 머물러 있는 유저
        if be == 0:
            fail.append((i+1, 0))
        else:
            fail.append((i+1, yet/be))
    print(fail)
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(item[0])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
