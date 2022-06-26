def solution(bridge_length, weight, truck_weights):
    # 다리 길이 bridge_length : 트럭은 1초에 1칸씩 전진한다. (bridge_length 초 지나면 건너기 완료)
    # 다리에 올라가는 트럭 수 최대 bridge_length
    # 다리가 견디는 무게 최대 weight (완전히 오른 트럭만 고려)

    num_of_truck = len(truck_weights)
    on_bridge = []
    passed_truck = []
    time_of_truck = []
    time = 0

    while (len(passed_truck) < num_of_truck):
        time += 1

        # 다리 위 트럭이 존재하고, 첫번째 트럭이 bidge length 만큼 지나갔으면, 다리 건너기
        if on_bridge:
            if time_of_truck[0] == bridge_length:
                passed_truck.append(on_bridge.pop(0))
                time_of_truck.pop(0)

        # 대기 트럭이 존재하고, 현재 다리 무게 + 첫번째 대기 트럭 무게가 weight보다 같거나 작으면, 트럭 한대 추가
        if truck_weights:
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights.pop(0))
                time_of_truck.append(0)

        # 다리 위 모든 트럭이 1초, 1만큼 전진
        time_of_truck = [i+1 for i in time_of_truck]

        print(
            f"{time}s: {passed_truck} | {on_bridge} | {time_of_truck} | {truck_weights}")

    answer = time

    return answer

# # Deque 라이브러리 사용
# from collections import deque


# def solution(bridge_length, weight, truck_weights):
#     # 다리 길이 bridge_length : 트럭은 1초에 1칸씩 전진한다. (bridge_length 초 지나면 건너기 완료)
#     # 다리에 올라가는 트럭 수 최대 bridge_length
#     # 다리가 견디는 무게 최대 weight (완전히 오른 트럭만 고려)

#     num_of_truck = len(truck_weights)
#     truck_weights = deque(truck_weights)
#     on_bridge = deque()
#     passed_truck = []
#     time_of_truck = deque()
#     time = 0

#     while (len(passed_truck) < num_of_truck):
#         time += 1

#         # 다리 위 트럭이 존재하고, 첫번째 트럭이 bidge length 만큼 지나갔으면, 다리 건너기
#         if on_bridge:
#             if time_of_truck[0] == bridge_length:
#                 passed_truck.append(on_bridge.popleft())
#                 time_of_truck.popleft()

#         # 대기 트럭이 존재하고, 현재 다리 무게 + 첫번째 대기 트럭 무게가 weight보다 같거나 작으면, 트럭 한대 추가
#         if truck_weights:
#             if sum(on_bridge) + truck_weights[0] <= weight:
#                 on_bridge.append(truck_weights.popleft())
#                 time_of_truck.append(0)

#         # 다리 위 모든 트럭이 1초, 1만큼 전진
    # for i in range(len(time_of_truck)):
    #   time_of_truck[i] += 1

#         # print(
#         #     f"{time}s: {passed_truck} | {on_bridge} | {time_of_truck} | {truck_weights}")

#     answer = time

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
