def solution(lottos, win_nums):
    answer = []

    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = 0
    for i in lottos:
        if i == 0:
            cnt_0 += 1

    cnt_win = 0
    for i in lottos:
        if i in win_nums:
            cnt_win += 1

    answer = [rank[cnt_win+cnt_0], rank[cnt_win]]

#     lower, zero = 0, 0
#     for i in lottos:
#         if i in win_nums:
#             lower += 1
#         if i == 0:
#             zero += 1
#     upper=lower+zero
#     rank=[upper,lower]

#     for r in rank:
#         if r==6:
#             answer.append(1)
#         elif r==5:
#             answer.append(2)
#         elif r==4:
#             answer.append(3)
#         elif r==3:
#             answer.append(4)
#         elif r==2:
#             answer.append(5)
#         else:
#             answer.append(6)

    # 당첨 가능한 최고 순위, 최저 순위
    return answer
