# def solution(rows, columns, queries):
#     answer = []
#     board = [[i*columns+j+1 for j in range(columns)] for i in range(rows)]

#     new_data = [item[:] for item in board]
#     tmp_data = [item[:] for item in board]

#     for a, b, c, d in queries:
#         x1, y1, x2, y2 = a-1, b-1, c-1, d-1
#         stack = []

#         for i in range(x1, x2):
#             tmp_data[i][y1] = new_data[i+1][y1]
#             stack.append(tmp_data[i][y1])
#         for i in range(x1+1, x2+1):
#             tmp_data[i][y2] = new_data[i-1][y2]
#             stack.append(tmp_data[i][y2])
#         for i in range(y1+1, y2+1):
#             tmp_data[x1][i] = new_data[x1][i-1]
#             stack.append(tmp_data[x1][i])
#         for i in range(y1, y2):
#             tmp_data[x2][i] = new_data[x2][i+1]
#             stack.append(tmp_data[x2][i])

#         new_data = [item[:] for item in tmp_data]
#         answer.append(min(stack))

#     return answer


# print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# # print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
# # print(solution(100, 97, [[1, 1, 100, 97]]))

def solution(rows, columns, queries):
    answer = []
    board = [[i*columns+j+1 for j in range(columns)] for i in range(rows)]

    for a, b, c, d in queries:
        stack = []
        x1, y1, x2, y2 = a-1, b-1, c-1, d-1

        for i in range(y1, y2+1):
            stack.append(board[x1][i])
            if len(stack) == 1:
                continue
            else:
                board[x1][i] = stack[-2]
        for j in range(x1+1, x2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]
        for k in range(y2-1, y1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]
        for l in range(x2-1, x1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))
    return answer


# print(solution(6, 6, [[2, 2, 5, 4]]))
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
# print(solution(100, 97, [[1, 1, 100, 97]]))
