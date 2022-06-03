from sys import stdin


def solution(arr):
    arr_count = [0 for _ in range(101)]

    # 앞의 숫자들부터 나타나는 횟수를 저장
    for i in arr:
        arr_count[i] += 1

    # 숫자의 중복을 제거해주기 위해 set(arr) 생성
    arr_set = set(arr)

    # 숫자가 나타나는 횟수가 2 이상일 경우 result 리스트에 횟수를 차례대로 추가
    result = []
    for i in arr_set:
        if arr_count[i] >= 2:
            result.append(arr_count[i])

    # result가 비었을 때 [-1] return
    if not result:
        result = [-1]

    return result


arr = list(map(int, stdin.readline().rstrip().split()))
print(solution(arr))
