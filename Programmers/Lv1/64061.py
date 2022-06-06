def solution(board, moves):
    answer = 0

    stacklist = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if stacklist and stacklist[-1] == board[j][i-1]:
                    stacklist.pop(-1)
                    answer += 2
                else:
                    stacklist.append(board[j][i-1])
                board[j][i-1] = 0
                break

    return answer
