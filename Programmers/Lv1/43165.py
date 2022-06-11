from itertools import *


def solution(numbers, target):
    answer = 0
    sub = (sum(numbers) - target)//2

    # numbers = [i for i in numbers if i <= sub]

    for i in range(1, len(numbers)+1):
        per = list(combinations(numbers, i))
        for j in per:
            if sum(j) == sub:
                answer += 1

    return answer

# 우선 기호가 모두 +라고 가정했을 때, numbers의 총 합에서 target 값을 뺀 차를 sub라고 한다.
# target 값으로 만들려면 sub만큼을 빼줘야 하는데,
# [4, 1, 2, 1]의 경우 합이 8이 되고, 4를 제외한 모든 원소를 -로 만드는게 아니라, 나머지 원소들끼리의 합을 0으로 만들어야 한다.
# 이 문제에서는 target 값이 만들어지지 않는 경우는 없으므로 (target 값이 되는 합이 반드시 존재하므로), 원소들의 조합이 sub/2가 되는 경우의 수를 구하면 된다.
