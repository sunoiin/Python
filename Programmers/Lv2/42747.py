def solution(citations):
    # 논문 갯수가 n개 일 때, h-index는 반드시 n보다 높다. [22, 24] -> 2 / [3] -> 1
    answer = len(citations)

    citations.sort(reverse=True)

    for i in range(len(citations)):

        # 논문 인용 횟수가 인덱스 값(편 수)보다 작아지는 경우 , i return
        if citations[i] < i + 1:
            answer = i
            break

    return answer


print(solution([3, 0, 6, 1, 5]))  # 3
print(solution([1, 1, 1, 1, 1]))  # 1
print(solution([1, 2, 2, 3, 4, 4, 5]))  # 3
print(solution([22, 24]))
print(solution([3]))
