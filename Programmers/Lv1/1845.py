def solution(nums):
    answer = min(len(nums)//2, len(set(nums)))
    return answer


print(solution([3, 1, 2, 3]))  # 2
print(solution([3, 3, 3, 2, 2, 4]))  # 3
print(solution([3, 3, 3, 2, 2, 2]))  # 2
