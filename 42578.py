def solution(clothes):
    # 의상의 종류별 갯수 / 의상의 이름 (한가지)

    # 선그리 1개, 모자 2개
    # (0, 1) (0, 1, 2) -> 2*3에서 (0, 0) 인 경우는 없으므로 2*3-1 = 5
    # (선그리 갯수 + 1) * (모자 갯수 + 1) - 1

    # 의상수 30개 이하니까 반복문 써도 됨.

    # 의상 종류 리스트 만들기
    cnt_of_type = {}
    for clothe in clothes:
        if clothe[1] not in cnt_of_type:
            cnt_of_type[clothe[1]] = 1
        else:
            cnt_of_type[clothe[1]] += 1
    # print(cnt_of_type)

    answer = 1
    for value in cnt_of_type.values():
        answer *= (value + 1)
    answer -= 1

    # 예외: 만약 옷 종류가 1개라면? -> 하루에 한 개의 의상은 꼭 입어야 하니까 성립 X

    return answer


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))  # 5
print(solution([["crowmask", "face"], [
      "bluesunglasses", "face"], ["smoky_makeup", "face"]]))  # 3
