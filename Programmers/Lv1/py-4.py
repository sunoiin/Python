# . 평지 F 숲 # 강
def solution(grid, k):
    answer = -1
    new_grid = [list(grid[i]) for i in range(len(grid))]
    # print(*new_grid, sep="\n")
    r = len(grid)
    c = len(grid[0])
    # print(r, c)

    current_xy = [0, 0]
    # for i in range(r):
    #     distance.append([abs(i-current_xy[0]+j-current_xy[1])
    #                     for j in range(c)])
    # print(*distance, sep="\n")

    day = 0
    max_distance = 0

    # i, j = 0, 0
    # while(True):
    #     distance = []
    #     for k in range(r):
    #         distance.append([abs(k-current_xy[0]+l-current_xy[1])
    #                         for l in range(c)])
    #     if distance[i][j] < k:
    #         print(i, j)
    #     i += 1
    #     j += 1
    #     if i > r-1:
    #         break
    #     if j > c-1:
    #         break

    for i in range(r):
        for j in range(c):
            distance = []
            for k in range(r):
                distance.append([abs(k-current_xy[0]+l-current_xy[1])
                                 for l in range(c)])
            if distance[i][j] > k:
                continue
            if new_grid[i][j] == ".":
                if distance[i][j] > max_distance:
                    max_distance = distance[i][j]
                    current_xy = [i, j]
                print(i, j)

        day += 1
    print(day, i, j, max_distance)

    return answer


solution(["..FF", "###F", "###."], 4)  # 1
solution(["..FF", "###F", "###."], 5)  # 0

# ..FF
# ###F
# ###.
