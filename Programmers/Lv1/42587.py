def solution(priorities, location):
    answer = 0

    printed = []  # 인쇄 순서대로 문서를 추가한 리스트
    locations = [i for i in range(len(priorities))]
    order = []

    while(priorities):
        # 만약 인쇄 대기목록의 첫번째 문서의 중요도가 max라면,
        # 문서를 인쇄하고, 문서의 위치를 인쇄 순서 목록 (order)에 추가한다.
        if priorities[0] == max(priorities):
            printed.append(priorities.pop(0))
            order.append(locations.pop(0))

        # 중요도가 뒤의 문서들보다 낮다면, 순서를 맨 뒤로 보낸다.
        else:
            priorities.append(priorities[0])
            locations.append(locations[0])
            priorities.pop(0)
            locations.pop(0)

    # 인쇄 순서에서 location의 인덱스 + 1 를 return한다.
    answer = order.index(location) + 1

    return answer


print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
print(solution([2, 1, 2, 1, 2, 1, 2, 1, 2], 1))  # 6
print(solution([1, 1, 1, 1, 1, 1], 3))  # 4
print(solution([2, 1, 2, 1, 2, 1, 2, 1, 2], 1))  # 6
