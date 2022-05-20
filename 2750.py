n = int(input())
num = list()

for _ in range(n):
    num.append(int(input()))

# Bubble Sort
# for i in range(n):
#     for j in range(n-1):
#         if num[j] > num[j+1]:
#             num[j], num[j+1] = num[j+1], num[j]

# Selection Sort
# for i in range(n):
#     min = i
#     for j in range(i+1, n):
#         if num[j] < num[min]:
#             min = j
#     num[i], num[min] = num[min], num[i]

# Insertion Sort
for end in range(1, len(num)):  # Index 1부터 마지막까지 비교 (1,0 / 2,1,0 / 3,2,1,0 / ...)
    for i in range(end, 0, -1):  # Index 끝에서부터 왼쪽으로 비교
        if num[i-1] > num[i]:  # 왼쪽 원소가 더 크면, 자리 바꾸기
            num[i-1], num[i] = num[i], num[i-1]


for i in num:
    print(i)
