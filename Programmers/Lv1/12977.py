def solution(nums):
    answer = 0

    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                isPrime = True
                for l in range(2, num):
                    if num % l == 0:
                        isPrime = False
                if isPrime:
                    answer += 1
    return answer
