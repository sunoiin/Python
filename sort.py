n = int(input())
num = list()

for _ in range(n):
    num.append(int(input()))

# Bubble Sort
# for i in range(n):
#     for j in range(i+1, n):
#         if num[j] < num[i]:
#             num[j], num[i] = num[i], num[j]
#     print(*num)

# Selection Sort
# for i in range(n):
#     min = i
#     for j in range(i+1, n):
#         if num[j] < num[min]:
#             min = j
#     num[i], num[min] = num[min], num[i]

# Insertion Sort
for end in range(1, n):
    for i in range(end, 0, -1):
        if num[i-1] > num[i]:
            num[i-1], num[i] = num[i], num[i-1]
    print(*num)
