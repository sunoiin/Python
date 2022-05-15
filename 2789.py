from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

combs = list(combinations(cards, 3))

max_sum = 0
for comb in combs:
    if sum(comb) > max_sum and sum(comb) <= m:
        max_sum = sum(comb)

print(max_sum)
