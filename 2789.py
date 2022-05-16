# from itertools import combinations

# n, m = map(int, input().split())
# cards = list(map(int, input().split()))

# combs = list(combinations(cards, 3))

# max_sum = 0
# for comb in combs:
#     if sum(comb) > max_sum and sum(comb) <= m:
#         max_sum = sum(comb)

# print(max_sum)

n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i]+cards[j]+cards[k] > m:
                continue
            else:
                result = max(result, cards[i]+cards[j]+cards[k])
print(result)
