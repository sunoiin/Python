def solution(numbers):
    answer = ''

    # 3, 30, 34를 비교하는 경우 -> 4자리까지 반복하여 정렬하면 됨.
    # 3333, 3030, 3434 -> 3434, 3333, 3030 -> 34, 3, 30

    # 네자리 반복을 담은 배열
    num_to_fourth = [(str(num) * 4)[:4] for num in numbers]

    # 원래 원소를 네자리 반복 기준으로 내림차순 정렬
    zip_number = list(zip(numbers, num_to_fourth))
    # 자릿수를 네자리로 맞췄으므로 str, int 정렬기준은 동일함.
    zip_number = sorted(zip_number, key=lambda x: int(x[1]), reverse=True)
    # print(zip_number)

    # 정렬된 원소를 순서대로 answer에 이어 붙이기
    for num, _ in zip_number:
        answer += str(num)

    # (예외) 0으로만 이루어진 배열일 경우, 자릿수에 상관 없이 0 return
    if int(answer) == 0:
        answer = '0'

    return answer


print(solution([6, 10, 2]))  # "6210"
print(solution([3, 30, 34, 5, 9]))  # "9534330"
print(solution([00, 000, 0]))  # "0"
