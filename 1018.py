n, m = map(int, input().split())

board = list()
for i in range(n):
    board.append(input())

white_board = """WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW""".split()

black_board = """BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB""".split()


cnt_list = list()

for i in range(n-7):
    for j in range(m-7):
        white_cnt = 0
        for k in range(8):
            for l in range(8):
                if board[i+k][j+l] != white_board[k][l]:
                    white_cnt += 1
        cnt_list.append(white_cnt)

for i in range(n-7):
    for j in range(m-7):
        black_cnt = 0
        for k in range(8):
            for l in range(8):
                if board[i+k][j+l] != black_board[k][l]:
                    black_cnt += 1
        cnt_list.append(black_cnt)

print(min(cnt_list))
