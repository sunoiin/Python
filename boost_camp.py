def solution(arr):
    result = []

    arr_count = [0 for _ in range(101)]

    # 앞의 숫자들부터 나타나는 횟수를 저장
    for i in arr:
        arr_count[i] += 1

    # 중복되는 숫자가 없을 경우 -1 반환
    if max(arr_count) < 2:
        return [-1]

    # 숫자의 중복을 제거해주기 위해 set(arr) 생성
    arr_set = set(arr)

    # 숫자가 나타나는 횟수가 2 이상일 경우 result 리스트에
    if arr_count[i] >= 2:
        result.append(arr_count[i])

    return result


print(solution([1, 2, 3, 3, 3, 3, 4, 4]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8]))
