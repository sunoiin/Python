def solution(progresses, speeds):
    answer = []
    day = 0

    while (progresses):
        day += 1

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        if progresses[0] < 100:
            continue

        task = 0
        while progresses and progresses[0] >= 100:
            progresses = progresses[1::]
            speeds = speeds[1::]
            task += 1
        print("day", day, "task", task)
        answer.append(task)
    return answer


# print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
