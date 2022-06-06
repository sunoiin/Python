def solution(absolutes, signs):
    answer = 0

    # for i in range(len(absolutes)):
    #     if signs[i]==True:
    #         answer+=absolutes[i]
    #     else:
    #         answer-=absolutes[i]

    for absolute, sign in zip(absolutes, signs):
        if sign:
            answer += absolute
        else:
            answer -= absolute

    return answer
