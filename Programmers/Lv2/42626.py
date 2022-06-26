# import heapq


# def solution(scoville, K):
#     answer = 0
#     heap = []
#     for num in scoville:
#         heapq.heappush(heap, num)

#     while heap[0] < K:
#         if len(heap) < 2:
#             return -1
#         heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap)*2)
#         answer += 1
#     return answer


import heapq


def solution(scoville, K):
    answer = 0

    # heapq.heapify(x) : 리스트 x를 heap으로 변환
    heapq.heapify(scoville)

    while(scoville[0] < K):  # 가장 맵지 않은 음식의 스코빌 지수가 K보다 작을 때
        if len(scoville) < 2:  # 음식이 1개 남을 때 -> 더이상 섞을 수 없다.
            return -1

        # heapq.heappop(heap) : heap에서 가장 작은 원소를 pop % return
        # heapq.heappush(heap, item) : item을 heap에 추가
        heapq.heappush(scoville, heapq.heappop(
            scoville) + heapq.heappop(scoville)*2)
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2, 1, 1, 1, 1], 31))
