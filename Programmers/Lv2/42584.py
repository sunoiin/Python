def solution(prices):
    answer = [0 for _ in range(len(prices)-1)]

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            # 가격 떨어지지 않은 시간만큼 더하기
            answer[i] += 1
            # 처음 가격보다 가격이 떨어지는 경우, j-i초 동안 버텼다.
            if prices[i] > prices[j]:
                answer[i] = j-i
                break

    # 마지막 가격은 0초 버틴 것으로 본다.
    answer.append(0)

    return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([1, 1, 2, 2, 3]))
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 1, 2, 1]))
print(solution([5, 4, 3, 2, 1]))

# [4, 3, 1, 1, 0]
# [4, 3, 2, 1, 0]
# [4, 3, 2, 1, 0]
# [4, 1, 2, 1, 0]
# [1, 1, 1, 1, 0]
