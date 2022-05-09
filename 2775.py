# # 3: 1 5 15 35 70 126
# # 2: 1 4 10 20 35 56
# # 1: 1 3 6  10 15 21
# # 0: 1 2 3  4  5  6

t = int(input())

for _ in range(t):
    floor = int(input())  # 층수
    num = int(input())  # 호수
    floor_0 = [x for x in range(1, num+1)]  # 0층

    for k in range(floor):
        for i in range(1, num):
            floor_0[i] += floor_0[i-1]
        print(floor_0)
    print(floor_0[-1])
