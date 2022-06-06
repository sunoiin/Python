def solution(participant, completion):
    answer = ""

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer

    answer = participant[-1]
    return answer

    # 아래 풀이는 시간초과 코드
    # for name in participant:
    #     if participant.count(name) != completion.count(name):
    #         answer=name
