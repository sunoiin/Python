# 1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

# 필요한 것
# 1) 합
# 2) 최댓값, 최솟값
# 3) 정렬

from sys import stdin
import statistics

N = int(stdin.readline().rstrip())
num = list()
for _ in range(N):
    num.append(int(stdin.readline().rstrip()))

sorted_num = sorted(num)
num_sum = sum(num)
num_max = max(num)
num_min = min(num)

# 최빈값 구하기
# num_dict = {}
# for i in num:
#     num_dict[i] = num.count(i)

# max_count = max(num_dict.values())
# max_list = list()

# for value, count in num_dict.items():
#     if count == max_count:
#         max_list.append(value)

# if len(max_list) == 1:
#     most = max_list[0]
# else:
#     most = sorted(max_list)[1]

mode = statistics.multimode(sorted_num)

# print("산술평균:", round(num_sum/N))
# print("중앙값:", sorted(num)[(N-1)//2])
# print("최빈값:", most)
# print("범위:", num_max-num_min)
print(round(num_sum/N))
print(sorted_num[(N-1)//2])
print(mode[1] if len(mode) > 1 else mode[0])
# print(most)
print(num_max-num_min)
