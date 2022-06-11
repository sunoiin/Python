# Queue FIFO를 활용한 풀이
# 입출력 순서에 대한 언급이 있다면 stack / queue 가능성 있으므로, pop 활용하여 풀어보기
def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0
    while progresses:
        if progresses[0]+day*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
