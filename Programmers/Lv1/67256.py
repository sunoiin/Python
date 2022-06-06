def solution(numbers, hand):
    answer = ""
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    L, R = "*", "#"

    for num in numbers:
        if num in [1, 4, 7]:
            L = num
            answer += "L"
        elif num in [3, 6, 9]:
            R = num
            answer += "R"
        else:
            for i in range(4):
                for j in range(3):
                    if keypad[i][j] == num:
                        target = [i, j]
                    if keypad[i][j] == L:
                        L_corr = [i, j]
                    if keypad[i][j] == R:
                        R_corr = [i, j]

            # 왼쪽으로 누르는게 오른쪽 손보다 가까우면
            L_distance = abs(target[0]-L_corr[0])+abs(target[1]-L_corr[1])
            R_distance = abs(target[0]-R_corr[0])+abs(target[1]-R_corr[1])
            if L_distance < R_distance:
                answer += "L"
                L = num
            elif L_distance > R_distance:
                answer += "R"
                R = num
            else:
                if hand == "right":
                    answer += "R"
                    R = num
                else:
                    answer += "L"
                    L = num

    return answer
