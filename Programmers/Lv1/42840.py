def solution(answers):
    answer = []

    person = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    person_cnt = [0, 0, 0, 0]

    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == person[i][j % len(person[i])]:
                person_cnt[i+1] += 1

    for i in range(1, 4):
        if person_cnt[i] == max(person_cnt):
            answer.append(i)
    answer.sort()

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
