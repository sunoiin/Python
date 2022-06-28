# 던전 8개 이하 -> 완전탐색

from itertools import permutations


def solution(k, dungeons):
    answer = -1
    result = []

    # 가능한 던전 방문 순서(순열)을 리스트로 생성
    orders = list(permutations(dungeons, len(dungeons)))

    for order in orders:
        cnt = 0
        tmp_k = k
        for i in range(len(order)):
            # 던전 최소 필요 필요도가 남아있는 피로도보다 작을 때, 방문처리
            if order[i][0] <= tmp_k:
                cnt += 1
                tmp_k -= order[i][1]
            else:
                break
        result.append(cnt)

    # 순열 중 가장 높은 방문횟수를 리턴
    answer = max(result)
    return answer
